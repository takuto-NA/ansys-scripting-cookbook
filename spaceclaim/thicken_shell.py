# -*- coding: utf-8 -*-
"""
SpaceClaim Script: Thicken Surfaces (Solidify)
Tested on: Ansys 2023 R2 (SpaceClaim)

Description:
This script thickens all surface bodies (shells) in the current design 
to turn them into solids. It allows specifying the thickness and whether 
to offset from both sides.
"""

# SpaceClaim specific unit helper: MM(x) converts millimeters to meters
# This is usually available in the SpaceClaim scripting environment.

def thicken_all_surfaces(thickness_mm, offset_both_sides=True):
    """
    Finds all surface bodies and thickens them.
    """
    root = GetRootPart()
    # Find all bodies where the shape is a surface (not a solid)
    surfaces = [b for b in root.Bodies if b.Shape.IsSurface]
    
    if not surfaces:
        print("No surface bodies found in the design.")
        return

    # Create a selection for all found surfaces
    selection = Selection.Create(surfaces)
    
    # Set up thickening options
    options = ThickenOptions()
    options.ThickenBothSides = offset_both_sides
    
    # Execute the thicken operation
    # Note: SpaceClaim API uses meters for length values by default.
    # The thickness is the TOTAL thickness.
    thickness = MM(thickness_mm)
    
    try:
        Thicken.Execute(selection, thickness, options)
        print("Successfully thickened {} surfaces by {} mm.".format(len(surfaces), thickness_mm))
    except Exception as e:
        print("Failed to thicken surfaces: {}".format(e))

if __name__ == "__main__":
    # Example: Thicken shells to 2.0 mm (1.0 mm on each side if offset_both_sides=True)
    thicken_all_surfaces(2.0, offset_both_sides=True)

