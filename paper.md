---
title: 'Vertical Photo Placer: A free open source plugin for QGIS that performs quick placement of vertical drone photos on map'
tags:
  - photo
  - drone
  - mapping
  - visualization
  - qgis-plugin
authors:
  - name: Duc Chuc Man^[co-first author] # note this makes a footnote saying 'co-first author'
    affiliation: 3 
  - name: Hiroshi Inoue^[co-first author] # note this makes a footnote saying 'co-first author'
    affiliation: 2
  - name: Satoru Sugita^[co-first author]
    affiliation: 1
  - name: Hiromichi Fukui^[co-first author]
    affiliation: 1
affiliations:
 - name: International Digital Earth Applied Science Research Center, Chubu University
   index: 1
 - name: Integrated Research on Disaster Risk Reduction Division, National Research Institute for Earth Science and Disaster Resilience
   index: 2
 - name: Graduate School of Engineering, Chubu University
   index: 3
date: 04 October 2021
bibliography: paper.bib

# Summary

The Vertical Photo Placer (VPP) is a free open source plugin for QGIS that 
performs quick geo-referencing and visualization of vertical drone photos on map.
Geo-reference is done by generating a world file for each photo according to ESRI 
specification. This plugin should be used in cases when quick information visualization 
is needed such as disaster response. 

# Statement of need

Drone imagery is a valuable source of information in various situations which include 
disaster response. In such situations, quick disaster impact assessment and decision 
is expected. VPP is developed as a quick mapping tool of drone imageries for disaster 
impact assessment and decision support for local government. The tool simpliy places 
geo-tagged vertical aerial photos on GIS maps without stitching process. The vertical 
photos are then placed on the GIS base map with the world files. VPP does not make 
seamless stitching and ignore small errors caused by misalignment of the cameras and 
slope and curvature of the terrain in order to prioritize the promptness and simplicity 
of the process for quick impact assessment during the disaster. We introduces VPP to 
disaster management division of local goverments and fire departments in Mie-prefecture, 
Japan and in the Philippines through hands-on training to be prepared for the future disasters 
in the countries. 

# Overview of the Vertical Photo Placer Plugin

The default VPP user interface requires only one input to work, which is the full path 
of the photos folder. In this mode, VPP performs Quick view to geo-referencing and visualizing 
all vertical drone photos found in the input folder. Geo-referencing uses default parameters 
as available in each photo’s metadata. This features minimize user's interaction to provide 
quick visualization of information. 

Visualization may be influenced by several factors which include photo’s ground altitude 
and GPS accuracy. GPS accuracy is often known and could be corrected in sophisticated software. 
This plugin focuses on estimation of the correct photo’s ground altitude, to enhance visualization.
Drone photos such as DJI Phantom 4 contain barometer altitude and GPS altitude. Barometer altitude 
is often more stable than GPS altitude, but it is measured against home point.
This could significantly reduce visualization if the terrain elevation of the home point 
is greatly different from the photo’s terrain altitude. Therefore, it is desirable to estimate 
the home point’s terrain elevation which then could be used to estimate a photo’s ground altitude. 
Home point correction and Adjacent photo matching introduce two ways to estimate home point’s terrain elevation. 
It is noted that for these two features, the input folder should only contain photos of the same flight 
(i.e., share the same home point).

Although GPS altitude is less stable than barometer altitude, it is still useful in cases where there is 
no barometer altitude, such as in some fixed-wing drones. But GPS altitude is still not the same as 
ground altitude yet. Simple correction implements a method to estimate ground altitude from GPS altitude.

# Citations

# Figures

# Acknowledgements

The author thanks the International Digital Earth Applied Science Research Center, Chubu University 
and National Research Institute for Earth Science and Disaster Resilience (NIED), Japan.

# References
