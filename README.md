<div align="center">

# 🔎 TracePilot

**Define the question. Plan the evidence. Turn scattered sources into verifiable research.**

<p align="center">
  <a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-2563EB?style=flat-square&labelColor=0F172A"></a>
  <a href="README.zh-CN.md"><img alt="Simplified Chinese" src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-DBEAFE?style=flat-square&labelColor=0F172A"></a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: Apache 2.0" src="https://img.shields.io/badge/License-Apache--2.0-D9A441.svg"></a>
  <img alt="Version 1.4.0" src="https://img.shields.io/badge/version-1.4.0-0F766E.svg">
  <a href="tracepilot/SKILL.md"><img alt="Agent Skill: SKILL.md" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-7C3AED.svg"></a>
</p>

<p align="center">
  <b>Works with</b><br>
  <a href="https://learn.chatgpt.com/docs/build-skills"><img alt="Codex" src="https://img.shields.io/badge/Codex-111827?style=for-the-badge"></a>
  <a href="https://code.claude.com/docs/en/skills"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white"></a>
  <a href="https://cursor.com/docs/skills"><img alt="Cursor" src="https://img.shields.io/badge/Cursor-111827?style=for-the-badge&logo=cursor&logoColor=white"></a>
  <a href="https://opencode.ai/docs/skills"><img alt="OpenCode" src="https://img.shields.io/badge/OpenCode-334155?style=for-the-badge"></a>
  <a href="https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market"><img alt="WorkBuddy" src="https://img.shields.io/badge/WorkBuddy-1D4ED8?style=for-the-badge"></a>
  <br><sub>The core research instructions are portable across hosts that support <code>SKILL.md</code>. Available sources, RealTrace, structured choices, and tool operations depend on each host's live capabilities, connections, and permissions.</sub>
</p>

<i>Business · Policy · Technology · Society · Organizations · Events · Products · Reviews · Social media · Creators</i>

</div>

---

TracePilot (商航) is a general-purpose evidence research skill for AI.
It turns an open question into a scoped research plan, selects sources by evidentiary need, distinguishes claims from observations and inference, and produces a verifiable Markdown or HTML report.

It can be used for business, policy, technology, society, organizations, events, and other researchable questions. Product, review, social-media, creator, and cross-platform research are first-class specialties—not the limits of the skill.

## Works across agent hosts

TracePilot is portable research guidance, not a workflow tied to one agent product.
It is portable to **Codex, Claude Code, Cursor, OpenCode, WorkBuddy**, and other capable agent systems that can load reusable instructions and work with research tools or source material.

This repository uses a Codex-compatible skill package as its reference distribution.
Other hosts may require adapting the directory layout, manifest, invocation syntax, or tool connections.
The research method and evidence rules remain the same; compatibility with the `SKILL.md` format does not imply identical tool access or end-to-end validation on every host.
The sources and operations available in a task depend on the host's live capabilities, connections, and permissions.

## Why TracePilot

Many research agents begin with search and only later decide what the collected material means. TracePilot reverses that order:

1. Clarify the question, audience, scope, and decision context.
2. Plan the evidence, then use the host's live capabilities to set sources, scope, and stopping conditions before collecting data.
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

A rough topic is enough to begin—for example, “analyze Dell.”
If the purpose, object level, or comparison relationship could lead to fundamentally different studies, TracePilot asks a small set of task-specific single- or multiple-choice questions.
It also confirms names that may refer to different industries, models, accounts, people, or events.
When the user already provides a clear request, precise identifier, reliable context, or executable reference template, TracePilot proceeds to the existing research-planning workflow without forcing another questionnaire.

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

For a single factual question, TracePilot can answer directly.
When a task requires sampling or evidence synthesis into a report, it first confirms the research plan, source scope, depth, stopping conditions, and delivery format.
The readiness check only resolves the purpose, object, object level, and comparison relationship; the rest of the workflow remains unchanged.

## Outputs

- **Markdown by default:** readable, searchable, and easy for another person or AI to continue.
- **Optional HTML:** redesigned for sharing, narrow screens, and print when the user explicitly requests it.
- **Verifiable sourcing:** key objects and sources link to originals; material limitations stay next to the claims they affect.
- **Clean provenance:** every external report ends with a compact source appendix; raw responses, coding, calculations, and QA remain in the task workspace.

## Repository layout

```text
tracepilot/
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

Start with the current `tracepilot-*.zip` release package.
Keep the original ZIP unless the steps below explicitly ask you to extract it.

### Codex — easiest method

1. Open a local Codex task and attach the TracePilot ZIP.
2. Send the following request:

   ```text
   Please inspect the attached TracePilot Skill package without running its scripts. Install it as a user-level Codex Skill, then verify that Codex can recognize and invoke $tracepilot. If you need file access or another confirmation, ask me first.
   ```

3. Let Codex complete the file placement and checks. Approve file access only when the destination is the Codex user skills location.
4. If the new Skill does not appear immediately, restart Codex and try:

   ```text
   $tracepilot Tell me what you can research and how to start.
   ```

If you prefer installing from the repository, invoke `$skill-installer` in Codex and ask it to install the `tracepilot` Skill from `https://github.com/SeanDCao/tracepilot`. This also avoids manually handling hidden folders. See the [official OpenAI Skill guide](https://learn.chatgpt.com/docs/build-skills).

### WorkBuddy — easiest method

1. Open **Experts · Skills · Connectors → Skills** in the WorkBuddy sidebar.
2. Choose **Add Skill → Upload Skill**.
3. Select the original TracePilot ZIP; do not extract and re-compress it.
4. Wait for WorkBuddy to finish importing it, then confirm that TracePilot is enabled under **Installed**.
5. Start a conversation and try:

   ```text
   Use TracePilot to tell me what you can research and how to start.
   ```

If WorkBuddy reports that the package cannot be parsed, attach the ZIP to a normal WorkBuddy task and send:

```text
Please inspect the attached TracePilot Skill package without running its scripts. Create a WorkBuddy-compatible local copy, preserve the original research instructions and references, install it, and verify it with a simple read-only test. Tell me before requesting extra permissions or changing anything outside the Skill installation area.
```

See the [official WorkBuddy Skill guide](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market).

The core research workflow uses whatever sources are available to the host.
RealTrace is optional and is needed only for the corresponding connected-data workflows.
Interface names may change between host versions; if they do, look for **Skills**, **Add Skill**, or **Upload Skill**.

## Design boundaries

- Search snippets and result-list summaries are weak evidence, not substitutes for full source material.
- More sources do not automatically make a claim stronger; each source must change, support, qualify, or challenge the analysis.
- Platform engagement metrics are not added across platforms as if they shared one denominator.
- Sample patterns are not generalized to an entire market or population without adequate evidence.
- The skill does not predict creator ROI, bypass access controls, or treat unavailable data as verified fact.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

Copyright information and attribution notices are provided in [NOTICE](NOTICE).
