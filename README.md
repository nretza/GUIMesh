# updates by me (github.com/nretza)
Since a CAD -> gdml converter was needed for GEANT4 simulations of P-ONE, multiple options were evaluated. Reviving this repo and making small adjustments seems to be the most feasible option.

## setting it up
1. clone the repo
2. make sure the stuff in requirements.txt is installed and running
3. you are good to go

## usage
P-ONE geometry files exist in a Solidworks environment. This converter takes in *.step files, so make use of Solidworks export function to export the geometry to *.step. Check out [The Solidworks documentation](https://help.solidworks.com/2022/English/SolidWorks/sldworks/HIDD_EXPORT_OPTIONS_STEP.htm) for more information.

Run GUIMesh.py, import the *.step file and set the necessary material information. [This](Documents/GUIMesh%20User%20Manual.pdf) is a well done visual guide through the program by its original author Marco Gui Alves Pinto for reference.

**IMPORTANT:** In order to allow an errorless conversion, make sure to resolve all subassemblys in Solidworks. The The exported Step file should only contain `Part` objects
## changes made 

* updated for python 3
* fixed bugs in material manager
* autodetect freecad in commonly used install dirs
* converter adjustments to properly handle *.step files coming from Solidworks
* fixed bugs in gdml output that prohibited direct import in GEANT4

# GUIMesh (original README)
Copyright (c) 2018  Marco Gui Alves Pinto  mail:mgpinto11@gmail.com

This program is distributed under the terms of the GNU General Public License 3

### Software Description
GUIMesh is a Graphical User Interface that converts STEP geometries to GDML format allowing
to import this geometries into Geant4

### Citation / Reference
GUIMesh is published in: https://doi.org/10.1016/j.cpc.2019.01.024. It has a full description of the program as well as all the tests done. You can request me the document via e-mail.
Please cite the paper if you found GUIMesh useful for your work.

### Dependencies
GUIMesh requires:

* UNIX distribution or Windows (R) 
* [Python 2.X](www.python.org) with TKinter extension
* [FreeCAD](www.freecadweb.org) v0.15 and 0.16
* [Geant4](https://geant4.web.cern.ch/) - although Geant4 is not necessary to run GUIMesh, its output are intended to be imported by it. Versions >10 are recomended.

Note: Since GUIMesh is a python script only its dependencies must be installed.

### File description
* GUIMesh.py - Main and only source code
* Documents - Folder with "GUIMesh User Manual.pdf", a guide on how to run GUIMesh found in the Documents directory
* GUIMeshLibs - folder containing libraries used in GUIMesh
* Materials - folder which should be used to save materials in a database
* STEP Files - folder with STEP geometries used in all tests
* COPYING - License disclosure

