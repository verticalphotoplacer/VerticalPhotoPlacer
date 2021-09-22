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
import numpy as np
from os.path import join, dirname

from .process_metadata import *
from .utility import getDSMValbyCoors
from .pyexiftool import ExifTool


class TaskCancelledByUser(Exception):
    pass


def updateTagswithExiftool(imgfolder, processed_files, imgs_spec):
    """Update photo's exif tags.

    :param imgfolder: folder containing photos.
    :type imgfolder: string

    :param processed_files: list of processed file.
    :type processed_files: list

    :param imgs_spec: list of images metadata.
    :type imgs_spec: list
    """

    update_txt = list()
    update_txt.append("SourceFile,GroundAltitude")
    for photo, spec in zip(processed_files, imgs_spec):
        update_txt.append("{0},{1}".format(photo, spec.groundalt))

    update_txt = np.array(update_txt)
    csvname = join(imgfolder, "update_altitude.csv")  # a csv file is required for the update process
    np.savetxt(csvname, update_txt, fmt='%s', delimiter=",")
    # then, update using exiftool
    with ExifTool() as et:
        status = et.write_tag_batch(csvname, imgfolder)
        if not status:
            raise Exception('Failed calling batch update exiftool: [Input folder]: {0}'.format(imgfolder))


def loadPhotosMetadata(task, params):
    """Load metadata of photos.

    :param task: task object passed from calling function

    :param params: params: list of parameters, containing:
        photos: list of string, containing fullpaths of photos

    :return: list of processed file, its metadata and summary of task
    :rtype: dict
    """

    photos = params[0]

    task.setProgress(1)

    imgsmeta = ProcessMetadata(photos).getTagsAllImgs()

    task.setProgress(100)
    if task.isCanceled():
        raise TaskCancelledByUser('Task cancelled!')

    return {'files': photos, 'imgsmeta': imgsmeta, 'task': task.description()}


def altitudeAdjusterTerrain(task, params):
    """Estimation of ground altitude based on terrain height substraction.
    This function uses photo's GPS altitude.

    :param task: task object passed from calling function

    :param params: list of parameters, containing:
        photos: list of string, containing fullpaths of photos
        imgs_spec: list of images metadata.
        dem_path: string, path to DEM file

    :return: list of processed file, its metadata and summary of task
    :rtype: dict
    """

    photos = params[0]
    imgs_spec = params[1]
    dsm = params[2]

    task.setProgress(1)

    n_photos = len(photos)
    processed_index = list()
    for i in range(0, n_photos):
        try:
            # If photo has a GPS altitude and it is covered by DEM file, correction is possible.
            # Else, exceptions are raised.
            lat, lon = imgs_spec[i].gpslat, imgs_spec[i].gpslon
            img_terrain_alt = getDSMValbyCoors(dsm, [lon, lat])
            imgs_spec[i].groundalt = imgs_spec[i].gpsalt - img_terrain_alt
            processed_index.append(i)
        except Exception:
            continue

        task.setProgress(float((i + 1) / n_photos) * 100)
        if task.isCanceled():
            raise TaskCancelledByUser('Task cancelled!')

    processed_files = [photos[i] for i in processed_index]
    imgs_spec = [imgs_spec[i] for i in processed_index]
    updateTagswithExiftool(dirname(photos[0]), processed_files, imgs_spec)

    return {'files': processed_files, 'imgsmeta': imgs_spec, 'task': task.description()}


def altitudeAdjusterAdjacent(task, params):
    """Estimation of ground altitude based on adjacent photo matching.
    This function uses photo's barometer altitude.

    :param task: task object passed from calling function

    :param params: list of parameters, containing:
        photos: list of string, containing fullpaths of photos
        imgs_spec: list of images metadata
        home_terrain_alt: float, terrain altitude of homepoint if DEM else offset altitude
        adj_terrain_alt_avg: float, average terrain altitude of the overlap photos
        dsm: string, path to DEM file

    :return: list of processed file, its metadata and summary of task
    :rtype: dict
    """

    photos = params[0]
    imgs_spec = params[1]
    home_terrain_alt = params[2]
    adj_terrain_alt_avg = params[3]
    dsm = params[4]

    task.setProgress(1)

    # correction
    n_photos = len(photos)
    processed_index = list()
    for i in range(0, n_photos):
        try:
            # if there is barometer altitude, correction is possible
            # if dsm is specified, use dsm in correction
            if dsm:
                lat, lon = imgs_spec[i].gpslat, imgs_spec[i].gpslon
                img_terrain_alt = getDSMValbyCoors(dsm, [lon, lat])
                # best guest if DSM does not cover the photo location.
                img_terrain_alt = img_terrain_alt if img_terrain_alt else adj_terrain_alt_avg
                imgs_spec[i].groundalt = imgs_spec[i].baroalt + (home_terrain_alt - img_terrain_alt)
            else:
                # In this case, home_terrain_alt is just the offset which complements adj-photos-barometer alts
                # to make up its ground altitude.
                # Thus, this case works best in flat terrains.
                imgs_spec[i].groundalt = imgs_spec[i].baroalt + home_terrain_alt
            processed_index.append(i)
        except Exception:
            continue

        task.setProgress(float((i + 1) / n_photos) * 100)
        if task.isCanceled():
            raise TaskCancelledByUser('Task cancelled!')

    processed_files = [photos[i] for i in processed_index]
    imgs_spec = [imgs_spec[i] for i in processed_index]
    updateTagswithExiftool(dirname(photos[0]), processed_files, imgs_spec)

    return {'files': processed_files, 'imgsmeta': imgs_spec, 'task': task.description()}


def altitudeAdjusterHome(task, params):
    """Estimation of photo's ground altitude based on home point terrain altitude.
    This function uses photo's barometer altitude.

    :param task: task object passed from calling function

    :param params: list of parameters, containing:
        homepoint_alt: float, elevation of home point
        photos: list of string, containing fullpaths of photos
        imgs_spec: list of images metadata
        dem_path: string, path to DEM file

    :return: list of processed file, its metadata and summary of task
    :rtype: dict
    """

    home_terrain_alt = params[0]
    photos = params[1]
    imgs_spec = params[2]
    dsm = params[3]

    task.setProgress(1)

    # correction
    n_photos = len(photos)
    processed_index = list()
    for i in range(0, n_photos):
        try:
            # If photo has a GPS altitude and it is covered by DEM file, correction is possible.
            # Else, exceptions are raised.
            # calculate ground altitude
            lat, lon = imgs_spec[i].gpslat, imgs_spec[i].gpslon
            img_terrain_alt = getDSMValbyCoors(dsm, [lon, lat])
            imgs_spec[i].groundalt = imgs_spec[i].baroalt + (home_terrain_alt - img_terrain_alt)
            processed_index.append(i)
        except Exception:
            continue

        task.setProgress(float((i + 1) / n_photos) * 100)
        if task.isCanceled():
            raise TaskCancelledByUser('Task cancelled!')

    processed_files = [photos[i] for i in processed_index]
    imgs_spec = [imgs_spec[i] for i in processed_index]
    updateTagswithExiftool(dirname(photos[0]), processed_files, imgs_spec)

    return {'files': processed_files, 'imgsmeta': imgs_spec, 'task': task.description()}
