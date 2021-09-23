Welcome to the Vertical Photo Placer Plugin user guide!

## Contents
[Quick start](#quick-start)

[Improving visualization of vertical drone photos](#improving-visualization-of-vertical-drone-photos)

[Custom foo description](#foo)

![ADJ_Principle](https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/icon/app_smaller.png?raw=true) The Vertical Photo Placer Plugin (VPP) is a free open source plugin for QGIS that performs quick placement of vertical drone photos on map.

The objective of VPP is to provide a tool for quickly geo-referencing and visualization of vertical drone photos on map. Geo-reference is done by generating a world file for each photo according to ESRI specification, see https://en.wikipedia.org/wiki/World_file for detailed information.

This plugin should be used in cases when quick information visualization is needed such as disaster response. If geo-referencing accuracy is top priority, more advanced tools should be considered.

## Quick Start
The default VPP user interface requires only one input to work, which is fullpath of the photos folder (See figure 1). User could either drag and drop/or browse to the input folder. In this mode, VPP performs Quick view to geo-referencing and visualizing all vertical drone photos found in the input folder. Geo-referencing uses default parameters as available in each photo's metadata. This is done automatically.  

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/DefaultUI.PNG?raw=true" alt="Quickview_Guide">
  <br>
  <br>
  <em><b>Figure 1. Guide to Quick view</b></em>
</p>

It is recommended to use this feature first to quickly visualize photos. If the visualization is unsatisfactory, adjustment could be made later.

## Improving visualization of vertical drone photos


### Home point position
<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/HomepointUI.PNG?raw=true" alt="Homepoing_Guide">
  <br>
  <br>
  <em><b>Figure 2. Guide to Home point correction</b></em>
</p>

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/homepoint_principle.png?raw=true" alt="Homepoing_Principle">
  <br>
  <br>
  <em><b>Figure 3. Background of estimation of photo's ground altitude from home point's terrain altitude</b></em>
</p>

### Adjacent photo matching
To be updated.

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/Adj_UI_after.PNG?raw=true" alt="Adj_UI_afterSliding">
  <br>
  <br>
  <em><b>Figure 4. Guide to Adjacent photos matching (after sliding)</b></em>
</p>

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/Adj_UI_before.PNG?raw=true" alt="Adj_UI_beforeSliding">
  <br>
  <br>
  <em><b>Figure 5. Guide to Adjacent photos matching (before sliding)</b></em>
</p>

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/adj_principle.png?raw=true" alt="Adj_Principle">
  <br>
  <br>
  <em><b>Figure 6. Background of estimation of photo's ground altitude by matching two adjacent photos</b></em>
</p>

### Simple correction

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/SimpleUI.PNG?raw=true" alt="SimpleCorr_Guide">
  <br>
  <br>
  <em><b>Figure 7. Guide to Simple correction</b></em>
</p>

<p align="center">
<img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/simplecorr_principle.png?raw=true" alt="SimpleCorr_Principle">
  <br>
  <br>
  <em><b>Figure 8. Background of estimation of photo's ground altitude by terrain substraction</b></em>
</p>

This feature tries to estimate photo's ground altitude from GPS altitude. The ground altitude is considered part of GPS altitude. The remaining part is terrain elevation. Therefore, to use Simple correction, a digital elevation data file (DEM) is required. DEM file could be SRTM or any applicable datasets. 

Because Simple correction uses GPS altitude which may often be less stable than Barometer altitude, this feature should be used in case where the photos do not have Barometer altitude. 
