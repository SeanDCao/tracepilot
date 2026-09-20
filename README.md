# TracePilot

**Plan the evidence. Verify the sources. Deliver research people can inspect.**

[简体中文](README.zh-CN.md) · [Skill entry](skill/tracepilot/SKILL.md) · [Usage guide](skill/tracepilot/references/usage-guide.md)

TracePilot (商航) is a general-purpose evidence research skill for AI. It turns an open question into a scoped research plan, selects sources by evidentiary need, distinguishes claims from observations and inference, and produces a verifiable Markdown or HTML report.

It can be used for business, policy, technology, society, organizations, events, and other researchable questions. Product, review, social-media, creator, and cross-platform research are first-class specialties—not the limits of the skill.

> Current skill version: **1.2.2**

## Why TracePilot

Many research agents begin with search and only later decide what the collected material means. TracePilot reverses that order:

1. Clarify the question, audience, scope, and decision context.
2. Plan the evidence and stopping conditions before collecting data.
3. Use public sources, connected data tools, user-provided material, or RealTrace where appropriate.
4. Check entity, version, geography, time period, definitions, and counterevidence.
5. Separate source claims, sample observations, independent verification, inference, and unknowns.
6. Deliver a readable report with direct links, explicit limitations, and a compact source appendix.

## What it can research

- Business, organizations, industries, and competitive landscapes
- Policies, regulations, public events, and stakeholder positions
- Technologies, implementation approaches, and trade-offs
- Products, categories, pricing, variants, and purchase decisions
- Reviews, user needs, complaints, workarounds, and non-consumption
- Social topics, content performance, and disagreement patterns
- Creators, audience fit, content history, and collaboration risks
- Cross-platform questions that require evidence from different source types

TracePilot does not force every question into a fixed questionnaire, fixed sample size, or fixed report structure. It adapts the research design to the actual question while retaining strict evidence boundaries.

## Example prompts

```text
Use $tracepilot to compare these two devices for procurement in Germany. Cover positioning, verified specifications, user experience, total cost, and the strongest counterevidence.
```

```text
Use $tracepilot to explain how this new policy affects small organizations, including applicability, major disagreements, and unresolved questions.
```

```text
Use $tracepilot to study consumer needs in this category by combining product pages, reviews, social discussion, and relevant public sources.
```

For a single factual question, TracePilot can answer directly. When a task requires sampling or evidence synthesis into a report, it first confirms the research plan, source scope, depth, stopping conditions, and delivery format.

## Outputs

- **Markdown by default:** readable, searchable, and easy for another person or AI to continue.
- **Optional HTML:** redesigned for sharing, narrow screens, and print when the user explicitly requests it.
- **Verifiable sourcing:** key objects and sources link to originals; material limitations stay next to the claims they affect.
- **Clean provenance:** every external report ends with a compact source appendix; raw responses, coding, calculations, and QA remain in the task workspace.

## Repository layout

```text
skill/tracepilot/
├── SKILL.md                  # Skill entry and routing rules
├── agents/openai.yaml        # Display metadata and default prompt
├── references/
│   ├── workflow.md           # General research workflow
│   ├── report-design.md      # Evidence-led report design
│   ├── report-delivery.md    # Delivery and provenance rules
│   ├── html-report.md        # Optional HTML reporting guidance
│   ├── modes/                # Product, review, social, creator, cross-platform modes
│   └── sources/              # Public-web and RealTrace source guidance
└── scripts/                  # Deterministic run setup and research checks
```

## Installation

Use the `tracepilot` directory as a Codex-compatible skill package. Place it in your host's skills directory, or import the packaged release if your host supports skill imports. The core research workflow can operate with the sources available to the host; RealTrace is optional and only needed for the corresponding connected-data workflows.

After installation, invoke it with `$tracepilot` followed by the question you want to research.

## Design boundaries

- Search snippets and result-list summaries are weak evidence, not substitutes for full source material.
- More sources do not automatically make a claim stronger; each source must change, support, qualify, or challenge the analysis.
- Platform engagement metrics are not added across platforms as if they shared one denominator.
- Sample patterns are not generalized to an entire market or population without adequate evidence.
- The skill does not predict creator ROI, bypass access controls, or treat unavailable data as verified fact.

## Development

The repository includes contract tests for core positioning, evidence boundaries, specialist modes, and report provenance.

```bash
python3 -m unittest discover -s tests
```

Development notes and validation material are separate from the distributable skill package. See [START-HERE.md](START-HERE.md) for the current local development state.

## License

A public-use license has not yet been selected. Until a license file is added, the repository's contents remain subject to default copyright restrictions.
