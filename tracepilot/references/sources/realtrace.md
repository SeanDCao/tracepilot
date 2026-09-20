# RealTrace 通用运行规则

只在当前任务确需 RealTrace 时加载。平台专项窍门不是永久 API 文档：每次新会话实际调用前先发现可用工具，读实时 get_agent_instructions 的 core 与当前业务层，并核对当前工具声明；更多/尽可能全量或后台任务时再读相关层。宿主若仅暴露开放对象形状，不能声称已取得完整 inputSchema。历史实测只证明当时的具体参数组合，不替代当前契约。

使用用户提供或前序搜索/详情返回的稳定 ID；不从显示名、标题或 URL 猜造机器码。默认每次一个平台、顺序执行。可能同时启动多个后台任务前查实时容量和 allowed_actions；不擅自取消其他任务。后台受理且 data 为空不是最终空结果，保存 task_id/progress_version，按 next_action 读取状态和全部结果。cursor 只回传紧邻响应，同一查询条件内使用；结果读完、任务完成、达到请求目标、上游自然耗尽分别记录。不可重试错误不原样重试。

原始响应与字段映射按任务留存。指南描述为 documented，当前工具参数核对为 schema_verified，真实返回并检查筛选/归属后才叫 sample_verified。搜索摘要不充当详情，不能替代商品规格、正文、字幕、画面、评论或稳定对象 ID；若详情确实不可达，只能按[公开检索规则](public-web.md)把标题或列表概要降级为受限弱证据。缺失值不是零；来源方宣称不自动变成实测性能。记录实际业务调用、收费和后台未分摊费用；没有用户指定上限时按证据缺口与边际价值取样，不沿用开发测试额度。

按当前操作才读专项：

| 操作 | 专项窍门 |
| --- | --- |
| Amazon 商品评论，尤其大样本或尽可能全量 | [Amazon 评论](realtrace/amazon-reviews.md) |
| YouTube 内容、评论和频道 | [YouTube](realtrace/youtube.md) |
| Reddit 帖子和评论 | [Reddit](realtrace/reddit.md) |
| TikTok 内容与创作者 | [TikTok](realtrace/tiktok.md) |
| Facebook／Instagram 评论入口 | [Meta 社媒](realtrace/meta-social.md) |
| 其他平台创作者标准 ID | [创作者 ID](realtrace/creator-ids.md) |

专项文件的状态与日期只界定**那条窍门**验证到哪一步；调用时以实时指南、schema 和当前响应为准。某平台未列专项，按通用规则探索，不套用别的平台参数。
