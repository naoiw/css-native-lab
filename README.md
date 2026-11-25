# CSS Native Lab

CSS標準機能を実際に触って学ぶ、フレームワーク不要の実験サイトです。[Web Native Lab](https://github.com/naoiw/web-native-lab) の姉妹プロジェクトです。

**リポジトリ:** https://github.com/naoiw/css-native-lab

- CSSが主言語（実装コードを `styles/*.css` に集約）
- **JavaScript 0行**、npm・バンドラ・外部UIライブラリなし
- 12種類の実験。各デモは操作可能で、短いCSSコード例・MDNリンク付き
- 新しいCSS機能は段階的に適用し、未対応時の代替表示を用意
- キーボードフォーカス・動きの低減設定に配慮

## 実験一覧

| カテゴリ | CSS機能 | 動作 |
| --- | --- | --- |
| Layout | Container Queries | コンテナ幅で部品が変わる |
| Layout | Grid auto-fit | コンテナ幅で列数を自動調整 |
| Layout | aspect-ratio | 縦横比を維持 |
| State | :has() | 子要素のチェック状態で見た目を変更 |
| State | CSS Nesting | ネストしたホバー / フォーカス |
| State | color-mix() | CSSのみで配色を合成 |
| Motion | @property | 型付きカスタムプロパティをアニメーション |
| Motion | Scroll-driven Animations | スクロールに連動するプログレスバー |
| Motion | Scroll Snap | スクロール位置を吸着 |
| New | Anchor Positioning | 要素に追従するPopover |
| New | @starting-style | Popoverの登場・退場演出 |
| New | mask-image | 見える領域をマスクで切り替え |

`Container Queries` や `Grid auto-fit` のデモは、右下のリサイズハンドルをドラッグして試します。タッチ端末ではハンドルが操作できない場合があります。

**Progressive** 機能はブラウザごとに対応状況が異なります。Anchor Positioningは未対応時に中央表示、Scroll-driven Animationsは未対応時にバーが固定となります。各デモのMDNリンクで対応状況を確認してください。

## ローカル実行

`public/index.html` を直接開くか、次のようにサーバーを起動します。

```sh
python3 -m http.server 8000 --directory public
```

http://localhost:8000 で確認できます。Node.js / npmは不要です。

## 構造チェック

```sh
python3 scripts/check_site.py
```

ローカルのファイル参照、ページ内アンカー、重複ID、12実験の存在、CSSファイル量を確認します。完全なHTML/CSSバリデータやブラウザのE2Eテストではありません。PR時にはGitHub Actionsの `validate` ジョブでも実行されます。

## GitHub Pages / CI

GitHub Pages とRulesetsの初期設定は完了しています。

- **公開URL**: https://naoiw.github.io/css-native-lab/
- PagesのSource: **GitHub Actions**
- ワークフロー: `.github/workflows/site.yml`
- Pull Request: `validate` を実行し、デプロイはしない
- `main` へのpush: `validate` 成功後、自動的に `deploy` を実行
- サイトは `public/` の静的ファイルから公開。Node.js・npm・シークレットは不要

デプロイにリポジトリ変数や専用シークレットは不要です。`main` へのマージで自動公開されます。必要に応じて [Actions](https://github.com/naoiw/css-native-lab/actions/workflows/site.yml) から `Run workflow` で再実行できます。

## Rulesets

`main` には `Protect main` を設定済みです。PR必須（承認数0）、削除・force pushの制限、必須チェック `validate` を適用しています。

`deploy` はPRで実行されないため、必須チェックに追加しないでください。

## 設計方針

詳細は [docs/architecture.md](docs/architecture.md) を参照してください。CSSの実動作は `public/styles/experiments.css` に、サイト全体のデザインは `public/styles/site.css` に記述しています。

## License

[MIT](LICENSE)
