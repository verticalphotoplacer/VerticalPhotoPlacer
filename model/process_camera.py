# -*- coding: utf-8 -*-
"""
/******************************************************************************************
 VerticalPhotoPlacer

 The Vertical Photo Placer Plugin for QGIS performs quick placement of
 vertical drone photos on map.
                              -------------------
        begin                : 2019-09-05
        copyright            : (C) 2019-2021 by Chubu University and
               National Research Institute for Earth Science and Disaster Resilience (NIED)
        email                : chuc92man@gmail.com
 ******************************************************************************************/

/******************************************************************************************
 *   This file is part of Vertical Photo Placer Plugin.                                   *
 *                                                                                        *
 *   This program is free software; you can redistribute it and/or modify                 *
 *   it under the terms of the GNU General Public License as published by                 *
 *   the Free Software Foundation, version 3 of the License.                              *
 *                                                                                        *
 *   Vertical Photo Placer Plugin is distributed in the hope that it will be useful,      *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or    *
 *   FITNESS FOR A PARTICULAR PURPOSE.                                                    *
 *   See the GNU General Public License for more details.                                 *
 *                                                                                        *
 *   You should have received a copy of the GNU General Public License along with         *
 *   Vertical Photo Placer Plugin. If not, see <http://www.gnu.org/licenses/>.            *
 ******************************************************************************************/
"""
import xml.etree.ElementTree as Et
from .utility import resolveFile


class CameraModelNotFound(Exception):
    pass


class ProcessCamera:
    """Search camera sensor size from xml config file.
    """

    def __init__(self):
        
        self.tree = Et.parse(resolveFile("camlist.xml"))
        self.root = self.tree.getroot()
    
    def getCamsize(self, model):
        """Get camera size in meter unit.

        :param model: name of camera model.
        :type model: string

        :return: width and height of camera.
        :rtype: tuple
        """

        try:
            for x in self.root.findall("model"):
                if model.lower() == x.find("name").text.lower():
                    width = float(x.find("width").text) / 1000  # original width is in milimeter
                    height = float(x.find("height").text) / 1000  # original height is in milimeter
                    return width, height
            raise CameraModelNotFound('Camera model not found for: {0}. '
                                      'Please inserts the model name, sensor width and height to camlist.xml.'.
                                      format(model.lower()))
        except Exception:
            raise


def guessCamSensorSize(img_width, img_height):
    sw = img_width*1.55/1000000   # 3000 -> 4.5,  close guess to some DJI camera models
    sh = img_height*1.55/1000000   # 4000 -> 6.0,  close guess to some DJI camera models

    return sw, sh


def getCamSensorSize(rcamobj, model, img_width, img_height):
    """ Get sensor size from available list first.
    If not found, try to guess.

    :param rcamobj: ProcessCamera object
    :type rcamobj: ProcessCamera

    :param model: camera model name
    :type model: string

    :param img_width: photo width
    :type img_width: int

    :param img_height: photo height
    :type img_height: int

    :return: sensor width and height
    :rtype: tuple
    """

    try:
        sw, sh = rcamobj.getCamsize(model)
    except CameraModelNotFound:
        sw, sh = guessCamSensorSize(img_width, img_height)

    return sw, sh
