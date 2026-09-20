#!/usr/bin/env python3
"""Create one isolated TracePilot research directory and print its path."""

import argparse
from datetime import datetime
from pathlib import Path
import secrets
import unicodedata


def topic_slug(topic: str) -> str:
    """Keep a short, path-safe label; callers must supply a nonsensitive topic."""
    normalized = unicodedata.normalize("NFKC", topic)
    parts = []
    pending_separator = False
    for char in normalized:
        if char.isalnum():
            if pending_separator and parts:
                parts.append("-")
            parts.append(char.lower())
            pending_separator = False
        else:
            pending_separator = True
    slug = "".join(parts).strip("-")[:24].rstrip("-")
    return slug or "research"


def create_run(runs_root: Path, topic: str) -> Path:
    root = runs_root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().astimezone().strftime("%Y%m%d-%H%M%S")
    slug = topic_slug(topic)
    for _ in range(10):
        run_dir = root / f"{timestamp}-{slug}-{secrets.token_hex(4)}"
        try:
            run_dir.mkdir(exist_ok=False)
        except FileExistsError:
            continue
        return run_dir
    raise RuntimeError("Could not create a unique research directory")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="Short, nonsensitive research topic")
    parser.add_argument(
        "--runs-root",
        type=Path,
        default=Path.cwd() / "analysis-runs",
        help="Parent directory for research runs (default: ./analysis-runs)",
    )
    args = parser.parse_args()
    print(create_run(args.runs_root, args.topic))


if __name__ == "__main__":
    main()
