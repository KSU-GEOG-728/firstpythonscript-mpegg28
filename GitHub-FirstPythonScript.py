#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Michael Pegg
    Description:  Calulates total river miles within the buffered ecoregion boundary.
    Date created: 09/11/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "C:/Users/mpegg/Documents/GitHub/firstpythonscript-mpegg28/GitHub-FirstPythonScript/ExerciseData.gdb"

# Geoprocessing Starts Here:

# Select the Ecoregion Polygon
flinthills = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

# Create a 10 km Buffer around the Ecoregion Boundary
arcpy.analysis.Buffer(flinthills, "FlintHills10km", "10 Kilometer", 'FULL', 'ROUND',  'NONE',"", 'PLANAR')

# Clip the Rivers inside the 10 km Buffer
arcpy.analysis.Clip('ks_major_rivers', "FlintHills10km", "ClippedRivers")

# Adds the Length of the Rivers in Miles
arcpy.management.AddGeometryAttributes("ClippedRivers", 'LENGTH', 'MILES_US')

# Total Sum of the Length of the Rivers in Miles
SumofRivers = arcpy.analysis.Statistics(ClippedRivers,"SumofRivers", [['LENGTH', "SUM"]])

