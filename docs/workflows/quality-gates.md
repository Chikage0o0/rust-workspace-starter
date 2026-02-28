# 质量闸门

本项目采用"本地等价 CI"原则：本地通过即应接近 CI 通过。

## 必过检查

1. `cargo fmt --all -- --check`
2. `cargo clippy --workspace --all-targets -- -D warnings`
3. `cargo check --workspace`
4. `cargo nextest run --workspace --all-features --no-tests pass`
5. `RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps`

## 执行位置

- 本地提交：`.pre-commit-config.yaml`
- 远端 CI：`.github/workflows/ci.yml`

## 失败处理约定

1. 先修复失败，再继续功能开发。
2. 若规则噪声过大，优先做"规则调优"，不要绕过检查。
3. 对于空测试场景，必须保留 `--no-tests pass`，避免流程被空仓卡住。

## 依赖治理约束

1. 新增依赖时，仅允许修改根 `Cargo.toml` 的 `[workspace.dependencies]`。
2. 子 crate 依赖必须使用 `workspace = true` 引用，不得直接写版本号。
