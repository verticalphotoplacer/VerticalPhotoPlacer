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

from qgis.PyQt.QtWidgets import QGraphicsPixmapItem
from qgis.PyQt.QtGui import QPen, QColor

class PixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, parent=None):
        super().__init__(pixmap, parent)
        self.setAcceptHoverEvents(True)
        #self._is_hovered = True

    # def hoverEnterEvent(self, event):
    #     self._is_hovered = True
    #     self.update()
    #     super().hoverEnterEvent(event)

    # def hoverLeaveEvent(self, event):
    #     self._is_hovered = False
    #     self.update()
    #     super().hoverLeaveEvent(event)

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        #if self._is_hovered:
        painter.save()
        pen = QPen(QColor("red"))
        pen.setWidth(1)
        painter.setPen(pen)
        r = self.boundingRect()
        r.adjust(0, 0, -pen.width()/2, -pen.width()/2)
        painter.drawRect(r)
        painter.restore()
