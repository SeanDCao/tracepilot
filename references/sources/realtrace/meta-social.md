# RealTrace · Facebook／Instagram

**适用**：从帖子发现到评论目标解析。**状态**：下述路径来自截至 2026-09-17 的 V14 指南，尚无本项目端到端真实验收；调用前须读实时指南/schema。

当时指南要求由搜索返回的 content_url 先取帖子详情，再从详情取得 comment_target_id 或 media_id 取评论；列表 ID 不是通用评论入口。Facebook 账号内容另需数字 owner/page ID 与匹配主页 URL。不同端点的 ID 不可凭同名推断或混用。若当前工具缺少必要详情入口，改用可核对的公开页面或标明未解决，不拼造评论目标。
