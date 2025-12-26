# -*- coding: utf-8 -*-
"""
Mechanical Script: Add Local Sizing
Tested on: Ansys 2023 R2 (Mechanical)

Description:
This script adds a 'Sizing' control to a specific Named Selection.
"""

def add_local_sizing(ns_name, size_mm):
    """
    Adds a local sizing control to the specified Named Selection.
    """
    # Find the Named Selection
    all_ns = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.NamedSelection)
    target_ns = [ns for ns in all_ns if ns.Name == ns_name]
    
    if not target_ns:
        print("Error: Named Selection '{}' not found.".format(ns_name))
        return
    
    ns = target_ns[0]
    
    # Add Sizing control to the Mesh object
    mesh = Model.Mesh
    sizing = mesh.AddSizing()
    
    # Assign the Named Selection to the Sizing control
    sizing.Location = ns
    
    # Set the local element size
    sizing.ElementSize = Quantity("{} [mm]".format(size_mm))
    sizing.Name = "Local Sizing - {}".format(ns_name)
    
    print("Added local sizing of {} mm to '{}'.".format(size_mm, ns_name))
    
    # Re-generate mesh to apply changes
    # mesh.GenerateMesh()

if __name__ == "__main__":
    # Example: Add 1.0 mm sizing to 'NS_CriticalArea'
    add_local_sizing("NS_CriticalArea", 1.0)

