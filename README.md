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

### Predict

规则文件：

```text
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/Predict.list
```

QX 配置示例：

```ini
[filter_remote]
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/Predict.list, tag=Predict, update-interval=86400, opt-parser=false, enabled=true
```

当前规则覆盖：

- `predict.fun` 主站、API 和 WebSocket
- `relay.walletconnect.org` 钱包连接中继
- `eth.llamarpc.com` Ethereum RPC

默认策略名使用 `PROXY`。如果你的 Quantumult X 配置里没有名为 `PROXY` 的策略组，需要把规则文件最后一列的 `PROXY` 改成你自己的策略组名，例如 `节点选择`、`🚀 节点选择`、`Proxy`。

建议把这些规则放在 `GEOIP,CN,DIRECT` 和 `FINAL` 之前，否则可能不生效。

### WebRTC / STUN 防直连

规则文件：

```text
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/WebRTC-Protect.list
```

QX 配置示例：

```ini
[filter_remote]
https://raw.githubusercontent.com/amudream/filter-rules/main/QuantumultX/WebRTC-Protect.list, tag=WebRTC-Protect, force-policy=Global, update-interval=172800, opt-parser=false, inserted-resource=true, enabled=true
```

这条远程资源必须放在 `ChinaMax` 等宽泛直连资源之前，并指向支持 UDP 的代理策略。浏览器端仍建议启用 Chrome 的 `WebRtcIPHandling=disable_non_proxied_udp` 作为最终防线。
