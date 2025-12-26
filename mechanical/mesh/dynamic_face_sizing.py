# -*- coding: utf-8 -*-
"""
Mechanical Script: Dynamic Face Sizing by Area
Tested on: Ansys 2023 R2 (Mechanical)

Description:
このスクリプトは、モデル内の「面（Face）」を面積（Area）に基づいて自動的に分類し、
それぞれのグループに対して異なるメッシュサイズ（Sizing）を適用します。
微小な面に細密メッシュを自動で割り当てる際などに便利です。
"""

def apply_dynamic_sizing_by_area(threshold_area, small_mesh_size, large_mesh_size):
    """
    面積に基づいて面を分類し、メッシュサイズを設定する。
    """
    # 全てのボディから全ての面を取得
    all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
    
    small_faces = []
    large_faces = []
    
    for body in all_bodies:
        # ボディのジオメトリエンティティから面を取得
        geo_body = body.GetGeoEntity()
        for face in geo_body.Faces:
            if face.Area < threshold_area:
                small_faces.append(face.Id)
            else:
                large_faces.append(face.Id)
    
    # --- 1. 小さい面への設定 ---
    if small_faces:
        ns_small = Model.AddNamedSelection()
        ns_small.Name = "NS_SmallFaces_Auto"
        
        selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
        selection.Ids = small_faces
        ns_small.Location = selection
        
        sizing_small = Model.Mesh.AddSizing()
        sizing_small.Name = "Sizing_SmallFaces"
        sizing_small.Location = ns_small
        sizing_small.ElementSize = Quantity("{} [mm]".format(small_mesh_size))
        print("Applied {}mm mesh to {} small faces.".format(small_mesh_size, len(small_faces)))

    # --- 2. 大きい面への設定 ---
    if large_faces:
        ns_large = Model.AddNamedSelection()
        ns_large.Name = "NS_LargeFaces_Auto"
        
        selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
        selection.Ids = large_faces
        ns_large.Location = selection
        
        sizing_large = Model.Mesh.AddSizing()
        sizing_large.Name = "Sizing_LargeFaces"
        sizing_large.Location = ns_large
        sizing_large.ElementSize = Quantity("{} [mm]".format(large_mesh_size))
        print("Applied {}mm mesh to {} large faces.".format(large_mesh_size, len(large_faces)))

    # メッシュ生成
    # Model.Mesh.GenerateMesh()

if __name__ == "__main__":
    # 閾値 100 mm^2 以下を「小さい面」として 1mm メッシュ、それ以外を 10mm メッシュにする例
    apply_dynamic_sizing_by_area(100.0, 1.0, 10.0)

