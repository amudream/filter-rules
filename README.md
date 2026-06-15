# filter-rules

个人分流规则仓库。

## Quantumult X

### Binance / 币安

规则文件：

```text
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/Binance.list
```

QX 配置示例：

```ini
[filter_remote]
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/Binance.list, tag=Binance, update-interval=86400, opt-parser=false, enabled=true
```

默认策略名使用 `PROXY`。如果你的 Quantumult X 配置里没有名为 `PROXY` 的策略组，需要把规则文件最后一列的 `PROXY` 改成你自己的策略组名，例如 `节点选择`、`🚀 节点选择`、`Proxy`。

建议把币安规则放在 `GEOIP,CN,DIRECT` 和 `FINAL` 之前，否则可能不生效。
