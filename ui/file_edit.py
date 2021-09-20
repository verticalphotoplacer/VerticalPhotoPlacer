# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:38:04 2020

@author: chuc9
"""

from qgis.PyQt.QtWidgets import QMessageBox, QLineEdit
import os

class FileEdit(QLineEdit):
    def __init__(self, parent):
        super(FileEdit, self).__init__(parent)

        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            if os.path.isfile(filepath):
                if filepath.lower().endswith('.tif'):
                    self.setText(filepath)
                else:
                    dialog = QMessageBox()
                    dialog.setSizeGripEnabled(True)
                    dialog.setWindowTitle("Error: Invalid Input")
                    dialog.setText("Only GeoTIFF file is accepted")
                    dialog.setIcon(QMessageBox.Warning)
                    dialog.exec_()
            else:
                dialog = QMessageBox()
                dialog.setSizeGripEnabled(True)
                dialog.setWindowTitle("Error: Invalid Input")
                dialog.setText("Only file is accepted")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()