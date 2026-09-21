<div align="center">

# 🔎 商航 TracePilot

**先定义问题，再规划证据——把分散资料变成可核验的研究结论。**

<p align="center">
  <a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-DBEAFE?style=flat-square&labelColor=0F172A"></a>
  <a href="README.zh-CN.md"><img alt="简体中文" src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-2563EB?style=flat-square&labelColor=0F172A"></a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="许可证：Apache 2.0" src="https://img.shields.io/badge/License-Apache--2.0-D9A441.svg"></a>
  <img alt="版本 1.3.0" src="https://img.shields.io/badge/version-1.3.0-0F766E.svg">
  <a href="tracepilot/SKILL.md"><img alt="Agent Skill：SKILL.md" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-7C3AED.svg"></a>
</p>

<p align="center">
  <b>适用于</b><br>
  <a href="https://learn.chatgpt.com/docs/build-skills"><img alt="Codex" src="https://img.shields.io/badge/Codex-111827?style=for-the-badge"></a>
  <a href="https://code.claude.com/docs/en/skills"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white"></a>
  <a href="https://cursor.com/docs/skills"><img alt="Cursor" src="https://img.shields.io/badge/Cursor-111827?style=for-the-badge&logo=cursor&logoColor=white"></a>
  <a href="https://opencode.ai/docs/skills"><img alt="OpenCode" src="https://img.shields.io/badge/OpenCode-334155?style=for-the-badge"></a>
  <a href="https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market"><img alt="WorkBuddy" src="https://img.shields.io/badge/WorkBuddy-1D4ED8?style=for-the-badge"></a>
  <br><sub>核心研究指令可在支持 <code>SKILL.md</code> 的宿主中使用；实际可用来源、RealTrace、结构化选择和工具操作取决于宿主的实时能力、连接与权限。</sub>
</p>

<i>商业 · 政策 · 技术 · 社会 · 组织 · 事件 · 商品 · 评论 · 社媒 · 创作者</i>

</div>

---

商航 TracePilot 是一套面向 AI 的通用证据研究 Skill。
它把开放问题转化为有边界的研究方案，从问题所需证据反推来源，区分来源方陈述、样本观察、独立核验、推断与未知，并交付可核验的 Markdown 或 HTML 报告。

它可用于商业、政策、技术、社会、组织、事件及其他能够界定和核验的问题。商品、评论、社媒、创作者与跨平台研究是它的核心专项能力，但不是使用边界。

## 可应用于多个智能体宿主

TracePilot 是一套可迁移的研究指导，不是绑定某个智能体产品的固定工作流。
它可以迁移至 **Codex、Claude Code、Cursor、OpenCode、WorkBuddy**，以及其他能够加载复用指令并使用研究工具或来源材料的智能体系统。

本仓库以 Codex 兼容的 Skill 包作为参考发行格式。
其他宿主可能需要适配目录结构、清单文件、调用语法或工具连接方式。
研究方法和证据规则保持一致；兼容 `SKILL.md` 格式不等于所有宿主都具备相同工具访问能力，也不表示均已完成同等程度的端到端验证。
具体任务可使用的来源与操作，取决于宿主当时具备的实时能力、连接和权限。

## 为什么是 TracePilot

很多研究型 AI 助手会先搜索，再决定材料意味着什么。TracePilot 把顺序倒过来：

1. 先理解问题、读者、范围和实际用途。
2. 取数前规划证据，并依据宿主实时能力安排来源、范围与停止条件。
3. 按需使用公开资料、已连接数据工具、用户资料或 RealTrace。
4. 核对实体、版本、地域、时期、定义、统计口径与反证。
5. 区分来源方说法、样本观察、独立验证、推断和未知。
6. 交付带原始链接、关键限制和简洁来源附录的可读报告。

## 可以研究什么

- 商业、组织、行业与竞争格局
- 政策、制度、公共事件与利益相关方观点
- 技术路线、实施约束与取舍
- 商品、品类、价格、变体与购买决策
- 评论、用户需求、抱怨、替代做法与非消费
- 社媒话题、内容表现、主要观点与分歧
- 创作者、受众匹配、内容历史与合作风险
- 需要多类来源相互补证的跨平台问题

TracePilot 不会把所有问题塞进固定问卷、固定样本量或固定报告结构。它会根据实际问题动态设计研究，同时守住一致的证据边界。

只知道大致主题也可以开始，例如“分析一下戴尔”。
当目的、对象层级或比较关系可能把研究带向不同方向时，TracePilot 会用少量单选或多选题帮助确认。
遇到同名、跨行业、型号或账号歧义时，它会先确认对象。
已经提供清晰要求、精确链接或型号、可靠上下文或参考分析模板时，则直接进入原有研究规划，不强制重复询问。

## 提问示例

```text
使用 $tracepilot 比较这两款设备在德国市场的定位、已核验规格、真实体验、总成本和最强反证，用于采购决策。
```

```text
使用 $tracepilot 解释这项新规对中小机构的适用条件、主要影响、争议和仍未解决的问题。
```

```text
使用 $tracepilot 研究这个品类的消费者需求，综合商品页、评论、社媒讨论与相关公开资料。
```

单一事实或轻量解释可以直接回答。
需要取样、整合证据并交付报告时，TracePilot 会先确认研究问题、范围、来源、深度、停止条件与交付格式。
前置澄清只解决目的、对象、对象层级和比较关系是否足够明确；其余研究步骤保持原有顺序。

## 交付方式

- **默认 Markdown：**便于阅读、检索，也方便人或其他 AI 继续分析。
- **可选 HTML：**用户明确选择时，重新设计为适合分享、窄屏与打印的独立页面。
- **关键内容可核验：**正文中的重要对象和来源链接到原文，限制紧跟它所影响的结论。
- **来源清楚但不过载：**每份对外报告以简洁来源附录收尾；原始响应、编码、计算和 QA 留在任务工作区。

## 仓库结构

```text
tracepilot/
├── SKILL.md                  # Skill 正式入口与路由规则
├── agents/openai.yaml        # 展示信息与默认提示词
├── references/
│   ├── workflow.md           # 通用研究工作法
│   ├── report-design.md      # 证据导向的报告设计
│   ├── report-delivery.md    # 交付与来源规则
│   ├── html-report.md        # 可选 HTML 报告指导
│   ├── modes/                # 商品、评论、社媒、创作者、跨平台专项
│   └── sources/              # 公开资料与 RealTrace 来源指导
└── scripts/                  # 确定性的任务目录与研究检查脚本
```

## 安装与使用

先准备当前版本的 `tracepilot-*.zip` 发布包。
除非下面的步骤明确要求，否则不要自行解压或重新打包。

### Codex：最省事的安装方式

1. 在本机 Codex 中新建一个任务，把 TracePilot 压缩包作为附件发给 Codex。
2. 复制并发送下面这段话：

   ```text
   请检查附件中的 TracePilot Skill 安装包，安装时不要运行其中的脚本。请把它安装为我的用户级 Codex Skill，然后确认 Codex 能识别并调用 $tracepilot。如果需要文件访问权限或其他确认，请先询问我。
   ```

3. 等 Codex 完成文件放置和检查。只有当它说明目标是 Codex 的用户 Skill 目录时，再允许相应的文件访问。
4. 如果新 Skill 没有马上出现，重启一次 Codex，然后发送：

   ```text
   $tracepilot 请介绍你能研究什么，以及我应该怎样开始。
   ```

如果不想下载压缩包，也可以在 Codex 中调用 `$skill-installer`，请它从 `https://github.com/SeanDCao/tracepilot` 安装 `tracepilot` Skill。这样同样不需要自己寻找隐藏目录。详见 [OpenAI 官方 Skill 指南](https://learn.chatgpt.com/docs/build-skills)。

### WorkBuddy：最省事的安装方式

1. 在 WorkBuddy 左侧打开 **专家 · Skills · Connectors → Skills**。
2. 选择 **添加技能 → 上传技能**。
3. 选择 TracePilot 的原始压缩包；不要先解压再重新压缩。
4. 等待 WorkBuddy 完成导入，然后在 **已安装** 中确认 TracePilot 已启用。
5. 新建一个对话，发送：

   ```text
   使用 TracePilot 介绍你能研究什么，以及我应该怎样开始。
   ```

如果 WorkBuddy 提示压缩包无法解析，可以把压缩包发到普通 WorkBuddy 任务中，再发送：

```text
请检查附件中的 TracePilot Skill 安装包，检查时不要运行其中的脚本。请创建一个兼容 WorkBuddy 的本地副本，保留原始研究指令和引用资料，完成安装，并用一个简单的只读任务验证。需要额外权限或修改 Skill 安装区域之外的内容前，请先告诉我。
```

详见 [WorkBuddy 官方技能说明](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

核心研究工作流会使用宿主当前可用的来源。
RealTrace 是可选能力，只在相应的连接数据工作流中需要。
不同版本的界面名称可能略有变化；找不到上述入口时，可以寻找 **Skills／技能**、**添加技能** 或 **上传技能**。

## 设计边界

- 搜索摘要和结果列表只能作为弱证据，不能代替完整原文。
- 来源数量多不等于主张更可靠；每个新增来源都应支持、修正、反驳或补充分析。
- 不把不同平台的互动量简单相加为一个“总热度”。
- 没有充分证据时，不把样本现象外推为整个市场或人群结论。
- 不预测创作者 ROI，不绕过访问控制，也不把不可用数据写成已核实事实。

## 许可证

本项目采用 [Apache License 2.0](LICENSE) 许可。

版权信息和署名声明请参阅 [NOTICE](NOTICE)。
