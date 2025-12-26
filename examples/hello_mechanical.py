# -*- coding: utf-8 -*-
"""
Example: Hello Mechanical
Tested on: Ansys 2023 R2 (Mechanical)

Description:
Mechanical スクリプトの最も基本的なサンプルです。
ツリー内のジオメトリ情報を取得し、ログに出力します。
"""

import sys

def hello_mechanical():
    print("--- Mechanical Script: Hello World ---")
    
    # Model (モデル) 階層へのアクセス
    geometry = Model.Geometry
    
    # 全ボディの取得
    # DataModel.GetObjectsByType は特定の型を持つオブジェクトを抽出する強力なメソッドです
    all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
    
    print("Total number of bodies: {}".format(len(all_bodies)))
    
    for i, body in enumerate(all_bodies):
        # Name プロパティでオブジェクト名を取得
        print("[{}] Body Name: {}".format(i+1, body.Name))
        
        # 物理量の取得 (例: 体積)
        # 単位系に注意が必要ですが、まずは数値として取得する例です
        try:
            volume = body.Volume
            print("    Volume: {}".format(volume))
        except:
            print("    Volume: (Could not retrieve)")

    print("---------------------------------------")

if __name__ == "__main__":
    hello_mechanical()

