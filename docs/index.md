# 文档索引

本目录是仓库的工程知识库（System of Record）。

## 导航

- 工程原则：[Agent-First 工程原则](/docs/principles/agent-first.md)
- 仓库结构：[仓库结构](/docs/architecture/repo-layout.md)
- 分层约束：[多 crate 分层与依赖方向](/docs/architecture/layering.md)
- 质量闸门：[质量闸门](/docs/workflows/quality-gates.md)
- 执行计划：[执行计划（Exec Plans）](/docs/exec-plans/README.md)

## 维护规则

1. 新增工程约束时，必须同步更新对应文档。
2. 规则优先写成可执行检查（lint、脚本、hook），文档负责解释"为什么"。
3. 目录内文档以短小、可定位、可交叉链接为原则。
