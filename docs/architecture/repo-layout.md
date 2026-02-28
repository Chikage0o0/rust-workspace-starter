# 仓库结构

## 当前布局

```text
.
├── AGENTS.md
├── Cargo.toml
├── crates/
│   └── app/
├── docs/
│   ├── index.md
│   ├── principles/
│   ├── architecture/
│   ├── workflows/
│   └── exec-plans/
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
└── devenv.nix
```

## 设计约束

1. Rust 代码统一放在 `crates/`，避免根目录散落业务 crate。
2. 质量与流程配置集中在根目录（`Cargo.toml`、pre-commit、CI）。
3. 文档统一放在 `docs/`，并按主题分目录，便于代理按路径索引。

## 演进建议

- 新增业务模块时，优先新增 crate（例如 `crates/auth`、`crates/config`）。
- 分层与依赖方向规范见：[多 crate 分层与依赖方向](/docs/architecture/layering.md)。
- 当 crate 数量增长后，补充依赖边界图文档（例如 [dependency-graph](/docs/architecture/dependency-graph.md)）。
