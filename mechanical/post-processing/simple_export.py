# -*- coding: utf-8 -*-
"""
Mechanical Script: Simple Maximum Stress Export
Tested on: Ansys 2023 R2 (Mechanical)

Description:
This script finds the Equivalent (von-Mises) Stress result in the tree,
gets its maximum value, and exports it to a text file.

Prerequisites:
- A completed static structural or similar analysis.
- 'Equivalent Stress' result must exist in the Solution branch.
"""

import os

def export_max_stress(output_path):
    # Get all results in the solution
    results = DataModel.GetObjectsByType(Ansys.ACT.Automation.Mechanical.Results.Result)
    
    stress_result = None
    for res in results:
        # Looking for 'Equivalent Stress'
        if "Equivalent Stress" in res.Name:
            stress_result = res
            break
            
    if stress_result:
        # Get the maximum value
        max_stress = stress_result.Maximum
        unit = stress_result.ResultUnit
        
        # Write to file
        with open(output_path, "w") as f:
            f.write("Result Name: {}\n".format(stress_result.Name))
            f.write("Maximum Stress: {} [{}]\n".format(max_stress, unit))
            
        print("Successfully exported max stress to: {}".format(output_path))
    else:
        print("Error: 'Equivalent Stress' result not found.")

if __name__ == "__main__":
    # Define output path (Desktop)
    user_profile = os.environ.get("USERPROFILE")
    output_file = os.path.join(user_profile, "Desktop", "max_stress_export.txt")
    
    export_max_stress(output_file)

