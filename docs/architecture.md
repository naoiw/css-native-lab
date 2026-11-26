# Architecture

## 目的

`web-native-lab` がHTML標準要素を中心に実験するのに対し、`css-native-lab` はCSS固有のレイアウト・状態・配色・アニメーションを扱う独立プロジェクトです。

## 方針

- JavaScriptと外部パッケージを使用せず、HTML/CSS標準機能のみで動作させる
- CSSをメイン言語にするため、スタイルは実装別CSSファイルに集約
- HTMLは構造・アクセシビリティのために使用
- すべての実験にタイトル、デモ、短いコード例、MDNへのリンクを付ける
- 未対応機能は `@supports` とデフォルトスタイルを使って徐々に拡張
- `prefers-reduced-motion` を尊重する
- HTMLの `popover` やチェックボックスはCSS実験のトリガーとして使用し、独自JSによる状態管理はしない

## ファイル構成

```
public/
  index.html             12件の実験カタログ
  styles/site.css        サイト内のレイアウト・デザイン
  lab-chrome.css         姉妹サイト共通のヘッダー・フッターとコンテンツ幅
  styles/experiments.css 各実験の動作CSS
  favicon.svg
  robots.txt
  sitemap.xml
scripts/check_site.py   最小限の構造チェック
.github/workflows/site.yml
```

## 共通ヘッダー・フッター

`public/lab-chrome.css` は `naoiw/web-native-lab` と `naoiw/css-native-lab` で同一内容です。最大コンテンツ幅を1360pxに統一し、ヘッダー・フッターのフォント、文字サイズ、間隔、スマホ表示も一致させています。サイト名・ロゴ記号・アクセントカラー・MDNリンク先は各サイト固有です。共通デザインを変更する際は両方のCSSを更新してください。CSSファイルはそれぞれのリポジトリ内で配信し、相互のデプロイには依存しません。

## 互換性・制限

- CSSリサイズハンドルはブラウザと入力方式に依存し、スマホでは操作しにくい
- Anchor Positioningが未対応の場合、ポップアップは中央に表示する
- Scroll-driven Animationsが未対応の場合、進捗バーは固定のまま
- `@starting-style` 非対応なら通常のPopoverは開けるが、登場演出は限定される
- `@property` 非対応ならアニメーションの動きが異なる可能性がある
- Reduce Motion設定では装飾アニメーションを停止する
- CIは構造検証であり、各ブラウザの見た目や操作を保証しない

## Pages / CI

- GitHub Pages、Rulesetsの初期設定を完了
- 公開URL: https://naoiw.github.io/css-native-lab/
- PagesのSourceはGitHub Actions
- `validate`: mainへのpush、PR、手動実行時に構造チェックを実施
- `deploy`: PR以外で `main` のコミットが対象なら、`validate` 成功後に自動実行
- リポジトリ変数 `PAGES_ENABLED` は不要。必要に応じて `workflow_dispatch` で手動再実行
- デプロイ対象: `public/` のみ（ビルド不要）
- `main` のRuleset `Protect main` は削除・force pushを制限し、PR必須（承認数0）と必須チェック `validate` を指定
- `deploy` はPRでスキップされるためRequired status checkには指定しない
- GitHub Actionsで `deploy` がsuccessになることを公開確認の判定にする

## 実験追加ルール

1. カードに固有IDを割り当てる
2. CSS効果を実際に確認できるデモにする
3. 必要なブラウザ対応・操作条件を短く明記
4. 最小のCSS例とMDNリファレンスを追加する
5. `scripts/check_site.py` の期待実験IDも更新する
6. 外部ライブラリ導入が必要になった場合は別Issueで検討する
