# 🛠️ VS Code 環境構築ガイド

Ansysのスクリプト開発を効率化するために、VS Code で入力補完（IntelliSense）を効かせる設定方法を解説します。

## 1. 必要な拡張機能のインストール

VS Code で以下の拡張機能をインストールしてください。

- **Python** (Microsoft)

## 2. IronPython (Python 2.7) の考慮

Ansys の内部スクリプトは **IronPython 2.7** で動作します。
最新の Python (3.x) とは文法が一部異なるため、VS Code の Linter がエラーを出すことがありますが、動作には影響ありません。

- ❌ `f-string` は使用できません。
- ❌ `yield` や一部の標準ライブラリの挙動が異なります。

## 3. IntelliSense (入力補完) の設定

Ansys 独自の API（`DataModel`, `Model`, `Tree` など）は外部の Python 環境からは参照できません。これらを補完対象にするには、**Stub (スタブ) ファイル** を用意し、VS Code にそのパスを教える必要があります。

### ステップ 1: Stub ファイルの入手

[Ansys-stubs](https://github.com/ansys/pyansys-geometry) (またはプロジェクトに適したスタブ提供元) から、利用したい製品のスタブファイルをダウンロードします。
※ 一般的には、Mechanical や SpaceClaim の API を模した `.py` ファイル群です。

### ステップ 2: settings.json の編集

プロジェクトのルートにある `.vscode/settings.json` に以下の設定を追加します。

```json
{
    "python.analysis.extraPaths": [
        "./path/to/ansys-stubs"
    ]
}
```

これにより、スクリプト内で `import` していなくても、グローバル変数の型推論が効くようになります。

## 4. デバッグのコツ

Ansys 内部スクリプトは VS Code から直接デバッグ実行（F5）はできません。

1.  **Mechanical/SpaceClaim 内で実行**: スクリプトをコピペして Ansys のコンソールに貼り付けます。
2.  **ログ出力**: `print` 文や、本リポジトリの `common-snippets/logger.py` を活用して実行時の値を確認してください。

---

[← 戻る](../README.md)

