# -*- coding: utf-8 -*-
"""
Mechanical Script: Batch Assign Materials
Tested on: Ansys 2023 R2 (Mechanical)

Description:
This script iterates through all bodies in the geometry and assigns 
materials based on keywords found in the body name.
This is much faster than manual assignment for large assemblies.

Prerequisites:
- Materials (e.g., 'Steel', 'Aluminum') must already be added to the 
  Engineering Data of the Workbench project.
"""

# Define mapping: Keyword in Body Name -> Material Name in Engineering Data
MATERIAL_MAPPING = {
    "STEEL": "Structural Steel",
    "AL": "Aluminum Alloy",
    "BOLT": "Structural Steel",
}

def batch_assign_materials():
    # Get all bodies in the model
    # Model.Geometry.GetChildren(...) is used to traverse the tree
    all_bodies = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Body)
    
    count = 0
    for body in all_bodies:
        body_name = body.Name.upper()
        
        assigned = False
        for keyword, mat_name in MATERIAL_MAPPING.items():
            if keyword in body_name:
                try:
                    # Assignment is done via the Material property (string)
                    body.Material = mat_name
                    print("Assigned '{}' to Body: {}".format(mat_name, body.Name))
                    count += 1
                    assigned = True
                    break
                except Exception as e:
                    print("Failed to assign '{}' to Body: {}. Error: {}".format(mat_name, body.Name, e))
        
        if not assigned:
            print("No matching material found for Body: {}".format(body.Name))

    print("\nBatch assignment completed. Total bodies updated: {}".format(count))

if __name__ == "__main__":
    batch_assign_materials()

