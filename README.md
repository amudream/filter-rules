# filter-rules

个人跨端分流规则项目。**GitHub 只管规则，私有订阅只管节点。**

## 最终分流目标

```text
OpenAI / ChatGPT / Codex / Sora / OpenAI 支付
                        -> OpenAI -> 菲律宾节点

Apple / LAN / 中国大陆 -> DIRECT

其他所有需要代理的流量
                        -> Personal -> 自己的普通节点
```

## 目录

```text
source/        自维护规则的唯一真源，只改这里
QuantumultX/   自动生成的 Quantumult X 规则
Mihomo/        自动生成的 Clash Verge Rev / Mihomo 规则
examples/      无密钥客户端示例
scripts/       规则生成器
UPSTREAMS.md   直接复用的成熟公共规则
```

`QuantumultX/` 和 `Mihomo/` **不要手改**。修改 `source/*.yaml` 后，GitHub Actions 会自动重新生成两端规则。

## 节点层与规则层分离

公开仓库不保存任何节点、订阅 token、UUID、Reality key 或 MITM 证书。

建议私有订阅内统一命名：

```text
OPENAI-PH-01
OPENAI-PH-02
PERSONAL-ANYTLS-01
PERSONAL-VLESS-01
```

客户端按名称筛选：

- `OpenAI` 组只选 `^OPENAI-PH-`
- `Personal` 组只选 `^PERSONAL-`

这样换服务器只改私有订阅；改分流只改这个 GitHub 仓库。

## 自维护规则

| 规则 | 默认目标 | QX | Mihomo |
|---|---|---|---|
| OpenAI | OpenAI / 菲律宾 | `QuantumultX/OpenAI.list` | `Mihomo/OpenAI.yaml` |
| WebRTC-Protect | Personal | `QuantumultX/WebRTC-Protect.list` | `Mihomo/WebRTC-Protect.yaml` |
| Binance | Personal | `QuantumultX/Binance.list` | `Mihomo/Binance.yaml` |
| Predict | Personal | `QuantumultX/Predict.list` | `Mihomo/Predict.yaml` |
| ClaudeCode | Personal | `QuantumultX/ClaudeCode.list` | `Mihomo/ClaudeCode.yaml` |
| WMLIA | DIRECT | `QuantumultX/WMLIA.list` | `Mihomo/WMLIA.yaml` |
| ChinaTLD | DIRECT | `QuantumultX/ChinaTLD.list` | `Mihomo/ChinaTLD.yaml` |

OpenAI 规则包含 OpenAI 自有域名、ChatGPT/Codex/Sora、实际观察到的区域化 Sentry endpoint，以及 Stripe/Link 等支付链路；它必须排在 Apple 和 CN 直连规则之前。

## 直接复用上游

Apple、LAN、中国大陆主规则不复制维护，见 [`UPSTREAMS.md`](UPSTREAMS.md)。

## 客户端示例

- Quantumult X：`examples/QuantumultX.conf.example`
- Clash Verge Rev / Mihomo：`examples/Mihomo.yaml.example`

示例中没有真实订阅或节点凭证。
