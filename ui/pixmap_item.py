# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:18:03 2020

@author: chuc9
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
