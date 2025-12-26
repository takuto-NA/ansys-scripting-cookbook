# 🦏 Rhino から解析実行までの一貫自動化 (色ベースの属性付与)

Rhino で付けた色が、自動的に「メッシュ細密化」や「荷重条件」として Mechanical に伝わり、解析が実行されるまでのワークフローを解説します。

## 1. 運用ルール (Color Mapping)

このワークフローでは、以下の色と解析条件を紐付けます。

| Rhino での色 | RGB 値 | Mechanical での役割 |
| :--- | :--- | :--- |
| **赤 (Red)** | 255, 0, 0 | **メッシュ細密化**: 0.5mm の Sizing を適用 |
| **青 (Blue)** | 0, 0, 255 | **荷重条件**: 1000N の圧力を印加 |

## 2. 工程詳細

### ステップ 1: Rhino での作業
1.  メッシュを細かくしたい面に **赤** を設定。
2.  荷重をかけたい面に **青** を設定。
3.  STEP ファイルとして保存。

### ステップ 2: Workbench の設定
1.  Geometry コンポーネントのプロパティで `Named Selections: Yes`, `Named Selection Key: Color` を設定。

### ステップ 3: Mechanical での自動処理スクリプト

```python
# Mechanical Script: Color-based Mesh & Load Assignment
import os

def run_analysis_pipeline():
    analysis = Model.Analyses[0]
    all_ns = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.NamedSelection)
    
    # --- 1. 赤色の面を探してメッシュ制御 ---
    red_ns = [ns for ns in all_ns if "255.0.0" in ns.Name]
    if red_ns:
        sizing = Model.Mesh.AddSizing()
        sizing.Location = red_ns[0]
        sizing.ElementSize = Quantity("0.5 [mm]")
        print("Applied mesh sizing to Red faces.")

    # --- 2. 青色の面を探して荷重設定 ---
    blue_ns = [ns for ns in all_ns if "0.0.255" in ns.Name]
    if blue_ns:
        force = analysis.AddForce()
        force.Location = blue_ns[0]
        force.Magnitude.Output.SetData("1000 [N]")
        print("Applied force to Blue faces.")

    # --- 3. メッシュ生成と解析実行 ---
    print("Generating mesh...")
    Model.Mesh.GenerateMesh()
    
    print("Solving analysis...")
    analysis.Solve(True)
    print("Analysis completed successfully.")

if __name__ == "__main__":
    run_analysis_pipeline()
```

## 3. 自動化のメリット
- **デザインの反復が容易**: Rhino で形状を微調整して再出力するだけで、メッシュや荷重の再設定なしに解析結果を得られます。
- **ヒューマンエラーの削減**: 毎回手動で面を選択する必要がないため、設定漏れを防げます。

---
[← 戻る](./README.md)

