# 多 crate 分层与依赖方向

本文件定义未来仓库扩展到多个 crate 时的依赖方向约束。
目标是让结构可预测、可检查、可长期演进。

## 分层模型

建议按业务域拆 crate，并在域内保持固定分层：

1. `types`：领域类型、错误类型、协议结构。
2. `config`：配置读取与校验。
3. `repo`：外部数据访问（DB、HTTP、文件系统）。
4. `service`：业务编排与领域规则。
5. `runtime`：进程启动、任务调度、依赖装配。
6. `ui`（可选）：CLI/HTTP handler/页面层。

## 依赖方向（硬约束）

仅允许“向前依赖”：

- `types` -> 无域内依赖。
- `config` -> `types`。
- `repo` -> `types` | `config`。
- `service` -> `types` | `config` | `repo`。
- `runtime` -> `types` | `config` | `repo` | `service`。
- `ui` -> `types` | `config` | `repo` | `service` | `runtime`。

禁止反向依赖与跨层回跳（例如 `repo` 依赖 `service`）。

## workspace 层约束

1. 根 `Cargo.toml` 作为单一事实源，统一管理：
   - workspace members
   - `[workspace.dependencies]`
   - `[workspace.lints.*]`
2. 所有第三方依赖必须定义在 `[workspace.dependencies]`，禁止在子 crate 写版本号。
3. 子 crate 仅允许以 `workspace = true` 引用依赖。
4. 各 crate 必须声明：

```toml
[lints]
workspace = true
```

5. 公共能力优先下沉为共享 crate，避免在多个业务 crate 复制工具函数。

## 跨域协作约束

1. 业务域之间只通过公开接口交互，不直接引用对方内部模块。
2. 跨域调用优先依赖 trait/port，而不是直接依赖具体实现。
3. 遥测、鉴权、特性开关等横切能力通过 provider/infrastructure crate 注入。

## 落地与校验建议

当前先用文档约束，后续可逐步机械化：

1. 用 `cargo metadata` + 脚本做依赖方向检查。
2. 在 CI 增加“结构测试”任务，阻止非法依赖边。
3. 当 crate 数量 >= 5 时，补充 [dependency-graph](/docs/architecture/dependency-graph.md) 可视化依赖图。
