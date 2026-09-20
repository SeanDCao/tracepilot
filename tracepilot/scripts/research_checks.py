"""Optional deterministic checks for TracePilot research.

The AI defines the sample, interprets evidence, and writes the report. These
functions never fetch data, decide relevance, or generate report prose.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from urllib.parse import urlparse
import re


def valid_public_url(value: str | None) -> bool:
    if not isinstance(value, str) or not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.hostname) and not (
        parsed.username or parsed.password
    )


def placeholder_date(value: str | None) -> bool:
    """Recognize the 1970 epoch placeholders observed in saved Amazon samples."""
    if not isinstance(value, str):
        return False
    return value.strip().lower() in {
        "january 01, 1970", "january 1, 1970", "1970-01-01",
        "1970-01-01t00:00:00z", "1970-01-01t00:00:00+00:00",
    }


def deduplicate(records: list[dict]) -> dict:
    """Keep the first observation per native identity and expose conflicts.

    This does not infer identity from similar titles or review text. Changed
    prices and engagement can be observations at different times, not conflicts.
    """
    seen = {}
    duplicates = []
    conflicts = set()
    for record in records:
        key = tuple(record.get(field) for field in ("platform", "site", "kind", "id"))
        if not all(isinstance(part, str) and part for part in key):
            raise ValueError("Each record needs platform, site, kind and stable id")
        if key not in seen:
            seen[key] = record
            continue
        stable = ("text", "parent_id", "item_id")
        if any(seen[key].get(field) != record.get(field) for field in stable):
            conflicts.add(key)
        else:
            duplicates.append(key)
    return {
        "unique": [record for key, record in seen.items() if key not in conflicts],
        "duplicates": duplicates,
        "conflicts": sorted(conflicts),
    }


def _reddit_post_parts(value: str | None):
    if not valid_public_url(value):
        return None
    parsed = urlparse(value)
    if parsed.hostname != "reddit.com" and not parsed.hostname.endswith(".reddit.com"):
        return None
    match = re.search(r"/r/([^/]+)/comments/([^/]+)/([^/]+)", parsed.path, re.I)
    if not match:
        return None
    return tuple(part.lower() for part in match.groups())


def reddit_comment_belongs(post_url: str, comment_url: str | None) -> bool | None:
    """Compare subreddit, post ID and slug; None means a URL cannot be checked."""
    parent, child = _reddit_post_parts(post_url), _reddit_post_parts(comment_url)
    return None if parent is None or child is None else parent == child


def viewpoint_distribution(rows: list[dict], expected_ids: list[str], selection: str) -> list[dict]:
    """Count one predefined, fully coded sample; percentages remain sample-only."""
    if selection not in {"all_eligible", "systematic", "random", "purposive"}:
        raise ValueError("Declare how the sample was selected")
    if len(expected_ids) != len(set(expected_ids)) or not expected_ids:
        raise ValueError("Expected sample IDs must be unique and nonempty")
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)) or set(ids) != set(expected_ids):
        raise ValueError("Every planned eligible record must be coded exactly once")
    groups = defaultdict(list)
    for row in rows:
        if not all(row.get(key) for key in ("platform", "site", "kind")):
            raise ValueError("Missing platform, site or kind")
        if row.get("reviewed") is not True:
            raise ValueError("Every sample record must be reviewed")
        labels = row.get("labels")
        if not isinstance(labels, list) or not all(isinstance(x, str) for x in labels):
            raise ValueError("Each record needs a reviewed label list, possibly empty")
        if row.get("stance") not in {"positive", "negative", "neutral", "mixed", "unknown"}:
            raise ValueError("Each record needs a reviewed stance")
        groups[(row["platform"], row["site"], row["kind"], row.get("item_id"))].append(row)
    result = []
    for key, group in sorted(groups.items(), key=lambda item: str(item[0])):
        themes = Counter(label for row in group for label in set(row["labels"]))
        stances = Counter(row["stance"] for row in group)
        n = len(group)
        result.append({
            "platform": key[0], "site": key[1], "kind": key[2], "item_id": key[3],
            "denominator": n, "theme_counts": dict(sorted(themes.items())),
            "stance_counts": dict(sorted(stances.items())),
            "theme_sample_percent": (
                None if selection == "purposive"
                else {theme: round(count * 100 / n, 1) for theme, count in themes.items()}
            ),
            "selection": selection,
            "population_inference": False,
        })
    return result


def first_year_total(device_price, required_charges: list[dict], currency: str):
    """Sum explicit first-year payments; never guess billing schedule or currency."""
    if not currency:
        raise ValueError("Currency required")
    try:
        total = Decimal(str(device_price))
        if total < 0:
            raise ValueError("Device price cannot be negative")
        for charge in required_charges:
            if charge.get("currency") != currency:
                raise ValueError("Currency mismatch")
            amount = Decimal(str(charge["amount"]))
            payments = int(charge["payments_first_year"])
            if amount < 0 or payments < 0 or payments != charge["payments_first_year"]:
                raise ValueError("Invalid first-year payment")
            total += amount * payments
    except (TypeError, KeyError, InvalidOperation) as exc:
        raise ValueError("Incomplete price or first-year charge") from exc
    return total.quantize(Decimal("0.01"))
