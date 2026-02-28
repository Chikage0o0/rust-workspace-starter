## 变更说明

请简要说明本次改动的目的与背景（更关注 why，而非只列 what）。

## 改动类型

- [ ] 新功能
- [ ] 缺陷修复
- [ ] 重构
- [ ] 文档更新
- [ ] CI/工程治理

## 关联信息

- 关联 Issue: #
- 相关文档: `docs/...`

## 自检清单

- [ ] 我已阅读并遵守仓库工程约束（workspace 依赖、lint 继承等）
- [ ] 我已执行 `pre-commit run --all-files`
- [ ] 我已执行 `cargo clippy --workspace --all-targets -- -D warnings`
- [ ] 我已执行 `cargo nextest run --workspace --all-features --no-tests pass`
- [ ] 我已执行 `RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps`
- [ ] 我已同步更新必要文档（如 `docs/`）

## 验证结果

请粘贴关键验证输出或简述验证方式。

```text

```

## 风险与回滚

- 风险点:
- 回滚策略:
