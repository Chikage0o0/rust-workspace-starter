# rust-workspace-starter

一个面向团队协作的 Rust Workspace 模板仓库，内置一致化质量闸门与工程约束，适合作为 GitHub Template 快速派生新项目。

## 特性

- Rust workspace 单一事实源（根 `Cargo.toml` 统一管理）
- 预置质量闸门：`fmt`、`clippy`、`check`、`nextest`、`doc`
- 预置 pre-commit 与 CI，保证本地与 CI 检查一致
- 文档结构化：原则、架构、流程、执行计划分层维护

## 快速开始

1. 点击 GitHub 仓库页面的 **Use this template** 创建新仓库
2. 克隆你的新仓库并进入目录
3. 进入开发环境：

```bash
devenv shell
```

4. 执行本地质量闸门：

```bash
pre-commit run --all-files
cargo clippy --workspace --all-targets -- -D warnings
cargo nextest run --workspace --all-features --no-tests pass
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps
```

## 模板约束

- 所有第三方依赖统一声明在根 `Cargo.toml` 的 `[workspace.dependencies]`
- 子 crate 通过 `workspace = true` 引用依赖
- 子 crate 通过 `[lints] workspace = true` 继承 lint

## 文档入口

- 总索引：`docs/index.md`
- 工程原则：`docs/principles/agent-first.md`
- 仓库结构：`docs/architecture/repo-layout.md`
- 质量闸门：`docs/workflows/quality-gates.md`

## 许可证

本项目采用 MIT 协议，详见 `LICENSE`。
