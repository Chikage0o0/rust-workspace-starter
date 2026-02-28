---
name: Bug report
about: 报告缺陷并提供最小复现信息
title: "[Bug] "
labels: ["bug"]
assignees: []
---

## 问题描述

请清晰描述实际行为与期望行为的差异。

## 影响范围

- [ ] 构建/编译失败
- [ ] 测试失败
- [ ] 文档/流程错误
- [ ] 运行时功能异常

## 复现步骤

1.
2.
3.

## 最小复现（可选）

如可提供，请贴最小代码片段或仓库链接。

## 环境信息

- OS:
- Rust toolchain (`rustc -V`):
- Cargo (`cargo -V`):

## 日志与报错

请粘贴关键报错（勿包含密钥、Token、密码等敏感信息）。

```text

```

## 你已执行的检查

- [ ] `pre-commit run --all-files`
- [ ] `cargo clippy --workspace --all-targets -- -D warnings`
- [ ] `cargo nextest run --workspace --all-features --no-tests pass`
