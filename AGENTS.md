# AGENTS.md

本文件是仓库的"导航入口"，不是百科全书。
目标是让代理与人类都能快速找到真实约束与执行路径。

## 1) 快速开始（必须先读）

1. 进入开发环境：`devenv shell`
2. 安装/更新提交钩子：`enterShell` 会自动执行 `pre-commit install`
3. 本地质量闸门：
   - `pre-commit run --all-files`
   - `cargo clippy --workspace --all-targets -- -D warnings`
   - `cargo nextest run --workspace --all-features --no-tests pass`
   - `RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps`

## 2) 先看哪里（文档地图）

- 总索引：[docs/index.md](/docs/index.md)
- 工程原则：[docs/principles/agent-first.md](/docs/principles/agent-first.md)
- 仓库结构：[docs/architecture/repo-layout.md](/docs/architecture/repo-layout.md)
- 质量闸门：[docs/workflows/quality-gates.md](/docs/workflows/quality-gates.md)
- 执行计划：[docs/exec-plans/README.md](/docs/exec-plans/README.md)

## 3) 项目不变量（Invariants）

1. `Cargo.toml` 是 workspace 单一事实源：成员、依赖、lint、解析器都在根目录统一定义。
2. 所有第三方依赖必须定义在 `[workspace.dependencies]`；子 crate 仅通过 `workspace = true` 引用。
3. 子 crate 通过 `[lints] workspace = true` 继承 lint，不在每个 crate 重复配置。
4. Clippy 策略为 `all + pedantic`，默认在 CI/提交链路按 `-D warnings` 执行。
5. 测试以 `cargo nextest` 为准；无测试场景必须显式 `--no-tests pass`，避免空仓阻塞。
6. 文档构建必须零 warning（`RUSTDOCFLAGS=-D warnings`）。
7. 依赖通过 Nix/devenv 管理，不在系统全局随意安装。

## 4) 变更工作方式

1. 先改"约束与接口"，再改实现。
2. 小步提交：每次变更只做一件事，降低回归半径。
3. 若规则反复被人工提醒，优先把规则编码到 lint/脚本/钩子中。
4. 文档与代码同仓版本化；需求、计划、决策优先写入 `docs/`。

## 5) 完成定义（DoD）

- `pre-commit run --all-files` 通过。
- CI 本地等价命令可通过（fmt/clippy/check/nextest/doc）。
- 新增或变化的工程约束在 `docs/` 中有对应记录。
