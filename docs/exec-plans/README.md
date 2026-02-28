# 执行计划（Exec Plans）

复杂任务（3 步以上）应先写计划，再执行。

## 目录约定

- [active/](/docs/exec-plans/active/)：进行中的计划
- [completed/](/docs/exec-plans/completed/)：完成的计划
- [tech-debt-tracker.md](/docs/exec-plans/tech-debt-tracker.md)：持续性技术债跟踪
- [plan-template.md](/docs/exec-plans/plan-template.md)：新计划模板

> 新计划建议从模板复制：[plan-template.md](/docs/exec-plans/plan-template.md)。

## 单个计划建议结构

1. 背景与目标
2. 范围与非目标
3. 里程碑与验收标准
4. 风险与回滚方案
5. 决策日志（含日期）

## 与代理协作约定

- 计划必须可执行、可验证、可回溯。
- 每完成一个里程碑，更新计划状态并记录证据（命令/截图/日志摘要）。
- 需求变化时先更新计划，再改代码，避免漂移。
