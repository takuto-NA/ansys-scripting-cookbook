# 🐛 デバッグガイド

Ansys スクリプトの実行時に発生するエラーを調査・解決するための方法を解説します。

---

## 🎯 このガイドの目的

- エラーメッセージの読み方を理解する
- 効率的なデバッグ手法を身につける
- 問題の原因を素早く特定する

---

## 1. エラーメッセージの読み方

### 1.1 基本的な構造

Ansys のスクリプトコンソールに表示されるエラーは、通常以下の形式です：

```
Traceback (most recent call last):
  File "<string>", line 15, in <module>
  File "<string>", line 8, in main
AttributeError: 'NoneType' object has no attribute 'Name'
```

**読み方：**
1. **最後の行** = エラーの種類と内容（最も重要）
2. **`line XX`** = エラーが発生した行番号
3. **`in XXXX`** = エラーが発生した関数名

### 1.2 よくあるエラーの種類

| エラー種類 | 意味 | よくある原因 |
|:---|:---|:---|
| `NameError` | 変数が定義されていない | Ansys 外で実行した / スペルミス |
| `AttributeError` | オブジェクトに属性がない | オブジェクトが `None` / 型が違う |
| `TypeError` | 型が合わない | 引数の渡し方が間違っている |
| `IndexError` | インデックス範囲外 | リストが空 / 範囲外アクセス |
| `KeyError` | キーが存在しない | 辞書のキー名が間違っている |
| `ImportError` | モジュールがない | パスが通っていない |

---

## 2. デバッグの基本テクニック

### 2.1 print デバッグ

最も基本的で効果的な方法です。変数の値や処理の進捗を確認します。

```python
print("=== Debug Start ===")
print("all_bodies type: {}".format(type(all_bodies)))
print("all_bodies count: {}".format(len(all_bodies)))

for i, body in enumerate(all_bodies):
    print("[{}] body.Name = {}".format(i, body.Name))
    print("[{}] body.Material = {}".format(i, body.Material))

print("=== Debug End ===")
```

### 2.2 段階的な実行

問題のあるスクリプトを小さな部分に分割し、どこでエラーが発生するかを特定します：

```python
# Step 1: オブジェクト取得（ここは動く？）
print("Step 1: Getting bodies...")
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
print("Step 1: OK - {} bodies found".format(len(all_bodies)))

# Step 2: 最初のボディを処理（ここは動く？）
print("Step 2: Processing first body...")
if len(all_bodies) > 0:
    body = all_bodies[0]
    print("Body name: {}".format(body.Name))
    print("Step 2: OK")
else:
    print("Step 2: No bodies found!")

# Step 3: 材料割り当て（ここで失敗？）
print("Step 3: Assigning material...")
body.Material = "Structural Steel"
print("Step 3: OK")
```

### 2.3 型の確認

予期しない動作の原因は、多くの場合「型の不一致」です：

```python
print("Type of obj: {}".format(type(obj)))
print("obj is None: {}".format(obj is None))

# オブジェクトの属性一覧を確認
print("Available attributes: {}".format(dir(obj)))
```

### 2.4 try-except での詳細なエラー情報

```python
import traceback

try:
    risky_operation()
except Exception as e:
    print("Error: {}".format(e))
    print("Full traceback:")
    traceback.print_exc()
```

---

## 3. 問題別デバッグ手順

### 3.1 「オブジェクトが見つからない」場合

```python
# 検索結果を確認
results = DataModel.GetObjectsByName("NS_FixedFaces")
print("Search results: {}".format(results))
print("Result count: {}".format(len(results)))

# 全ての Named Selection を列挙
all_ns = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.NamedSelection)
print("All Named Selections:")
for ns in all_ns:
    print("  - '{}'".format(ns.Name))
```

**チェックポイント：**
- 名前が完全に一致しているか（大文字小文字、スペース）
- オブジェクトが作成済みか
- 正しい型で検索しているか

### 3.2 「属性がない」場合

```python
print("Object type: {}".format(type(body)))
print("Available attributes:")
for attr in dir(body):
    if not attr.startswith("_"):
        print("  - {}".format(attr))
```

**チェックポイント：**
- オブジェクトが `None` になっていないか
- 期待している型のオブジェクトか
- API のバージョン違いがないか

### 3.3 「処理が遅い」場合

```python
import datetime

def timed_operation(name, func):
    start = datetime.datetime.now()
    result = func()
    end = datetime.datetime.now()
    print("{}: {} elapsed".format(name, end - start))
    return result

# 使用例
bodies = timed_operation("GetObjectsByType", 
    lambda: DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body))
```

**よくある原因：**
- `GetObjectsByType` をループ内で繰り返し呼び出している
- 大量のオブジェクトを一つずつ処理している

### 3.4 「単位がおかしい」場合

```python
# 値と単位を確認
print("Raw value: {}".format(body.Volume))

# Quantity オブジェクトの場合
quantity = force.Magnitude.Output
print("Value: {}".format(quantity.Value))
print("Unit: {}".format(quantity.Unit))
```

---

## 4. ログファイルへの出力

コンソールだけでなく、ファイルにもログを残すと後から確認しやすくなります。

### 4.1 シンプルなログ出力

```python
import datetime
import os

LOG_PATH = os.path.join(os.environ["USERPROFILE"], "Desktop", "debug_log.txt")

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "[{}] {}\n".format(timestamp, message)
    print(line.strip())
    with open(LOG_PATH, "a") as f:
        f.write(line)

log("Script started")
log("Processing {} bodies".format(len(all_bodies)))
```

### 4.2 common-snippets/logger.py の活用

```python
import sys
sys.path.append(r"C:\path\to\ansys-scripting-cookbook")
from common_snippets.logger import SimpleLogger

logger = SimpleLogger(r"C:\Temp\debug.log")
logger.info("Script started")
logger.error("An error occurred")
```

---

## 5. Mechanical 固有のデバッグ

### 5.1 ツリー構造の確認

```python
def print_tree(obj, indent=0):
    """オブジェクトのツリー構造を表示"""
    print("{}[{}] {}".format("  " * indent, type(obj).__name__, obj.Name))
    if hasattr(obj, "Children"):
        for child in obj.Children:
            print_tree(child, indent + 1)

# 使用例
print_tree(Model.Geometry)
```

### 5.2 プロパティの一覧取得

```python
def inspect_object(obj):
    """オブジェクトのプロパティを表示"""
    print("=== Inspecting: {} ===".format(obj.Name))
    for attr in dir(obj):
        if not attr.startswith("_"):
            try:
                value = getattr(obj, attr)
                if not callable(value):
                    print("{}: {}".format(attr, value))
            except:
                pass

inspect_object(all_bodies[0])
```

---

## 6. SpaceClaim 固有のデバッグ

### 6.1 選択状態の確認

```python
# 現在の選択を確認
current_selection = GetActiveSelection()
print("Selected items: {}".format(current_selection.Count))

for item in current_selection:
    print("  - {} ({})".format(item.Name, type(item).__name__))
```

### 6.2 ジオメトリ情報の確認

```python
for body in GetRootPart().Bodies:
    print("Body: {}".format(body.Name))
    print("  Faces: {}".format(len(body.Faces)))
    print("  Edges: {}".format(len(body.Edges)))
    print("  Volume: {}".format(body.Volume))
```

---

## 7. デバッグチェックリスト

エラーが発生したら、以下を順番に確認してください：

1. **エラーメッセージを読む**
   - [ ] エラーの種類は？（NameError, AttributeError など）
   - [ ] 何行目で発生した？

2. **基本的な確認**
   - [ ] スクリプトは Ansys 製品内で実行している？
   - [ ] ジオメトリはインポート済み？
   - [ ] 必要な材料は Engineering Data に追加済み？

3. **変数の確認**
   - [ ] 変数が `None` になっていない？
   - [ ] 変数の型は期待通り？
   - [ ] リストが空になっていない？

4. **名前の確認**
   - [ ] オブジェクト名は完全一致している？（大文字小文字、スペース）
   - [ ] 材料名は Engineering Data と一致している？

5. **バージョンの確認**
   - [ ] スクリプトの動作確認バージョンと一致している？

---

## 📚 関連ドキュメント

- **[トラブルシューティング](../troubleshooting.md)**: よくあるエラーと解決策
- **[技術的な落とし穴](./pitfalls.md)**: IronPython の制限と回避策
- **[API 概要ガイド](./api-overview.md)**: オブジェクト階層の理解

---

[← 戻る](../README.md)

