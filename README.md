# Vertical Photo Placer

![VPP](https://github.com/verticalphotoplacer/VerticalPhotoPlacer/blob/master/icon/app_smaller.png?raw=true) The Vertical Photo Placer (VPP) is a free open source plugin for QGIS that performs quick placement of vertical drone photos on map.

The objective of VPP is to provide a tool for quickly geo-referencing and visualization of vertical drone photos on map. Geo-reference is done by generating a world file for each photo according to ESRI specification, see https://en.wikipedia.org/wiki/World_file for detailed information.

![VPP](https://github.com/verticalphotoplacer/VerticalPhotoPlacerPlugin/blob/master/docs/img/vpp_example_update.png?raw=true)

This plugin should be used in cases when quick information visualization is needed such as disaster response. If geo-referencing accuracy is top priority, more advanced tools should be considered.

## Plugin installation

The VPP is developed with Python 3 and available for QGIS version 3.x. This plugin requires the installation of GDAL, NumPy, Exiftool.

The easiest way to install VPP is through QGIS's Manage and Install Plugins Interface.

First, install QGIS 3.x if it is not installed yet. Please download and install following this [guide](https://qgis.org/en/site/forusers/download.html).

Then, open the QGIS application and install this plugin by following this [guide (sections 9.1.1 and 9.1.2)](https://docs.qgis.org/3.16/en/docs/training_manual/qgis_plugins/fetching_plugins.html). 
Please type "Vertical Photo Placer" in the search box if it is not easily located.

## Usage

Please follow this [tutorial](https://verticalphotoplacer.github.io/VerticalPhotoPlacer/).

[Videos] are also available.

## Contributing

If you find some issue that you are willing to fix, code contributions are welcome. Please read [the development notes](DEVELOPMENT.md) before contributing. 

## Author

* **Man Duc Chuc** 

## Credits

The author thanks the International Digital Earth Applied Science Research Center, Chubu University and National Research Institute for Earth Science and Disaster Resilience (NIED), Japan.

## License

This plugin is distributed under a GNU General Public License version 3.

## How to cite 
Coming soon!

## Code on Zenodo
Coming soon!
