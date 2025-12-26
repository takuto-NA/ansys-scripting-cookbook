# 🔍 逆引きチートシート

「〇〇したい」から必要なコードを探せる逆引きリファレンスです。

---

## 📌 使い方

1. 目的のセクションを探す
2. コードスニペットをコピー
3. Ansys のスクリプトウィンドウに貼り付けて実行

---

## 🧊 Mechanical 編

### ジオメトリ・オブジェクト取得

#### 全ボディを取得したい

```python
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
print("Body count: {}".format(len(all_bodies)))
```

#### 名前でオブジェクトを検索したい

```python
# 完全一致
obj = DataModel.GetObjectsByName("MyObject")[0]

# 部分一致（キーワード検索）
all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
matched = [b for b in all_bodies if "BOLT" in b.Name.upper()]
```

#### 特定の型のオブジェクトを全て取得したい

```python
# Named Selection を全て取得
all_ns = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.NamedSelection)

# 荷重を全て取得
all_forces = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Force)

# 結果オブジェクトを全て取得
all_results = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Results.Result)
```

---

### Named Selection（名前付き選択）

#### Named Selection を新規作成したい

```python
ns = Model.AddNamedSelection()
ns.Name = "NS_MySelection"
```

#### Named Selection にボディを割り当てたい

```python
target_bodies = [b for b in all_bodies if "PART" in b.Name]
ids = [b.GetGeoEntity().Id for b in target_bodies]

selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = ids
ns.Location = selection
```

#### 既存の Named Selection を取得したい

```python
ns = DataModel.GetObjectsByName("NS_FixedFaces")[0]
```

---

### 材料・プロパティ

#### ボディに材料を割り当てたい

```python
body.Material = "Structural Steel"
```

#### 利用可能な材料一覧を取得したい

```python
materials = [mat.Name for mat in Model.Materials.Children]
print("Available materials: {}".format(materials))
```

#### ボディの体積を取得したい

```python
try:
    volume = body.Volume
    print("Volume: {}".format(volume))
except:
    print("Could not retrieve volume")
```

---

### 境界条件

#### 荷重を追加したい

```python
analysis = Model.Analyses[0]  # 最初の解析システム
force = analysis.AddForce()
force.Location = ns  # Named Selection を指定
force.Magnitude.Output.SetData("1000 [N]")
```

#### 固定拘束を追加したい

```python
fixed = analysis.AddFixedSupport()
fixed.Location = ns
```

---

### 解析・結果

#### 解析を実行したい

```python
Model.Analyses[0].Solve(True)  # True = 結果を待つ
```

#### 結果（相当応力）を追加したい

```python
solution = Model.Analyses[0].Solution
stress = solution.AddEquivalentStress()
stress.EvaluateAllResults()
```

#### 最大応力値を取得したい

```python
stress_results = DataModel.GetObjectsByType(
    Ansys.ACT.Automation.Mechanical.Results.EquivalentStress
)
if stress_results:
    max_stress = stress_results[0].Maximum
    print("Max Stress: {}".format(max_stress))
```

---

### ファイル入出力

#### 結果をテキストファイルに出力したい

```python
import os
output_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "result.txt")

with open(output_path, "w") as f:
    f.write("Max Stress: {}\n".format(max_stress))
print("Exported to: {}".format(output_path))
```

#### 結果を CSV に出力したい

```python
with open(output_path, "w") as f:
    f.write("Body Name,Material\n")
    for body in all_bodies:
        f.write("{},{}\n".format(body.Name, body.Material))
```

#### モデルを CDB (MAPDL) 形式でエクスポートしたい

```python
analysis = Model.Analyses[0]
analysis.ExportMechanicalData(r"C:\temp\model.cdb")
```

---

## ✏️ SpaceClaim 編

### ジオメトリ取得

#### 全ボディを取得したい

```python
root = GetRootPart()
all_bodies = root.Bodies
print("Body count: {}".format(len(all_bodies)))
```

#### 全ての面を取得したい

```python
all_faces = GetRootPart().GetAllFaces()
```

#### 特定の色の面を抽出したい

```python
target_faces = []
for face in all_faces:
    color = face.Color
    if color.R == 255 and color.G == 0 and color.B == 0:  # 赤
        target_faces.append(face)
```

---

### Named Selection (Groups)

#### Named Selection を作成したい

```python
selection = Selection.Create(target_faces)
NamedSelection.Create(selection, "NS_LoadFaces")
```

---

### ジオメトリ操作

#### ファイルをインポートしたい

```python
options = ImportOptions.Create()
DocumentInsert.Execute(r"C:\path\to\file.step", options)
```

#### ドキュメントを保存したい

```python
options = ExportOptions.Create()
DocumentSave.Execute(r"C:\path\to\output.scdocx", options)
```

#### サーフェス（シェル）を厚み付けしてソリッド化したい

```python
# 全サーフェスを選択
surfaces = [b for b in GetRootPart().Bodies if b.Shape.IsSurface]
selection = Selection.Create(surfaces)

# 厚み付けオプション
options = ThickenOptions()
options.ThickenBothSides = True # 両側にオフセット

# 2.0 mm の厚み付けを実行
Thicken.Execute(selection, MM(2.0), options)
```

---

## ⚙️ Workbench Journal 編

### プロジェクト操作

#### プロジェクトを保存したい

```python
Save()

# 別名で保存
Save(FilePath=r"C:\output\project.wbpj", Overwrite=True)
```

#### プロジェクトをアーカイブしたい

```python
Archive(
    FilePath=r"C:\output\project_backup.wbpz",
    IncludeExternalFiles=True,
    IncludeSimulationResults=True
)
```

---

### パラメータ操作

#### パラメータ値を変更したい

```python
param_set = GetProject().GetParameterSet()
param = param_set.GetParameter(Name="P1")
param.Expression = "100 [mm]"
```

#### 全デザインポイントを更新したい

```python
UpdateAllDesignPoints()
```

---

### システム操作

#### システムを取得したい

```python
system = GetSystem(Name="SYS")
```

#### Mechanical を開きたい

```python
model_component = system.GetComponent(Name="Model")
model_component.Edit()
```

---

## 🔧 共通・ユーティリティ

### ログ出力

#### タイムスタンプ付きログを出力したい

```python
import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("[{}] {}".format(timestamp, message))

log("Processing started")
```

### エラーハンドリング

#### 安全に処理を実行したい

```python
try:
    result = risky_operation()
except Exception as e:
    print("Error: {}".format(e))
```

### パス操作

#### デスクトップのパスを取得したい

```python
import os
desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
```

#### ファイルの存在を確認したい

```python
import os
if os.path.exists(file_path):
    print("File exists")
else:
    print("File not found")
```

---

## 📚 関連ドキュメント

- **[API 概要ガイド](./reference/api-overview.md)**: オブジェクト階層の詳細
- **[スクリプトテンプレート](./reference/script-template.md)**: スクリプトの書き方
- **[デバッグガイド](./reference/debugging.md)**: エラー調査の方法
- **[トラブルシューティング](./troubleshooting.md)**: よくあるエラーと解決策

---

[← 戻る](./README.md)

