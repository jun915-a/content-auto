# content-auto

HackerNews と Reddit のトレンドを自動収集し、バズ度スコアで厳選した記事を LLM で生成・複数プラットフォームに配信するシステム。

## 概要

GitHub Actions で **4時間ごと** に自動実行され、以下の処理を行います:

1. **トレンド収集** → HackerNews + Reddit から最新トレンドを取得
2. **バズ度スコアリング** → キーワード + ヒューリスティクスで「バズりそう」な記事を厳選（スコア10点以上）
3. **記事生成** → 日本語・英語の両言語で LLM により記事を自動生成（9段階フォールバック）
4. **自動投稿** → Blogger に日本語記事を自動投稿（SendGrid 経由）
5. **GitHub 保存** → 4形式の Markdown ファイルを articles/ に保存
6. **Discord 通知** → 投稿完了 + 手動投稿用 URL を通知
7. **手動投稿** → Note / Medium / Substack / Hashnode に手動でコピペ投稿

## 特徴

- **マルチ LLM フォールバック** — Groq → Gemini → Mistral → Together → Cohere（9段階）
- **Note 互換 Markdown** — `##` 見出しのみ、テーブル・コードブロック自動変換
- **完全自動化** — GitHub Actions で 4時間ごとに実行、Secrets で認証情報管理
- **低コスト** — 無料 API 枠を活用（Groq、Gemini、Mistral 等）
- **信頼性** → 投稿済み履歴管理で重複を防止、古い記事は自動削除

## システムフロー

```
[GitHub Actions (毎4時間)]
    ↓
[トレンド収集]
 HackerNews (30件) + Reddit (30件)
    ↓
[バズ度スコアリング]
 スコア10点以上のみ通過 → 上位5件を選定
    ↓
[記事生成 (LLM 9段階フォールバック)]
 日本語版 + 英語版 を同時生成
    ↓
[Blogger 自動投稿]
 SendGrid メール API 経由
    ↓
[GitHub に 4形式で保存]
 ja.md / en.md / ja_formatted.md / en_formatted.md
    ↓
[Discord 通知]
 Note / Medium / Substack / Hashnode 用 URL を送信
    ↓
[手動投稿]
 Discord の URL からコピペでプラットフォームに投稿
```

## クイックスタート

### 1. リポジトリをクローン

```bash
git clone https://github.com/jun915-a/content-auto.git
cd content-auto
```

### 2. 依存ライブラリをインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数を設定

```bash
cp .env.example .env
# .env を編集して API キーを記入
```

**最小限の設定（いずれか1つ以上必須）:**
```
GROQ_API_KEY=gsk_xxxx
GEMINI_API_KEY=AIzaSyxxx
```

**Blogger 自動投稿を使う場合:**
```
SENDGRID_API_KEY=SG.xxxx
SENDGRID_FROM_EMAIL=your@gmail.com
BLOGGER_BLOG_EMAIL=xxxx@blogger.com
```

**Discord 通知を使う場合:**
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxxx
```

### 4. ローカルで実行

```bash
python main.py
```

### 5. GitHub Actions で自動実行（オプション）

`.github/workflows/publish.yml` が存在すれば、GitHub Secrets に上記を設定するだけで自動実行開始。

## 記事生成の仕組み

### バズ度スコアリング

トレンドのタイトルと説明文から以下でスコアを計算:

**加点キーワード例（+3〜+25）:**
- 話題性: `breakthrough` (+25), `revolutionary`, `game-changing`
- AI企業: `openai` (+18), `anthropic` (+18), `gpt-5` (+20), `gpt-6` (+22)
- 感情喚起: `shocking` (+15), `leaked` (+20), `mind-blowing` (+18)
- 発表系: `launches` (+15), `unveils`, `reveals`

**減点キーワード例（-5〜-30）:**
- HN特殊投稿: `ask hn` (-25), `who is hiring` (-30)
- 古い記事: `(1975)` (-30), `vintage` (-15)
- 教本系: `tutorial` (-8), `introduction to` (-5)

**スコア補正:**
- タイトル長 40〜80文字: +8
- `?` 付き: +5
- 数字含む: +5
- 古い年号 `(19xx)`: -15
- 現在年を含む: +10（動的）

スコア10点以上のトレンドのみ記事化対象。

### LLM フォールバックチェーン

生成失敗時に自動的に次の LLM に切り替わります:

| 順番 | LLM | モデル | 特徴 |
|------|-----|--------|------|
| 1 | Groq | llama-3.3-70b-versatile | 高品質・高速 |
| 2 | Groq | llama-3.1-8b-instant | 70B の代替枠 |
| 3 | Gemini | gemini-2.5-flash | 広い無料枠 |
| 4-5 | Gemini | gemini-2.0-flash / lite | 安定稼働 |
| 6-7 | Mistral | small / ministral-8b | JSON mode 対応 |
| 8 | Together | Llama-3.3-70B-Instruct | 無料モデル |
| 9 | Cohere | command-r-08-2024 | 最終フォールバック |

全 API で JSON mode / structured output を有効化。

### 生成される記事の構造

Note 互換 Markdown（`##` 見出しのみ、テーブル・コードブロック禁止）:

```markdown
# [タイトル]

[冒頭要約 150-200文字]

## 📌 このトピックの本質
[200文字 コア解説]

## 🎯 5秒で分かるポイント
- ポイント1
- ポイント2
- ポイント3

## 📊 詳細解説
## 1. [要素1]
- 観点A / 説明A

## 2. [要素2]
> 💡 Insight: [重要示唆]

## 🚀 実世界への影響
- 影響1
- 影響2

## ✨ 結論
[締めメッセージ]
```

## ファイル構成

```
content-auto/
├── main.py                  # エントリポイント・全体オーケストレーション
├── config.py                # 設定値・環境変数読み込み
├── trend_ranker.py          # バズ度スコアリング
├── tracker.py               # 投稿履歴管理（重複除外）
├── article_storage.py       # 記事ファイル保存・git commit・Note互換サニタイズ
├── notifier.py              # Discord 通知
├── requirements.txt         # 依存ライブラリ
│
├── sources/
│   ├── base.py              # TrendItem / TrendSource 基底クラス
│   ├── news.py              # HackerNews ソース
│   └── reddit.py            # Reddit ソース
│
├── generators/
│   └── article.py           # LLM 記事生成（JSON mode + 9段階フォールバック）
│
├── publishers/
│   ├── base.py              # Publisher / PublishResult 基底クラス
│   └── blogger.py           # Blogger (SendGrid) 投稿
│
├── articles/                # 生成記事保存先（時刻ベースフォルダ）
│   └── YYYY-MM-DD-HHMMSS/
│       ├── ja.md
│       ├── en.md
│       ├── ja_formatted.md
│       └── en_formatted.md
│
├── published_history.json   # 投稿履歴（重複防止）
│
├── .github/workflows/
│   └── publish.yml          # GitHub Actions ワークフロー（0 */4 * * *）
│
├── SPEC.md                  # 詳細仕様書
├── README.md                # このファイル
└── .env.example             # 環境変数テンプレート
```

## 設定項目

### 必須

| 環境変数 | 用途 | 例 |
|---------|------|-----|
| `GROQ_API_KEY` または `GEMINI_API_KEY` | LLM | `gsk_xxxx` / `AIzaSyxxx` |

### Blogger 自動投稿（オプション）

| 環境変数 | 用途 | 例 |
|---------|------|-----|
| `SENDGRID_API_KEY` | SendGrid API | `SG.xxxx` |
| `SENDGRID_FROM_EMAIL` | 送信元メール | `your@gmail.com` |
| `BLOGGER_BLOG_EMAIL` | Blogger 受信メール | `xxxx@blogger.com` |

### その他（オプション）

| 環境変数 | 用途 | 例 |
|---------|------|-----|
| `MISTRAL_API_KEY` | Mistral LLM | `xxxx` |
| `TOGETHER_API_KEY` | Together LLM | `xxxx` |
| `COHERE_API_KEY` | Cohere LLM | `xxxx` |
| `DISCORD_WEBHOOK_URL` | Discord 通知 | `https://discord.com/api/webhooks/xxxx` |
| `REDDIT_SUBREDDITS` | Reddit 対象サブレディット | （config.py で定義） |

## トラブルシューティング

| 症状 | 原因 | 対処 |
|------|------|------|
| `[LLM] 全て失敗` | API クォータ枯渇 | 翌日待機または複数キーを追加 |
| `429` エラー連発 | 1日トークン制限超過 | 次の実行まで待機（4時間後） |
| Blogger に投稿されない | SendGrid From Email 未認証 | SendGrid コンソールで `SENDGRID_FROM_EMAIL` を認証 |
| Reddit 403エラー | GitHub Actions からブロック | 正常動作。HackerNews のみで続行 |
| 生成記事が0件 | バズ度フィルタで全除外 | `trend_ranker.py` の `min_score` を下げる |
| Discord 通知こない | Webhook URL 無効 | `.env` で `DISCORD_WEBHOOK_URL` を確認 |

## 投稿先プラットフォーム

| プラットフォーム | 言語 | 投稿方法 |
|----------------|------|---------|
| **Blogger** | 日本語 | 自動（SendGrid メール） |
| **Note** | 日本語 | 手動（Discord URL からコピペ） |
| **Medium** | 英語 | 手動（Discord URL からコピペ） |
| **Substack** | 英語 | 手動（Discord URL からコピペ） |
| **Hashnode** | 英語 | 手動（Discord URL からコピペ） |

## 開発

### コードスタイル

- Python 3.9+
- Type hints 推奨
- 簡潔性重視（過度な抽象化は避ける）

### テスト

```bash
# ローカル実行で動作確認
python main.py
```

## ライセンス

MIT

## 更新履歴

- **2026-04-21**: README 作成
- **2026-04-19**: Note 互換化・小さな修正・SPEC.md 更新
- **以前**: 初期実装・マルチ LLM フォールバック・Discord 通知等

---

質問や問題は [Issues](https://github.com/jun915-a/content-auto/issues) で報告してください。
