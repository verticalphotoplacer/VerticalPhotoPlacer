# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:46:01 2020

@author: chuc9
"""

from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox, QSpinBox, QFormLayout

class InputDialog(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QSpinBox(self)
        self.first.setRange(-10000, 10000)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Max value", self.first)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.value())