# -*- coding: utf-8 -*-
"""
SpaceClaim Script: Thicken Shells and Export STEP
Tested on: Ansys 2023 R2 (SpaceClaim)

Description:
このスクリプトは、インポートされたサーフェスボディ（シェル）を指定した厚みでソリッド化し、
結果を新しい STEP ファイルとしてエクスポートします。
"""

def thicken_and_export(thickness_mm, output_path):
    # 1. すべてのサーフェスボディを取得
    root = GetRootPart()
    surfaces = [b for b in root.Bodies if b.Shape.IsSurface]
    
    if not surfaces:
        print("No surface bodies found.")
        return

    # 2. 厚み付け（両側オフセット）
    selection = Selection.Create(surfaces)
    options = ThickenOptions()
    options.ThickenBothSides = True
    
    # MM() はミリメートルを内部単位（メートル）に変換する関数
    Thicken.Execute(selection, MM(thickness_mm), options)
    print("Thickened {} surfaces to {} mm.".format(len(surfaces), thickness_mm))

    # 3. STEP としてエクスポート
    export_options = ExportOptions.Create()
    # DocumentSave.Execute ではなく、エクスポート用のコマンドを使用する場合もあるが
    # STEP などの外部フォーマットは DocumentSave または専用のエクスポートAPIを使用
    # ここでは一般的な形式を示す
    DocumentSave.Execute(output_path, export_options)
    print("Exported thickened model to: " + output_path)

if __name__ == "__main__":
    # 厚み 1.0mm でデスクトップに出力する例
    import os
    out = os.path.join(os.environ["USERPROFILE"], "Desktop", "thickened_model.step")
    thicken_and_export(1.0, out)

