# 🔧 トラブルシューティングガイド

Ansys スクリプト実行時に発生するよくあるエラーとその解決方法をまとめています。

## ❌ よくあるエラーと解決方法

### エラー: `NameError: name 'DataModel' is not defined`

**エラーメッセージ例：**
```
NameError: name 'DataModel' is not defined
```
または
```
NameError: name 'Model' is not defined
```

**原因：**
- スクリプトを Ansys 製品外（VS Code のターミナル、通常の Python 環境など）で実行しようとしている
- `DataModel`、`Model`、`ExtAPI` などの変数は、Ansys 製品の内部環境でのみ自動的に定義されます
- これらの変数は、Ansys が起動時にスクリプト実行環境に注入するグローバル変数です

**解決方法：**

1. **Ansys 製品内で実行する**
   - Mechanical: **Automation** タブ → **Scripting** を開き、そこにコードを貼り付けて実行
   - SpaceClaim: **Design** タブ → **Script** を開き、そこにコードを貼り付けて実行
   - Workbench: **File** → **Scripting** → **Run Script File...** から `.wbjn` ファイルを選択

2. **実行環境を確認する**
   - VS Code から直接実行することはできません
   - Ansys 製品が起動していることを確認してください

3. **デバッグのヒント**
   - スクリプトの最初に `print(type(DataModel))` を追加して、変数が定義されているか確認できます
   - 定義されていない場合は、Ansys 製品内で実行していない可能性が高いです

**参考：** [環境構築ガイド - スクリプトの実行方法](./setup.md#4-スクリプトの実行方法-各製品)

---

### エラー: `UnicodeDecodeError` または日本語の文字化け

**エラーメッセージ例：**
```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe3 in position 10
```
または、コンソールに日本語が文字化けして表示される（例：`ããã` のような表示）

**原因：**
- スクリプトファイルのエンコーディング設定が不適切
- Ansys の IronPython 環境は、デフォルトで ASCII エンコーディングを想定している
- 日本語のコメントや文字列を含むスクリプトを実行する際に、エンコーディング宣言がないとエラーになる

**解決方法：**

1. **スクリプトの1行目にエンコーディング宣言を追加**
   ```python
   # -*- coding: utf-8 -*-
   ```
   または
   ```python
   # encoding: utf-8
   ```

2. **ファイルの保存形式を確認**
   - VS Code で保存する際は、**UTF-8** で保存してください
   - 画面右下のエンコーディング表示をクリックして、**Save with Encoding** → **UTF-8** を選択

3. **文字化けが発生する場合**
   - エンコーディング宣言を追加しても文字化けする場合は、ファイルを UTF-8 で再保存してください
   - 日本語を含むパスを使用する場合は、可能な限り英数字のみのパスに変更することを推奨します

**参考：** [技術的な落とし穴 - 日本語パスとエンコーディング](./reference/pitfalls.md#1-日本語パスとエンコーディング)

---

### エラー: `AttributeError: 'Body' object has no attribute 'Volume'`

**エラーメッセージ例：**
```
AttributeError: 'Body' object has no attribute 'Volume'
```

**原因：**
- ボディがまだメッシュ化されていない（`Volume` プロパティはメッシュ生成後に利用可能）
- ボディが無効な状態（ジオメトリエラーがある）
- ジオメトリが正しくインポートされていない

**解決方法：**

1. **ジオメトリの状態を確認**
   - Mechanical のツリービューで、ボディに警告やエラーアイコンが表示されていないか確認
   - エラーがある場合は、SpaceClaim や DesignModeler でジオメトリを修正してください

2. **メッシュを生成してから実行**
   ```python
   # メッシュを生成
   Model.Mesh.GenerateMesh()
   
   # その後、Volume にアクセス
   volume = body.Volume
   ```

3. **エラーハンドリングを追加**
   ```python
   # エラーハンドリングを追加
   try:
       volume = body.Volume
       print("Volume: {}".format(volume))
   except AttributeError:
       print("Volume is not available. Please generate mesh first.")
   except Exception as e:
       print("Could not retrieve volume: {}".format(e))
   ```

4. **ボディの有効性を確認**
   ```python
   # ボディが有効か確認
   if body.State == Ansys.ACT.Automation.Mechanical.GeometryBodyState.FullyDefined:
       # 処理を実行
       pass
   ```

---

### エラー: `KeyError` または材料が見つからない

**エラーメッセージ例：**
```
KeyError: 'Structural Steel'
```
または
```
Material 'Structural Steel' not found
```

**原因：**
- スクリプトで指定した材料名が、Engineering Data に存在しない
- 材料名の大文字小文字が一致していない（例：`Structural Steel` vs `structural steel`）
- 材料が Engineering Data に追加されていない
- 材料が正しいシステムに割り当てられていない

**解決方法：**

1. **利用可能な材料を確認**
   ```python
   # 利用可能な材料一覧を取得
   available_materials = [mat.Name for mat in Model.Materials.Children]
   print("Available materials: {}".format(available_materials))
   ```

2. **材料名を正確に一致させる**
   - Workbench の **Engineering Data** を開き、材料名を確認
   - スクリプト内の材料名を、Engineering Data に表示されている名前と**完全に一致**させる（大文字小文字も含む）
   - スペースや特殊文字も正確に一致させる必要があります

3. **材料が追加されているか確認**
   - Workbench のプロジェクトツリーで **Engineering Data** コンポーネントを開く
   - 材料が一覧に表示されているか確認
   - 表示されていない場合は、材料を追加してください

4. **安全な材料割り当て**
   ```python
   # 材料名を確認してから割り当て
   available_materials = [mat.Name for mat in Model.Materials.Children]
   target_material = "Structural Steel"
   
   if target_material in available_materials:
       body.Material = target_material
       print("Material '{}' assigned successfully.".format(target_material))
   else:
       print("Material '{}' not found!".format(target_material))
       print("Available materials: {}".format(available_materials))
   ```

**参考：** [`mechanical/batch_assign_materials.py`](../mechanical/batch_assign_materials.py)

---

### エラー: スクリプトの実行が非常に遅い

**症状：**
- スクリプトの実行に数分以上かかる
- 大規模なモデル（数百以上のボディ）で特に遅い
- メモリ使用量が異常に高い

**原因：**
- `GetObjectsByType` をループ内で繰り返し呼び出している（最も一般的な原因）
- 大規模なアセンブリに対して非効率な処理を行っている
- 不要なオブジェクトを大量に取得している

**解決方法：**

1. **`GetObjectsByType` の結果を変数に格納して使い回す**
   ```python
   # 悪い例：ループ内で毎回呼び出す（非効率）
   for i in range(100):
       bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
       # 処理
   ```
   
   ```python
   # 良い例：一度だけ取得して使い回す
   all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
   for body in all_bodies:
       # 処理
   ```

2. **必要な範囲だけを処理する**
   - 全ボディを取得するのではなく、特定の条件に合うボディだけを取得する
   ```python
   # 名前でフィルタリングしてから処理
   all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
   target_bodies = [b for b in all_bodies if "PART" in b.Name]
   ```

3. **進捗表示を追加してボトルネックを特定**
   ```python
   all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
   total = len(all_bodies)
   for i, body in enumerate(all_bodies):
       if i % 10 == 0:
           print("Processing {}/{}...".format(i+1, total))
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

