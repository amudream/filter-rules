#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
QX_DIR = ROOT / "QuantumultX"
MIHOMO_DIR = ROOT / "Mihomo"

QX_TYPES = {
    "domain": "HOST",
    "domain-suffix": "HOST-SUFFIX",
    "domain-keyword": "HOST-KEYWORD",
    "domain-wildcard": "HOST-WILDCARD",
}
MIHOMO_TYPES = {
    "domain": "DOMAIN",
    "domain-suffix": "DOMAIN-SUFFIX",
    "domain-keyword": "DOMAIN-KEYWORD",
    "domain-wildcard": "DOMAIN-WILDCARD",
}

def build_one(path: Path) -> None:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    name = data["name"]
    target = data["target"]
    rules = data["rules"]

    qx_policy = "direct" if str(target).upper() == "DIRECT" else target
    qx_lines = [
        "# GENERATED FILE - DO NOT EDIT",
        f"# Source: source/{path.name}",
        f"# Target: {target}",
        "# Edit source/ and let GitHub Actions rebuild this file.",
        "",
    ]
    mihomo_lines = [
        "# GENERATED FILE - DO NOT EDIT",
        f"# Source: source/{path.name}",
        f"# Suggested target: {target}",
        "# Use as a Mihomo rule-provider with behavior: classical.",
        "payload:",
    ]

    for rule in rules:
        kind = rule["type"]
        value = str(rule["value"])
        if kind not in QX_TYPES:
            raise ValueError(f"{path}: unsupported rule type {kind}")
        qx_lines.append(f"{QX_TYPES[kind]},{value},{qx_policy}")
        mihomo_lines.append(f"  - '{MIHOMO_TYPES[kind]},{value}'")

    QX_DIR.mkdir(parents=True, exist_ok=True)
    MIHOMO_DIR.mkdir(parents=True, exist_ok=True)
    (QX_DIR / f"{name}.list").write_text("\n".join(qx_lines) + "\n", encoding="utf-8")
    (MIHOMO_DIR / f"{name}.yaml").write_text("\n".join(mihomo_lines) + "\n", encoding="utf-8")

def main() -> None:
    for path in sorted(SOURCE.glob("*.yaml")):
        build_one(path)

if __name__ == "__main__":
    main()
