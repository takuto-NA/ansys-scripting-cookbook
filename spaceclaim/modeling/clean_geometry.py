# -*- coding: utf-8 -*-
"""
SpaceClaim Script: Clean Small Faces and Edges
Tested on: Ansys 2023 R2 (SpaceClaim)

Description:
This script identifies and removes small faces and edges based on a area/length threshold.
This is useful for simplifying geometry before meshing in Mechanical.
"""

# Thresholds (adjust according to your model's scale)
FACE_AREA_THRESHOLD = 0.000001 # in m^2 (1mm^2 = 1e-6 m^2)
EDGE_LENGTH_THRESHOLD = 0.001  # in m (1mm)

def clean_small_features():
    # 1. Search for small faces
    # In SpaceClaim, we use the Repair tools
    from SpaceClaim.Api.V19.Modeler import SmallFaceSearch, SmallEdgeSearch

    print("Cleaning small faces (Area < {})...".format(FACE_AREA_THRESHOLD))
    small_faces = SmallFaceSearch.Create(GetRootPart(), FACE_AREA_THRESHOLD)
    if small_faces.Count > 0:
        # Use the Fix method
        # Note: Fix commands in SC often return a result object
        FixSmallFaces.Execute(small_faces)
        print("Removed {} small faces.".format(small_faces.Count))
    else:
        print("No small faces found.")

    print("Cleaning small edges (Length < {})...".format(EDGE_LENGTH_THRESHOLD))
    small_edges = SmallEdgeSearch.Create(GetRootPart(), EDGE_LENGTH_THRESHOLD)
    if small_edges.Count > 0:
        FixSmallEdges.Execute(small_edges)
        print("Removed {} small edges.".format(small_edges.Count))
    else:
        print("No small edges found.")

if __name__ == "__main__":
    clean_small_features()

