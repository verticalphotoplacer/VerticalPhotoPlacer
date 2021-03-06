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
from .pyexiftool import ExifTool
from .utility import refConversion


class ImageMetaStore:
    """
    Store frequently used metadata tags of a photo.
    """

    def __init__(self, image_width=None, image_height=None,
                 focal_length=None, gpslat=None, gpslon=None,
                 gpsalt=None, baroalt=None, groundalt=None,
                 heading=None, cam_model=None):

        self._image_width = None if image_width is None else int(image_width)
        self._image_height = None if image_height is None else int(image_height)
        self._focal_length = None if focal_length is None else float(focal_length)
        self._gpslat = None if gpslat is None else float(gpslat)
        self._gpslon = None if gpslon is None else float(gpslon)
        self._gpsalt = None if gpsalt is None else float(gpsalt)
        self._baroalt = None if baroalt is None else float(baroalt)
        self._groundalt = None if groundalt is None else float(groundalt)
        self._heading = None if heading is None else float(heading)
        self._cam_model = None if cam_model is None else str(cam_model)

    @property
    def image_width(self):
        return self._image_width

    @property
    def image_height(self):
        return self._image_height

    @property
    def focal_length(self):
        return self._focal_length

    @property
    def gpslat(self):
        return self._gpslat

    @property
    def gpslon(self):
        return self._gpslon

    @property
    def gpsalt(self):
        return self._gpsalt

    @property
    def baroalt(self):
        return self._baroalt

    @property
    def groundalt(self):
        return self._groundalt

    @groundalt.setter
    def groundalt(self, new_groundalt):
        self._groundalt = float(new_groundalt)

    @property
    def heading(self):
        return self._heading

    @property
    def cam_model(self):
        return self._cam_model


class ProcessMetadata:
    def __init__(self, photos):

        self.iw = "file:imagewidth"
        self.ih = "file:imageheight"
        self.fl = "exif:focallength"
        self.gpslat = "exif:gpslatitude"
        self.gpslat_ref = "exif:gpslatituderef"
        self.gpslon = "exif:gpslongitude"
        self.gpslon_ref = "exif:gpslongituderef"
        self.gpsalt = "exif:gpsaltitude"
        self.baroalt = "xmp:relativealtitude"
        self.groundalt = "xmp:groundaltitude"
        self.heading = "xmp:flightyawdegree"  # "xmp:gimbalyawdegree"
        self.cam_model = "exif:model"

        tags = [self.iw, self.ih, self.fl,
                self.gpslat, self.gpslat_ref, self.gpslon,
                self.gpslon_ref, self.gpsalt, self.baroalt,
                self.groundalt, self.heading, self.cam_model]

        metadata = None
        with ExifTool() as et:
            metadata = et.get_tags_batch(tags, photos)
            metadata = [{k.lower(): v for k, v in d.items()} for d in metadata]
        
        self.metadata = metadata
        
    def filterTagFromIndex(self, idx, tag):
        """Get tag value for a single photo, search based on index."""
        try:
            return self.metadata[idx][tag]
        except Exception:
            return None
        
    def hasBaroAltitude(self):
        """Check for barometer altitude existence."""
        try:
            baroalt = self.filterTagFromIndex(0, self.baroalt)
            if baroalt:
                return True
            else:
                return False
        except Exception:
            return False

    def getTagsByImgindex(self, idx):
        """Get tags of an photo which is identified by its index position in photo list.

        :param idx: index of the photo in the photo list.
        :type idx: int

        :return: tags value for the photo or None if error occurred.
        :rtype: ImageMetaStore or None
        """

        try:
            # latitude and longitude needs to be in global reference
            latref = self.filterTagFromIndex(idx, self.gpslat_ref)
            lonref = self.filterTagFromIndex(idx, self.gpslon_ref)
            lat = self.filterTagFromIndex(idx, self.gpslat)
            lon = self.filterTagFromIndex(idx, self.gpslon)
            if latref is not None and lonref is not None:
                lat = refConversion(lat, latref.lower())
                lon = refConversion(lon, lonref.lower())

            tags_data = {
                'image_width': self.filterTagFromIndex(idx, self.iw),
                'image_height': self.filterTagFromIndex(idx, self.ih),
                'focal_length': self.filterTagFromIndex(idx, self.fl) / 1000,
                'gpslat': lat,
                'gpslon': lon,
                'gpsalt': self.filterTagFromIndex(idx, self.gpsalt),
                'baroalt': self.filterTagFromIndex(idx, self.baroalt),
                'groundalt': self.filterTagFromIndex(idx, self.groundalt),
                'heading': self.filterTagFromIndex(idx, self.heading),
                'cam_model': self.filterTagFromIndex(idx, self.cam_model),
            }

            img_meta = ImageMetaStore(**tags_data)
            return img_meta

        except Exception:
            return None

    def getTagsAllImgs(self):
        """Get tags for all photos.

        :return: list of ImageMetaStore instances.
        :rtype: list
        """
        imgsmeta = [self.getTagsByImgindex(i) for i in range(len(self.metadata))]
        return imgsmeta