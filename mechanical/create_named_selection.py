# -*- coding: utf-8 -*-
"""
Mechanical Script: Create Named Selections by Name
Tested on: Ansys 2023 R2 (Mechanical)

Description:
ボディの名前に含まれるキーワードを検索し、一致するボディを
Named Selection (名前付き選択) としてまとめます。
"""

def create_ns_by_keywords(mapping):
    """
    mapping: { "Keyword": "NS_Name" } のディクショナリ
    """
    # 全ボディを取得
    all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
    
    for keyword, ns_name in mapping.items():
        # キーワードに一致するボディを抽出
        target_bodies = [b for b in all_bodies if keyword.upper() in b.Name.upper()]
        
        if not target_bodies:
            print("No bodies found for keyword: {}".format(keyword))
            continue
            
        # Named Selection の作成
        ns = Model.AddNamedSelection()
        ns.Name = ns_name
        
        # 選択状態の設定 (Selection Manager を使用)
        # 内部 ID (GeoEntityId) のリストを作成
        ids = [b.GetGeoEntity().Id for b in target_bodies]
        
        # Location プロパティにセット
        selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
        selection.Ids = ids
        ns.Location = selection
        
        print("Created Named Selection: '{}' with {} bodies.".format(ns_name, len(target_bodies)))

if __name__ == "__main__":
    # 設定例: "BOLT" を含むボディを "NS_Bolts" に、"BRACKET" を含むものを "NS_Support" に
    target_mapping = {
        "BOLT": "NS_Bolts",
        "BRACKET": "NS_Support"
    }
    
    create_ns_by_keywords(target_mapping)

