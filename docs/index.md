![ADJ_Principle](https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/icon/app_smaller.png?raw=true) Welcome to the Vertical Photo Placer plugin user guide!

The Vertical Photo Placer (VPP) is a free open source plugin for QGIS that performs quick placement of vertical drone photos on map.

The objective of VPP is to provide a tool for quickly geo-referencing and visualization of vertical drone photos on map. Geo-reference is done by generating a world file for each photo according to ESRI specification, see <a href="https://en.wikipedia.org/wiki/World_file">World file</a> for detailed information.

This plugin should be used in cases when quick information visualization is needed such as disaster response. If geo-referencing accuracy is top priority, more advanced tools should be considered.

* [Installation](#installation)
   * [Prerequisites](#prerequisites)
   * [Install from QGIS official plugin repository](#install-from-qgis-official-plugin-repository)
   * [Install from ZIP file](#install-from-zip-file)
* [Quick start](#quick-start)
* [Improving visualization of vertical drone photos](#improving-visualization-of-vertical-drone-photos)
   * [Home point correction](#home-point-correction)
   * [Adjacent photo matching](#adjacent-photo-matching)
   * [Simple correction](#simple-correction)

## Installation

### Prerequisites

The VPP is developed with Python 3 and available for QGIS version 3.x. This plugin requires the installation of GDAL, NumPy, ExifTool.
GDAL and NumPy are normally included in QGIS already. [ExifTool](https://exiftool.org/) is an external library for reading and writing metadata in photos. VPP uses ExifTool to access drone photo's metadata tags. 

First, install QGIS 3.x if it is not installed yet. Please download and install following this [guide](https://qgis.org/en/site/forusers/download.html).

To install ExifTool, download from the [official website](https://exiftool.org/) the suitable version to your machine (Windows or Linux/MacOS). Note that the Linux version can be used in both Linux and MacOS machines. The downloaded file is a compressed <b>.zip</b> file on Windows, or <b>.tar.gz</b> in Linux/MacOS. Then, extract the file to a folder (see Figure 1). It is free to choose the folder path. 

In addition, a "<b>.ExifTool_config</b>" file is required. This file can be downloaded from the [VPP's tool folder](https://github.com/verticalphotoplacer/VerticalPhotoPlacer/tree/master/tool). Please download and insert it to your ExifTool folder (see Figure 1).

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/exiftool_folderstructure.png?raw=true" alt="ExifTool folder structure">
  <br>
  <br>
  <em><b>Figure 1. Folder structure of ExifTool in Windows (above) and Linux/MacOS (below)</b></em>
</p>

Finally, this folder needs to be added to the QGIS's PATH environment variable. Please follow these steps in Figure 2. 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/insert_path_var_exiftool.png?raw=true" alt="ExifTool folder structure">
  <br>
  <br>
  <em><b>Figure 2. Add ExifTool folder to QGIS's PATH environment variable</b></em>
</p>

Please restart QGIS to apply these changes.

### Install from QGIS official plugin repository

The easiest way to install VPP is from the QGIS official plugin repository.

Please type "Vertical Photo Placer" in the search box if it is not easily located.

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/qgis_plugin_install_interface.png?raw=true" alt="Quickview_Guide">
  <br>
  <br>
  <em><b>Figure 1. Open QGIS Manage and Install Plugins Interface</b></em>
</p>

### Install from ZIP file

It is also possible in QGIS to install plugins from zip files. This feature is provided by the same QGIS Manage and Install Plugins Interface. This way, the source code of VPP should be compressed into a zip file. This file is made available at [the official QGIS Python Plugins Repository](https://plugins.qgis.org/plugins/vertical_photo_placer/), or at [VPP Github](https://github.com/verticalphotoplacer/VerticalPhotoPlacer/blob/master/zip/vertical_photo_placer.zip). Please download it to your computer.

Then, in the QGIS Manage and Install Plugins Interface, select tab "Install from ZIP" and install VPP from the downloaded zip file (See Figure 6).
QGIS may raise a warning as <em><b>"Security warning: installing a plugin from an untrusted source can lead to data loss and/or leak. Continue?"</b></em>. Press <b>Yes</b> to install. You should get a successful message on finish.

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/install_plugin_from_zip_archive_update.png?raw=true" alt="Install plugin from zip">
  <br>
  <br>
  <em><b>Figure 6. Install VPP plugin from zip file</b></em>
</p>

## Quick Start

VPP could be accessed either from the Menu Toolbar (Raster -> Vertical Photo Placer -> Vertical Photo Placer) or from the Plugins Toolbar (through app icon) (See Figure 7).

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/VPP_access.png?raw=true" alt="Access VPP">
  <br>
  <br>
  <em><b>Figure 7. Open VPP</b></em>
</p>

The default VPP user interface requires only one input to work, which is the full path of the photos folder (See figure 8). Users could either drag and drop/or browse to the input folder. In this mode, VPP performs Quick view to geo-referencing and visualizing all vertical drone photos found in the input folder. Geo-referencing uses default parameters as available in each photo's metadata. This is done automatically.  

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/DefaultUI.PNG?raw=true" alt="Quickview_Guide">
  <br>
  <br>
  <em><b>Figure 8. Guide to Quick view</b></em>
</p>

It is recommended to use this feature first to quickly visualize photos. Quick view will often deliver good placement of vertical photos which were taken on flat terrain from a home point of similar terrain elevation.

If the visualization is unsatisfactory, several adjustment features are provided, as described in the [following section](#improving-visualization-of-vertical-drone-photos).

## Improving visualization of vertical drone photos

Visualization may be influenced by several factors which include photo's ground altitude and GPS accuracy. GPS accuracy is often known and could be corrected in sophisticated software. This plugin focuses on estimation of the correct photo's ground altitude, to enhance visualization.

Drone photos such as DJI Phantom 4 contain barometer altitude and GPS altitude. Barometer altitude is often more stable than GPS altitude, but it is measured against home point. This could significantly reduce visualization if the terrain elevation of the home point is greatly different from the photo's terrain altitude. Therefore, it is desirable to estimate the home point's terrain elevation which then could be used to estimate a photo's ground altitude. [Home point correction](#home-point-correction) and [Adjacent photo matching](#adjacent-photo-matching) introduce two ways to estimate home point's terrain elevation.

Although GPS altitude is less stable than barometer altitude, it is still useful in cases where there is no barometer altitude, such as in some fixed-wing drones. But GPS altitude is still not the same as ground altitude yet. [Simple correction](#simple-correction) implements a method to estimate ground altitude from GPS altitude.

### Home point correction

This feature tries to estimate a photo's ground altitude from the home point's terrain altitude. It asks the user to locate the home point. Required inputs are photos input folder, a DEM file and location of the home point (See Figure 9). In the correction method, please select <em><b>Home point correction</b></em>. The DEM file could be SRTM (Shuttle Radar Topography Mission) or any applicable datasets (30 meter spatial resolution or less). 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/HomepointUI.PNG?raw=true" alt="Homepoing_Guide">
  <br>
  <br>
  <em><b>Figure 9. Guide to Home point correction</b></em>
</p>

The basis of this feature is that a photo's ground altitude (True ground altitude) could be estimated from its barometer altitude, terrain altitude and home point's terrain altitude (See Figure 10).

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/homepoint_principle.png?raw=true" alt="Homepoing_Principle">
  <br>
  <br>
  <em><b>Figure 10. Background of estimation of photo's ground altitude from home point's terrain altitude</b></em>
</p>

As the user is expected to provide location of the home point, it may be difficult in cases such as the user is not the person taking the photos, or just simply forgot the location. In such situations, [Adjacent photo matching](#adjacent-photo-matching) may be useful.

### Adjacent photo matching

Similar to Home point correction, this feature also tries to estimate a photo's ground altitude from home point's terrain altitude. However, the way to estimate is different. Required inputs are photos input folder and sliding offset resulting from photos matching (See Figure 11). In the correction method, please select <em><b>Adjacent photo matching</b></em>. DEM is optional but recommended. The DEM file could be SRTM (Shuttle Radar Topography Mission) or any applicable datasets (30 meter spatial resolution or less). 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/Adj_UI_after.PNG?raw=true" alt="Adj_UI_afterSliding">
  <br>
  <br>
  <em><b>Figure 11. Guide to Adjacent photos matching (after sliding)</b></em>
</p>

The basis of this feature is that the home point's terrain altitude could be estimated from matching two adjacent photos (See Figure 13). 

When first loaded, photo 1 and photo 2 are visualized in such a way that their geometric relationship is preserved. This process uses barometer altitude. 
However, barometer altitude is measured against home point's terrain altitude, these photos will not match each other if home point is at higher or lower elevation (See Figure 12). By changing these barometer altitudes so that the photos match (this gives the sliding offset, See Figure 11 and Figure 13), it is possible to estimate the home point's terrain altitude. From that, the photo's ground altitude can be estimated. 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/Adj_UI_before.PNG?raw=true" alt="Adj_UI_beforeSliding">
  <br>
  <br>
  <em><b>Figure 12. Guide to Adjacent photos matching (before sliding)</b></em>
</p>

Substraction sliding offset from the photo's terrain altitude gives home point's terrain altitude.

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/Adj_principle.png?raw=true" alt="Adj_Principle">
  <br>
  <br>
  <em><b>Figure 13. Background of estimation of photo's ground altitude by matching two adjacent photos</b></em>
</p>

### Simple correction

This feature tries to estimate a photo's ground altitude from GPS altitude. Required inputs are photos input folder and a DEM file (See Figure 14). In the correction method, please select <em><b>Simple correction</b></em>. The DEM file could be SRTM (Shuttle Radar Topography Mission) or any applicable datasets (30 meter spatial resolution or less). This is similar to the previous barometer-based altitude correction.   

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/SimpleUI.PNG?raw=true" alt="SimpleCorr_Guide">
  <br>
  <br>
  <em><b>Figure 14. Guide to Simple correction</b></em>
</p>

The basis of this feature is that the ground altitude is considered part of GPS altitude. The remaining part is terrain elevation. Therefore, ground altitude could be derived by subtracting terrain elevation from GPS altitude (See Figure 15). 

<p align="center">
  <img align="middle" src="https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/simplecorr_principle.png?raw=true" alt="SimpleCorr_Principle">
  <br>
  <br>
  <em><b>Figure 15. Background of estimation of photo's ground altitude by terrain subtraction</b></em>
</p>

Because Simple correction uses GPS altitude which may often be less stable than Barometer altitude, this feature should be used in cases where:
* The photos do not have a Barometer altitude.  
* It is difficult to remember the homepoint location.
* The GPS accuracy is so low that it is difficult to match adjacent photos.

## Useful links

* [Plugin github](https://github.com/verticalphotoplacer/VerticalPhotoPlacer)
* [User guide page](https://verticalphotoplacer.github.io/VerticalPhotoPlacer/)
* [QGIS Python Plugins Repository](https://plugins.qgis.org/plugins/)
