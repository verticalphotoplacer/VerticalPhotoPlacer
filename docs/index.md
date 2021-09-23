![ADJ_Principle](https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/icon/app_smaller.png?raw=true) Welcome to the Vertical Photo Placer Plugin user guide!

The Vertical Photo Placer Plugin (VPP) is a free open source plugin for QGIS that performs quick placement of vertical drone photos on map.

The objective of VPP is to provide a tool for quickly geo-referencing and visualization of vertical drone photos on map. Geo-reference is done by generating a world file for each photo according to ESRI specification, see <a href="https://en.wikipedia.org/wiki/World_file">World file</a> for detailed information.

This plugin should be used in cases when quick information visualization is needed such as disaster response. If geo-referencing accuracy is top priority, more advanced tools should be considered.

* [Quick start](#quick-start)
* [Improving visualization of vertical drone photos](#improving-visualization-of-vertical-drone-photos)
   * [Home point correction](#home-point-correction)
   * [Adjacent photo matching](#adjacent-photo-matching)
   * [Simple correction](#simple-correction)

## Quick Start
The default VPP user interface requires only one input to work, which is the full path of the photos folder (See figure 1). User could either drag and drop/or browse to the input folder. In this mode, VPP performs Quick view to geo-referencing and visualizing all vertical drone photos found in the input folder. Geo-referencing uses default parameters as available in each photo's metadata. This is done automatically.  

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/DefaultUI.PNG?raw=true" alt="Quickview_Guide">
  <br>
  <br>
  <em><b>Figure 1. Guide to Quick view</b></em>
</p>

It is recommended to use this feature first to quickly visualize photos. Quick view will often deliver good placement of vertical photos which were taken on flat terrain from a home point of similar terrain elevation.

If the visualization is unsatisfactory, several adjustment features are provided, as described in the following section.

## Improving visualization of vertical drone photos

Visualization may be influenced by several factors which include photo's ground altitude and GPS accuracy. GPS accuracy is often known and could be corrected in sophisticated software. This plugin focuses on estimation of the correct photo's ground altitude, to enhance visualization.

Drone photos such as DJI Phantom 4 contain barometer altitude and GPS altitude. Barometer altitude is often more stable than GPS altitude, but it is measured against home point. This could significantly reduce visualization if the terrain elevation of the home point is greatly different from the photo's terrain altitude. Therefore, it is desirable to estimate the home point's terrain elevation which then could be used to estimate a photo's ground altitude. [Home point correction](#home-point-correction) and [Adjacent photo matching](#adjacent-photo-matching) introduce two ways to estimate home point's terrain elevation.

Although GPS altitude is less stable than barometer altitude, it is still useful in cases where there is no barometer altitude, such as in some fixed-wing drones. But GPS altitude is still not the same as ground altitude yet. [Simple correction](#simple-correction) implements a method to estimate ground altitude from GPS altitude.

### Home point correction
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

This feature tries to estimate photo's ground altitude from GPS altitude. Required inputs are photos input folder and a DEM file (See Figure 7). In the correction method, please select "Simple correction". DEM file could be SRTM or any applicable datasets. This is similar to the previous barometer-based altitude correction.   

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/SimpleUI.PNG?raw=true" alt="SimpleCorr_Guide">
  <br>
  <br>
  <em><b>Figure 7. Guide to Simple correction</b></em>
</p>

The basic of this feature is that the ground altitude is considered part of GPS altitude. The remaining part is terrain elevation. Therefore, ground altitude could be derived by substracting terrain elevation from GPS altitude (See Figure 8). 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/simplecorr_principle.png?raw=true" alt="SimpleCorr_Principle">
  <br>
  <br>
  <em><b>Figure 8. Background of estimation of photo's ground altitude by terrain substraction</b></em>
</p>

Because Simple correction uses GPS altitude which may often be less stable than Barometer altitude, this feature should be used in cases where:
* The photos do not have Barometer altitude.  
* It is difficult to remember homepoint location.
* The GPS accuracy is so low that it is difficult to match adjacent photos.
