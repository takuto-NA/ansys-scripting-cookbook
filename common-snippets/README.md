# 💡 Common Snippets

本ディレクトリには、複数の Ansys 製品（Mechanical, SpaceClaim, Workbench）で共通して利用できる汎用スクリプトを格納しています。

## 📖 このセクションについて

このディレクトリには、複数の Ansys 製品で共通して使用できるユーティリティスクリプトを格納しています。これらは、個別のスクリプトから `import` して使用することで、コードの再利用性と保守性を向上させます。

主な用途：
- **ログ出力**: タイムスタンプ付きのログ出力機能
- **ファイル操作**: パス操作やファイル I/O の共通処理
- **エラーハンドリング**: 共通のエラー処理パターン

## スニペットの利用方法

Ansys 内部の IronPython 環境では、通常のリポジトリ構造のように相対パスで `import` することができません。
他のディレクトリにあるスニペットを読み込むには、スクリプトの冒頭で `sys.path` にディレクトリを追加する必要があります。

### インポートの定型句

```python
import sys
import os

# プロジェクトのルートディレクトリをパスに追加
# (実行環境によって適切に変更してください)
project_root = r"C:\path\to\ansys-scripting-cookbook"
if project_root not in sys.path:
    sys.path.append(project_root)

# ユーティリティのインポート
from common_snippets.logger import SimpleLogger

logger = SimpleLogger()
logger.info("Script started")
```

## コンテンツ一覧

- **[logger.py](./logger.py)**: コンソールおよびファイルへのログ出力ユーティリティ。

## 🔗 関連ドキュメント

- **[クイックスタートガイド](../docs/quickstart.md)**: 初めてのスクリプト実行
- **[スクリプトテンプレート](../docs/reference/script-template.md)**: スクリプトの書き方とコーディング規約
- **[トラブルシューティング](../docs/troubleshooting.md)**: よくあるエラーと解決方法

---

[← 戻る](../README.md)
