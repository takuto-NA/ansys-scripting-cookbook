# -*- coding: utf-8 -*-
"""
Mechanical Script: Set Global Mesh Size
Tested on: Ansys 2023 R2 (Mechanical)

Description:
This script sets the global element size and generates the mesh.
"""

def set_global_mesh_size(size_mm):
    """
    Sets the global mesh element size.
    """
    mesh = Model.Mesh
    
    # Set element size using Quantity to ensure units are correct
    mesh.ElementSize = Quantity("{} [mm]".format(size_mm))
    
    # Optional: Set other global settings
    # mesh.Resolution = 2
    # mesh.PhysicsSelected = MeshPhysicsRestraint.Structural
    
    print("Global mesh size set to {} mm.".format(size_mm))
    
    # Generate mesh
    mesh.GenerateMesh()
    print("Mesh generation completed.")

if __name__ == "__main__":
    # Example: Set global mesh size to 5.0 mm
    set_global_mesh_size(5.0)

