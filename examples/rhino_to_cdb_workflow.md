# 🦏 Rhino から CDB 出力までのエンドツーエンド自動化

Rhino で作成したモデルに色を付け、それをトリガーにして Mechanical で自動メッシュ制御・CDB 出力を行う一連のワークフローを解説します。

## 1. ワークフロー概要

```mermaid
graph LR
    Rhino["Rhino (色付け)"] --> STEP["STEP エクスポート"]
    STEP --> WB["Workbench (色を NS に変換)"]
    WB --> Mech["Mechanical (自動メッシュ設定)"]
    Mech --> CDB["CDB エクスポート"]
```

## 2. 各工程の手順

### ステップ 1: Rhino での準備
1.  メッシュ密度を細かくしたい面を選択します。
2.  その面の **Display Color (表示色)** を「赤 (RGB: 255, 0, 0)」に設定します。
3.  `File > Export Selected` で **STEP** 形式で保存します。

### ステップ 2: Workbench の設定
STEP ファイルの色情報を Named Selection として読み込むための設定を行います。

1.  Workbench の **Geometry** コンポーネントを選択します。
2.  **Properties** パネル（または Details view）で以下を設定します。
    *   **Named Selections**: `Yes` (チェックを入れる)
    *   **Named Selection Key**: `Color`

### ステップ 3: Mechanical での自動処理
以下のスクリプトを実行することで、特定の色（赤）が付いた面を自動で探し、細密メッシュを適用して CDB を出力します。

```python
# Mechanical Script
import os

def run_automated_workflow():
    # 1. 赤色 (RGB: 255, 0, 0) に対応する名前付き選択を検索
    # Workbench の設定により "Color:255.0.0" のような名前でインポートされます
    all_ns = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.NamedSelection)
    target_ns = [ns for ns in all_ns if "255.0.0" in ns.Name]
    
    if not target_ns:
        print("指定された色の面が見つかりませんでした。")
        return
    
    ns = target_ns[0]
    print("Found Named Selection: " + ns.Name)

    # 2. メッシュサイズの設定 (0.5mm)
    sizing = Model.Mesh.AddSizing()
    sizing.Location = ns
    sizing.ElementSize = Quantity("0.5 [mm]")
    sizing.Name = "Sizing_From_Rhino_Color"

    # 3. メッシュ生成
    Model.Mesh.GenerateMesh()

    # 4. CDB エクスポート
    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    export_path = os.path.join(desktop, "output_from_rhino.cdb")
    
    analysis = Model.Analyses[0]
    analysis.ExportMechanicalData(export_path)
    print("CDB exported to: " + export_path)

run_automated_workflow()
```

## 3. この手法のメリット

- **GUI 操作の排除**: CAD 側で色を付けるだけで、Mechanical 側でのクリック操作なしに特定の部位を制御できます。
- **再現性**: モデルの形状が変更されても、色が同じであればスクリプトはそのまま動作します。
- **標準化**: 「赤はメッシュ細密化」「青は固定拘束」のようにチーム内でルール化することで、解析作業の自動化が進みます。

---
[← 戻る](./README.md)

