# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:08:35 2020

@author: chuc9
"""

from qgis.PyQt.QtWidgets import QMessageBox, QLineEdit
import os

class FolderEdit(QLineEdit):
    def __init__(self, parent):
        super(FolderEdit, self).__init__(parent)

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
            if os.path.isdir(filepath):
                self.setText(filepath)
            else:
                dialog = QMessageBox()
                dialog.setSizeGripEnabled(True)
                dialog.setWindowTitle("Error: Invalid Input")
                dialog.setText("Only folder is accepted")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()