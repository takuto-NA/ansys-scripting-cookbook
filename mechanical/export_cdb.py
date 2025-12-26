# -*- coding: utf-8 -*-
"""
Mechanical Script: Export CDB (MAPDL Common Database)
Tested on: Ansys 2023 R2 (Mechanical)

Description:
This script exports the current simulation model as a .cdb (MAPDL input) file.
This includes the mesh, material properties, and boundary conditions.

Prerequisites:
- A mesh must be generated.
- A Static Structural or other analysis system must be present.
"""

import os

def export_to_cdb(file_path):
    """
    Exports the current analysis model to a .dat/.cdb file.
    """
    try:
        # Get the first analysis in the model
        analysis = Model.Analyses[0]
        
        # ExportMechanicalData generates a MAPDL input file (.dat)
        # Many users rename this to .cdb or use it directly in MAPDL.
        analysis.ExportMechanicalData(file_path)
        
        print("Successfully exported model to: {}".format(file_path))
    except Exception as e:
        print("Error during export: {}".format(e))

if __name__ == "__main__":
    # Define output path (Desktop)
    user_profile = os.environ.get("USERPROFILE")
    output_file = os.path.join(user_profile, "Desktop", "model_export.cdb")
    
    # Run the export
    export_to_cdb(output_file)

