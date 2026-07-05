# **DMARCの「NP」タグとDNSSECの不一致**

DMARCの「NP」タグがDNSSECと不一致になる可能性を調べるために、DMARCwiseに寄稿したエンジニアは、DMARCの「NP」タグとDNSSECの不一致の根本原因を明らかにしました。

## このトピックの本質
DMARCの「NP」タグとDNSSECの不一致の根本原因は、DNSSECの署名がDMARCレポートの検証に影響を与えることにある。
## 5秒で分かるポイント
- **Point 1**: DMARCの「NP」タグがDNSSECと不一致になる可能性がある
- **Point 2**: DNSSECの署名がDMARCレポートの検証に影響を与える
- **Point 3**: DMARCの「NP」タグとDNSSECの対応策が必要

## 詳細解説
**DMARCレポートの検証**
DMARCレポートの検証はDNSSECの署名によって影響を受けることがある。これは、DMARCレポートが署名されたDNSSECのレコードを検証する必要があるからだ。
**DNSSEC署名の影響**
DNSSECの署名はDMARCレポートの検証に影響を与える。署名が不正である場合、DMARCレポートの検証に失敗する可能性がある。
> 💡 ポイント: DNSSECの署名がDMARCレポートの検証に影響を与える

## 実世界への影響
- DMARCの「NP」タグがDNSSECと不一致になる可能性が高くなる
- DMARCレポートの検証に失敗し、DMARCの機能が低下する
- DNSSECの署名が不正な場合、DMARCレポートの検証に影響を与える

## 結論
DMARCの「NP」タグとDNSSECの不一致の根本原因はDNSSECの署名による影響である。DMARCの「NP」タグとDNSSECの対応策が必要である。
