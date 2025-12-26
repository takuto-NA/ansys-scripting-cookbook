# 📝 スクリプトテンプレート & コーディング規約

新しいスクリプトを作成する際のテンプレートと、一貫性のあるコードを書くためのガイドラインです。

---

## 🎯 このガイドの目的

- 新規スクリプト作成時の「お作法」を理解する
- チーム内で一貫したコードスタイルを維持する
- メンテナンスしやすいスクリプトを書く

---

## 1. Mechanical スクリプトのテンプレート

```python
# -*- coding: utf-8 -*-
"""
Mechanical Script: [スクリプトの名前]
Tested on: Ansys 20XX RX (Mechanical)

Description:
[このスクリプトが何をするかを1-2文で説明]

Prerequisites:
- [前提条件1: 例) ジオメトリがインポートされていること]
- [前提条件2: 例) 'Structural Steel' が Engineering Data に存在すること]

Author: [作成者名]
Date: [作成日]
"""

# ============================================================
# Imports
# ============================================================
import sys
import os

# ============================================================
# Configuration (ユーザーが変更する設定値)
# ============================================================
# ここに設定値を集約することで、修正箇所が明確になります
OUTPUT_PATH = r"C:\Temp\output.txt"
TARGET_KEYWORD = "BOLT"

# ============================================================
# Main Functions
# ============================================================
def main():
    """
    メイン処理
    """
    print("--- Script Started ---")
    
    # 処理を記述
    all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
    print("Total bodies: {}".format(len(all_bodies)))
    
    for body in all_bodies:
        process_body(body)
    
    print("--- Script Completed ---")

def process_body(body):
    """
    個々のボディに対する処理
    
    Args:
        body: Ansys.ACT.Automation.Mechanical.Body オブジェクト
    """
    try:
        print("Processing: {}".format(body.Name))
        # 処理内容
    except Exception as e:
        print("Error processing {}: {}".format(body.Name, e))

# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    main()
```

---

## 2. SpaceClaim スクリプトのテンプレート

```python
# -*- coding: utf-8 -*-
"""
SpaceClaim Script: [スクリプトの名前]
Tested on: Ansys 20XX RX (SpaceClaim / Discovery)

Description:
[このスクリプトが何をするかを1-2文で説明]

Prerequisites:
- [前提条件: 例) ドキュメントが開かれていること]
"""

# ============================================================
# Configuration
# ============================================================
THRESHOLD_VALUE = 0.001  # [m]

# ============================================================
# Main Functions
# ============================================================
def main():
    """
    メイン処理
    """
    print("--- Script Started ---")
    
    root = GetRootPart()
    all_bodies = root.Bodies
    
    print("Total bodies: {}".format(len(all_bodies)))
    
    for body in all_bodies:
        process_body(body)
    
    print("--- Script Completed ---")

def process_body(body):
    """
    個々のボディに対する処理
    """
    try:
        print("Processing: {}".format(body.Name))
        # 処理内容
    except Exception as e:
        print("Error: {}".format(e))

# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    main()
```

---

## 3. Workbench Journal のテンプレート

```python
# encoding: utf-8
# Workbench Journal: [ジャーナルの名前]
# Tested on: Ansys 20XX RX

# Description:
# [このジャーナルが何をするかを1-2文で説明]

import os

# ============================================================
# Configuration
# ============================================================
OUTPUT_DIR = r"C:\Temp"

# ============================================================
# Main Functions
# ============================================================
def main():
    print("--- Journal Started ---")
    
    project = GetProject()
    
    # 処理を記述
    Save()
    
    print("--- Journal Completed ---")

# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    main()
```

---

## 4. コーディング規約

### 4.1 ヘッダーコメント（必須）

すべてのスクリプトの冒頭に以下を含めてください：

```python
# -*- coding: utf-8 -*-
"""
[製品名] Script: [スクリプト名]
Tested on: Ansys 20XX RX

Description:
[説明]

Prerequisites:
- [前提条件]
"""
```

### 4.2 IronPython 2.7 互換性

| ❌ 使用不可 | ✅ 使用可能 |
|:---|:---|
| `f"value: {x}"` | `"value: {}".format(x)` |
| `print "text"` (括弧なし) | `print("text")` |
| `async/await` | 非同期処理は使わない |
| `yield from` | 通常の `for` ループ |

### 4.3 命名規則

| 対象 | 規則 | 例 |
|:---|:---|:---|
| 変数・関数 | snake_case | `all_bodies`, `process_body()` |
| 定数 | UPPER_SNAKE_CASE | `OUTPUT_PATH`, `THRESHOLD` |
| クラス | PascalCase | `SimpleLogger` |
| Named Selection 名 | NS_ プレフィックス推奨 | `NS_FixedFaces`, `NS_LoadArea` |

### 4.4 設定値の集約

スクリプトの冒頭に `Configuration` セクションを設け、ユーザーが変更する可能性のある値を集約します：

```python
# ============================================================
# Configuration (ユーザーが変更する設定値)
# ============================================================
OUTPUT_PATH = r"C:\Temp\output.txt"
MATERIAL_NAME = "Structural Steel"
KEYWORD_LIST = ["BOLT", "NUT", "WASHER"]
```

### 4.5 エラーハンドリング

重要な処理には `try-except` を使用し、エラーをログに出力します：

```python
try:
    body.Material = "Structural Steel"
except Exception as e:
    print("Error: Could not assign material. {}".format(e))
```

### 4.6 ログ出力

- 処理の開始・終了を明示
- 重要なステップごとに進捗を出力
- エラー発生時は原因を出力

```python
print("--- Script Started ---")
print("Processing {} bodies...".format(len(all_bodies)))
print("[1/10] Processing Body_001...")
print("--- Script Completed ---")
```

### 4.7 コメント

- 複雑な処理には日本語（または英語）でコメントを付ける
- 「なぜ」その処理が必要かを説明する

```python
# ボディ名を大文字に変換して比較（大文字小文字を無視するため）
body_name_upper = body.Name.upper()
```

---

## 5. ファイル構成のベストプラクティス

### 5.1 1ファイル1機能

1つのスクリプトファイルは1つの機能に限定する。複数の機能を持たせると保守が困難になります。

### 5.2 再利用可能なコードの分離

汎用的な処理は `common-snippets/` に分離し、必要に応じてインポートする：

```python
import sys
sys.path.append(r"C:\path\to\ansys-scripting-cookbook")
from common_snippets.logger import SimpleLogger
```

### 5.3 ディレクトリ構成

```
mechanical/
├── geometry/
│   └── create_named_selection.py  # ジオメトリ操作
├── boundary-cond/
│   └── batch_assign_materials.py  # 境界条件設定
└── post-processing/
    └── simple_export.py           # 結果処理
```

---

## 6. チェックリスト（スクリプト公開前）

新しいスクリプトを作成したら、以下を確認してください：

- [ ] ヘッダーコメント（`Tested on`, `Description`, `Prerequisites`）がある
- [ ] `# -*- coding: utf-8 -*-` が1行目にある
- [ ] IronPython 2.7 互換（`f-string` を使っていない）
- [ ] 設定値が `Configuration` セクションに集約されている
- [ ] 重要な処理にエラーハンドリングがある
- [ ] 処理の開始・終了がログ出力される
- [ ] 実際の Ansys 環境で動作確認した

---

[← 戻る](../README.md) | [API 概要 →](./api-overview.md)

