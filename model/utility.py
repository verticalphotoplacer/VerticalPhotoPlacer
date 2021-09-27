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
from os import listdir
from os.path import isfile, join, exists, realpath, dirname, splitext
import shutil
from osgeo import gdal
import math


class ReferenceDirectionTextNotFound(Exception):
    pass


def computeHomepTerrAltfromAdjPhotosMatching(dsm_file, img1_coors, img2_coors, adjmatching_alt):
    overlapimg1_theight = getDSMValbyCoors(dsm_file, img1_coors)
    overlapimg2_theight = getDSMValbyCoors(dsm_file, img2_coors)
    if None in [overlapimg1_theight, overlapimg2_theight]:
        adj_terrain = 0
    else:
        adj_terrain = (overlapimg1_theight + overlapimg2_theight) / 2
    home_terrain_alt = adj_terrain + adjmatching_alt

    return home_terrain_alt, adj_terrain


def refConversion(coor, direction):
    direction_mult = {'n': 1, 's': -1, 'e': 1, 'w': -1, 'north': 1, 'south': -1, 'east': 1, 'west': -1}
    if direction in direction_mult:
        return coor*direction_mult[direction]
    else:
        raise ReferenceDirectionTextNotFound("Expected coordinate reference to be in {0}, "
                                             "but found '{1}' instead.".format(direction_mult.keys(), direction))


def getWorldfileExistPhotos(photos, world_ext):
    """
    :param photos: list of filepaths of photos.
    :type photos: list

    :param world_ext: extension of worldfiles.
    :type world_ext: string

    :return: list of photos that has worldfile.
    :rtype: list
    """

    has_worldfile = []
    n_files = len(photos)
    for i in range(0, n_files):
        wf = splitext(photos[i])[0] + world_ext
        if isfile(wf):
            has_worldfile.append(i)

    ok_photos = [photos[i] for i in has_worldfile]

    return ok_photos


def getGroundsize(iw, ih, sw, sh, fl, altitude):
    """Compute ground pixel size."""
    scale_factor = altitude / fl
    sensor_pixel_width = sw / iw
    sensor_pixel_length = sh / ih
    
    ground_pixel_width = sensor_pixel_width * scale_factor
    ground_pixel_length = sensor_pixel_length * scale_factor
    
    return ground_pixel_width, ground_pixel_length


def resolveTool(prog):
    tool = shutil.which(prog)
    if not tool:
        raise Exception('Cannot find {0}, make sure to add {1} to the system path variable.'.format(prog, prog))
    return tool


def resolveFile(name):
    """Find fullpath of a file."""
    basepath = dirname(realpath(__file__))
    return join(basepath, name)


def getPhotos(folder, exts=('.jpg')):
    """Get all photos with extensions inside a folder."""
    folder = str(folder)
    imgs = []
    if exists(folder):
        imgs = [join(folder, f) for f in listdir(folder) if (isfile(join(folder, f)) and f.lower().endswith(exts))]
        
    return imgs


def getDSMValbyCoors(DSMfname, coors):
    """Get DSM value by coors [lon, lat]."""
    try:
        dataset = gdal.Open(DSMfname)
        if dataset is None:
            return None
        
        band = dataset.GetRasterBand(1)
        
        cols = dataset.RasterXSize
        rows = dataset.RasterYSize
        
        transform = dataset.GetGeoTransform()
        
        x_origin = transform[0]
        y_origin = transform[3]
        pixel_width = transform[1]
        pixel_height = -transform[5]
        
        data = band.ReadAsArray(0, 0, cols, rows)
        
        col = int((coors[0] - x_origin) / pixel_width)
        row = int((y_origin - coors[1]) / pixel_height)
    
        # if DEM files is not covering this area
        if col >= cols or row >= rows or col < 0 or row < 0:
            return None  
        
        return float(data[row][col])
    
    except Exception:
        return None


def meter2Degree(latitude, x_length, y_length):
    """Convert from meter to degree, in both longitude and latitude directions.
    
    :param latitude: latitude coordinate (in decimal unit) at which the lengths to be converted to degrees.
    :type latitude: float

    :param x_length: length in longitude direction.
    :type x_length: float

    :param y_length: length in latitude direction.
    :type y_length: float

    :return: x_length and y_length in degrees, decimal format.
    :rtype: tuple
    """

    x_length = x_length / (111320 * math.cos(math.radians(latitude)))
    y_length = y_length / 110540

    return x_length, y_length

