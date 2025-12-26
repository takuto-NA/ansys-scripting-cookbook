# 💡 Common Snippets

本ディレクトリには、複数の Ansys 製品（Mechanical, SpaceClaim, Workbench）で共通して利用できる汎用スクリプトを格納しています。

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

- **[logger.py](https://github.com/your-org/ansys-scripting-cookbook/blob/main/common-snippets/logger.py)**: コンソールおよびファイルへのログ出力ユーティリティ。

