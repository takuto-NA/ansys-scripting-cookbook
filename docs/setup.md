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

Ansys 独自の API を補完するために、以下のいずれかのスタブファイルを入手してください。

- **[ansys-stubs (GitHub)](https://github.com/ansys/ansys-stubs)**: 多くの製品（Mechanical, SpaceClaim, DesignModeler等）の API をカバーしています。
- **PyAnsys プロジェクト**: 最新の Python API (PyMechanical 等) を使用する場合は、`pip install` で入手可能ですが、本リポジトリのような内部スクリプト開発には上記のスタブが適しています。

ダウンロードした `ansys-stubs` フォルダ（または特定の製品フォルダ）をプロジェクト内に配置するか、任意の場所に保存します。

### ステップ 2: settings.json の編集

プロジェクトのルートにある `.vscode/settings.json` に以下の設定を追加します。

```json
{
    "python.analysis.extraPaths": [
        "./stubs/mechanical",
        "./stubs/spaceclaim"
    ]
}
```

これにより、スクリプト内で `import` していなくても、`Model` や `DataModel` といったグローバル変数の型推論が効くようになります。

## 4. スクリプトの実行方法 (各製品)

スクリプトを実際に動作させる場所は以下の通りです。

### Ansys Mechanical
1.  **自動化 (Automation)** タブをクリック。
2.  **スクリプト (Scripting)** をクリックして、スクリプトウィンドウを表示します。
3.  エディタにコードを貼り付け、**実行 (Run)** ボタンをクリックします。

### Ansys SpaceClaim (Discovery)
1.  **デザイン (Design)** タブにある **スクリプト (Script)** ボタンをクリック。
2.  右側に開くスクリプトエディタにコードを貼り付け、再生ボタン（実行）をクリックします。

### Ansys Workbench
1.  **ファイル (File)** -> **ジャーナルのスクリプト実行 (Scripting -> Run Script File...)** を選択。
2.  `.wbjn` ファイルを選択して実行します。

## 5. デバッグのコツ

Ansys 内部スクリプトは VS Code から直接デバッグ実行（F5）はできません。

1.  **Mechanical/SpaceClaim 内で実行**: スクリプトをコピペして Ansys のコンソールに貼り付けます。
2.  **ログ出力**: `print` 文や、本リポジトリの `common-snippets/logger.py` を活用して実行時の値を確認してください。

詳細なデバッグ方法は **[デバッグガイド](./reference/debugging.md)** を参照してください。

---

## 📚 次のステップ

- **[API 概要ガイド](./reference/api-overview.md)**: API の全体像を把握
- **[スクリプトテンプレート](./reference/script-template.md)**: スクリプトの書き方を学ぶ
- **[チートシート](./cheatsheet.md)**: よく使うコードを探す

---

[← 戻る](../README.md)

