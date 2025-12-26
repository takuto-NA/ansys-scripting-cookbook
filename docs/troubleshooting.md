# 🔧 トラブルシューティングガイド

Ansys スクリプト実行時に発生するよくあるエラーとその解決方法をまとめています。

## ❌ よくあるエラーと解決方法

### エラー: `NameError: name 'DataModel' is not defined`

**原因：**
スクリプトを Ansys 製品外（VS Code のターミナルなど）で実行しようとしている。

**解決方法：**
- スクリプトは必ず **Ansys 製品内のスクリプトウィンドウ**で実行してください
  - Mechanical: **Automation** タブ → **Scripting**
  - SpaceClaim: **Design** タブ → **Script**
  - Workbench: **File** → **Scripting** → **Run Script File...**

**参考：** [環境構築ガイド - スクリプトの実行方法](./setup.md#4-スクリプトの実行方法-各製品)

---

### エラー: `UnicodeDecodeError` または日本語の文字化け

**原因：**
スクリプトファイルのエンコーディング設定が不適切。

**解決方法：**
1. スクリプトの1行目に以下を追加：
   ```python
   # -*- coding: utf-8 -*-
   ```
2. VS Code で保存する際は、**UTF-8 (BOM付き)** で保存することを推奨

**参考：** [技術的な落とし穴 - 日本語パスとエンコーディング](./reference/pitfalls.md#1-日本語パスとエンコーディング)

---

### エラー: `AttributeError: 'Body' object has no attribute 'Volume'`

**原因：**
- ボディがまだメッシュ化されていない
- ボディが無効な状態（エラーがある）

**解決方法：**
1. ジオメトリが正しくインポートされているか確認
2. SpaceClaim や DesignModeler でジオメトリのエラーを修正
3. メッシュを生成してから実行（必要に応じて）

**例：**
```python
# エラーハンドリングを追加
try:
    volume = body.Volume
    print("Volume: {}".format(volume))
except Exception as e:
    print("Could not retrieve volume: {}".format(e))
```

---

### エラー: `KeyError` または材料が見つからない

**原因：**
スクリプトで指定した材料名が、Engineering Data に存在しない。

**解決方法：**
1. Workbench の **Engineering Data** を開き、材料名を確認
2. スクリプト内の材料名を正確に一致させる（大文字小文字も含む）
3. 材料が正しく追加されているか確認

**例：**
```python
# 材料名を確認してから割り当て
available_materials = [mat.Name for mat in Model.Materials.Children]
print("Available materials: {}".format(available_materials))

if "Structural Steel" in available_materials:
    body.Material = "Structural Steel"
else:
    print("Material 'Structural Steel' not found!")
```

**参考：** [`mechanical/batch_assign_materials.py`](../mechanical/batch_assign_materials.py)

---

### エラー: スクリプトの実行が非常に遅い

**原因：**
- `GetObjectsByType` をループ内で繰り返し呼び出している
- 大規模なアセンブリに対して非効率な処理を行っている

**解決方法：**
1. `GetObjectsByType` の結果を変数に格納して使い回す
2. 必要な範囲だけを処理するように絞り込む

**悪い例：**
```python
# ループ内で毎回呼び出す（非効率）
for i in range(100):
    bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
```

**良い例：**
```python
# 一度だけ取得して使い回す
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
for body in all_bodies:
    # 処理
```

**参考：** [技術的な落とし穴 - GetObjectsByType のパフォーマンス](./reference/pitfalls.md#3-datamodelgetobjectsbytype-のパフォーマンス)

---

### エラー: `ImportError: No module named 'common_snippets'`

**原因：**
`common-snippets` ディレクトリが `sys.path` に追加されていない。

**解決方法：**
スクリプトの冒頭で `sys.path` にプロジェクトのルートディレクトリを追加：

```python
import sys
import os

# プロジェクトのルートディレクトリをパスに追加
project_root = r"C:\path\to\ansys-scripting-cookbook"
if project_root not in sys.path:
    sys.path.append(project_root)

from common_snippets.logger import SimpleLogger
```

**参考：** [`common-snippets/README.md`](../common-snippets/README.md)

---

### エラー: 単位系が期待と異なる

**原因：**
Ansys の内部単位系と GUI の表示単位系が異なる場合がある。

**解決方法：**
`Quantity` クラスを使用して明示的に単位を指定：

```python
# 単位を指定して値を設定
force.Magnitude.Output.SetData("100 [N]")
```

**参考：** [技術的な落とし穴 - 単位系の罠](./reference/pitfalls.md#2-単位系の罠)

---

### エラー: STEP ファイルのインポートに失敗する

**原因：**
- ファイルパスに日本語が含まれている
- ファイルが破損している
- アセンブリ内に同名のパーツが存在する

**解決方法：**
1. ファイルパスに日本語が含まれている場合は、英数字のみのパスに変更
2. SpaceClaim で一度開いて保存し直す
3. パーツ名の重複を確認

**参考：** [CAD 互換性ガイド - STEP インポートの注意点](./reference/cad-compatibility.md#5-step-インポートの注意点と詳細-2024-r2)

---

### エラー: Named Selection が作成されない

**原因：**
- 選択したオブジェクトが無効
- スクリプトの実行タイミングが早すぎる（ジオメトリがまだ読み込まれていない）

**解決方法：**
1. ジオメトリが完全に読み込まれた後に実行する
2. オブジェクトの存在を確認してから処理する

**例：**
```python
# ボディの存在を確認
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
if len(all_bodies) == 0:
    print("No bodies found. Please import geometry first.")
else:
    # Named Selection を作成
    ns = Model.NamedSelections.AddNamedSelection()
    ns.Location = selected_bodies
```

---

## 🆘 それでも解決しない場合

1. **デバッグガイドを参照**
   - **[デバッグガイド](./reference/debugging.md)** で詳細な調査方法を確認

2. **エラーメッセージを確認**
   - コンソールに表示されたエラーメッセージをよく読む
   - エラーが発生した行番号を確認

3. **ログを確認**
   - `print()` 文を追加して、実行の流れを確認
   - [`common-snippets/logger.py`](../common-snippets/logger.py) を使用してファイルにログを出力

4. **シンプルなテストスクリプトで確認**
   - 複雑なスクリプトではなく、最小限のコードで動作確認
   - [`examples/hello_mechanical.py`](../examples/hello_mechanical.py) を参考にする

5. **Ansys のバージョンを確認**
   - スクリプトの冒頭に記載された動作確認バージョンと一致しているか確認
   - 異なるバージョンでは API が変更されている可能性がある

6. **Issue を報告**
   - GitHub の Issue で問題を報告してください
   - エラーメッセージ、Ansys のバージョン、実行環境などの情報を含めてください

---

[← 戻る](../README.md) | [クイックスタートガイド →](./quickstart.md)

