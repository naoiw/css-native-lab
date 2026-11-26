# CSS Native Lab

CSS標準機能を、ブラウザ上で操作しながら学べる実験サイトです。レイアウト・状態制御・アニメーションなどを、JavaScriptや外部ライブラリを使わずに実装しています。[Web Native Lab](https://github.com/naoiw/web-native-lab) の姉妹プロジェクトです。

## 主な機能

- **12種類のCSS実験**：実際に操作できるデモと、CSSの最小コード例を掲載
- **MDNリファレンス**：各実験から仕様やブラウザ対応状況を確認可能
- **CSSのみで動作**：フレームワーク・JavaScript・ビルドツール・バックエンド不要
- **レスポンシブUI**：PC・スマートフォン向けの表示、キーボード操作、OSの「動きを減らす」設定に配慮

| 分類 | 実験 |
| --- | --- |
| レイアウト | Container Queries、Grid auto-fit、`aspect-ratio` |
| 状態・配色 | `:has()`、CSS Nesting、`color-mix()` |
| アニメーション | `@property`、Scroll-driven Animations、Scroll Snap |
| 新しいCSS機能 | Anchor Positioning、`@starting-style`、`mask-image` |

一部の機能はブラウザによって対応状況が異なります。Container QueriesとGrid auto-fitの実験では、デモ領域のサイズ変更に対応するブラウザ・入力環境が必要です。Anchor Positioning未対応時はPopoverを中央に表示し、Scroll-driven Animations未対応時は進捗バーが固定されます。

## 公開先

| 環境 | ブランチ | URL |
| --- | --- | --- |
| 本番 | `main` | https://naoiw.github.io/css-native-lab/ |

GitHub Pagesで公開しています。開発プレビュー用の常設ブランチは設けていません。

## 技術スタック

- **HTML / CSS** — 画面構造と12種類の標準CSS機能の実験
- **Python 3（標準ライブラリ）** — HTMLの参照先・アンカー・実験数などの構造チェック
- **GitHub Actions / GitHub Pages** — PR検証と本番デプロイ

Node.js・npm・JavaScript・CSSフレームワークは使用しません。

## ローカル開発

リポジトリを取得し、Python 3で静的ファイルを配信します。

```bash
git clone https://github.com/naoiw/css-native-lab.git
cd css-native-lab
python3 -m http.server 8000 --directory public
```

ブラウザで http://localhost:8000/ を開いてください。静的サイトのため `public/index.html` を直接開くこともできます。

変更後の構造チェック：

```bash
python3 scripts/check_site.py
```

このチェックはローカル参照・重複ID・実験数・CSSファイル量を検査します。HTML/CSSの完全な文法検証や実ブラウザの動作試験は含みません。

## ブランチ運用

1. `main` を本番ブランチとし、変更は作業ブランチで行います。
2. Pull RequestではGitHub Actionsの `validate` を実行し、デプロイは行いません。
3. `validate` 成功後にPRを `main` へマージすると、GitHub Pagesへ自動デプロイされます。
4. Ruleset `Protect main` でPR必須・force push禁止・削除制限を適用し、`validate` を必須チェックに設定しています。

## ディレクトリ構成

- `public/index.html` — 各実験のプレビュー、説明、CSSコード例
- `public/styles/site.css` — サイト全体のレイアウトとデザイン
- `public/styles/experiments.css` — CSS実験の実装
- `public/favicon.svg`、`robots.txt`、`sitemap.xml` — アイコン・検索エンジン向けファイル
- `scripts/check_site.py` — 静的構造チェック
- `.github/workflows/site.yml` — CI・GitHub Pagesへのデプロイ
- `docs/` — 設計・運用資料

## ドキュメント

- [設計・デプロイ構成](docs/architecture.md)
- [HTML標準機能の姉妹プロジェクト：Web Native Lab](https://github.com/naoiw/web-native-lab)

## ライセンス

[MIT License](LICENSE)
