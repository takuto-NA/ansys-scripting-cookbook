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

import sys
import os

# --- Logger Setup ---
# Note: In production, you might want to point this to a fixed directory
# common_snippets folder should be in the sys.path
# (Simplified for demonstration)
try:
    from common_snippets.logger import SimpleLogger
    logger = SimpleLogger()
except ImportError:
    # Fallback to print if common-snippets is not in path
    class SimpleLoggerFallback:
        def info(self, msg): print("[INFO] " + msg)
        def error(self, msg): print("[ERROR] " + msg)
    logger = SimpleLoggerFallback()

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
    
    logger.info("Starting batch material assignment...")
    
    count = 0
    for body in all_bodies:
        body_name = body.Name.upper()
        
        assigned = False
        for keyword, mat_name in MATERIAL_MAPPING.items():
            if keyword in body_name:
                try:
                    # Assignment is done via the Material property (string)
                    body.Material = mat_name
                    logger.info("Assigned '{}' to Body: {}".format(mat_name, body.Name))
                    count += 1
                    assigned = True
                    break
                except Exception as e:
                    logger.error("Failed to assign '{}' to Body: {}. Error: {}".format(mat_name, body.Name, e))
        
        if not assigned:
            logger.info("No matching material found for Body: {}".format(body.Name))

    logger.info("Batch assignment completed. Total bodies updated: {}".format(count))

if __name__ == "__main__":
    batch_assign_materials()

