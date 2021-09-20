# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:54:23 2020

@author: chuc9
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
                if x.find("name").text.lower() == model.lower():
                    width = float(x.find("width").text) / 1000  # original width is in milimeter
                    height = float(x.find("height").text) / 1000  # original height is in milimeter
                    return width, height
            raise CameraModelNotFound(f'Camera model not found for: {model.lower()}. \n'
                                      f'Please inserts the model name, sensor width and height to camlist.xml.')
        except Exception:
            raise

