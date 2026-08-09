# Upstream rules

成熟、维护活跃的公共规则不复制进本仓库，客户端直接引用上游；本仓库只维护自己的补充/私有规则。

## Apple

- Quantumult X: `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Apple/Apple.list`
- 建议策略：`DIRECT`
- Mihomo: 优先使用内置 GeoSite：`GEOSITE,apple,DIRECT`

OpenAI 规则必须排在 Apple 前，因为 `humb.apple.com` 是 OpenAI 依赖中的单点例外。

## LAN / private

- Quantumult X: `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Lan/Lan.list`
- 建议策略：`DIRECT`
- Mihomo: 在客户端配置中直接使用 RFC1918/private CIDR 直连规则。

## China mainland

- Quantumult X 域名集：`https://raw.githubusercontent.com/QuixoticHeart/rule-set/refs/heads/ruleset/quantumultx/cn.list`
- 本仓库补充：`QuantumultX/ChinaTLD.list`
- Mihomo: `GEOSITE,cn,DIRECT` + `GEOIP,CN,DIRECT`
- 本仓库补充：`Mihomo/ChinaTLD.yaml`

## 原则

1. 上游已经成熟：直接引用，不 fork 一份静态副本。
2. 上游缺失或需要自己的行为：写入 `source/`。
3. `QuantumultX/` 与 `Mihomo/` 都是生成物，不直接手改。
4. 节点、订阅 URL、UUID、Reality key、MITM 证书永远不进入此公开仓库。
