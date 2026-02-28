#!/usr/bin/env python3
"""检查子 crate 是否直接声明依赖版本。

规则：第三方依赖必须在根 Cargo.toml 的 [workspace.dependencies] 统一定义，
子 crate 只能通过 `workspace = true` 引用。
"""

from __future__ import annotations

from pathlib import Path
import sys
import tomllib


DEPENDENCY_SECTIONS = ("dependencies", "dev-dependencies", "build-dependencies")


def check_dependency_table(
    table: dict, manifest: Path, section: str, violations: list[str]
) -> None:
    for name, spec in table.items():
        if isinstance(spec, str):
            violations.append(
                f"{manifest}: [{section}] {name} 直接使用字符串版本 `{spec}`，应改为 workspace = true"
            )
            continue

        if not isinstance(spec, dict):
            continue

        if spec.get("workspace") is True:
            continue

        if "version" in spec:
            violations.append(
                f"{manifest}: [{section}] {name} 直接声明 version，必须改为 workspace = true"
            )


def check_manifest(manifest: Path, violations: list[str]) -> None:
    data = tomllib.loads(manifest.read_text(encoding="utf-8"))

    for section in DEPENDENCY_SECTIONS:
        table = data.get(section)
        if isinstance(table, dict):
            check_dependency_table(table, manifest, section, violations)

    targets = data.get("target")
    if not isinstance(targets, dict):
        return

    for target_name, target_cfg in targets.items():
        if not isinstance(target_cfg, dict):
            continue
        for section in DEPENDENCY_SECTIONS:
            table = target_cfg.get(section)
            if isinstance(table, dict):
                scoped = f"target.{target_name}.{section}"
                check_dependency_table(table, manifest, scoped, violations)


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    crates_dir = repo_root / "crates"

    if not crates_dir.exists():
        print("未找到 crates/ 目录，跳过依赖策略检查。")
        return 0

    violations: list[str] = []
    manifests = sorted(crates_dir.rglob("Cargo.toml"))

    for manifest in manifests:
        check_manifest(manifest, violations)

    if not violations:
        print("workspace 依赖策略检查通过。")
        return 0

    print("发现子 crate 直接声明依赖版本，违反 workspace 依赖治理规则：")
    for violation in violations:
        print(f"- {violation}")

    print(
        "\n修复方式：将依赖迁移到根 Cargo.toml 的 [workspace.dependencies]，并在子 crate 使用 workspace = true。"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
