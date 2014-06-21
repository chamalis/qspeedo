# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speedo.ui'
#
# Created: Wed Jul 24 11:18:22 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Speedo(object):
#    def __init__(self):
#        self.setupUi(Speedo)
    
    def setupUi(self, Speedo):
        Speedo.setObjectName(_fromUtf8("Speedo"))
        Speedo.resize(400, 300)
        self.widget = QtGui.QWidget(Speedo)
        self.widget.setGeometry(QtCore.QRect(20, 50, 63, 227))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.labelsLayout = QtGui.QVBoxLayout(self.widget)
        self.labelsLayout.setSpacing(30)
        self.labelsLayout.setMargin(0)
        self.labelsLayout.setObjectName(_fromUtf8("labelsLayout"))
        self.speedLabel = QtGui.QLabel(self.widget)
        self.speedLabel.setObjectName(_fromUtf8("speedLabel"))
        self.labelsLayout.addWidget(self.speedLabel)
        self.rotations = QtGui.QLabel(self.widget)
        self.rotations.setObjectName(_fromUtf8("rotations"))
        self.labelsLayout.addWidget(self.rotations)
        self.voltageLabel = QtGui.QLabel(self.widget)
        self.voltageLabel.setObjectName(_fromUtf8("voltageLabel"))
        self.labelsLayout.addWidget(self.voltageLabel)
        self.intensityLabel = QtGui.QLabel(self.widget)
        self.intensityLabel.setObjectName(_fromUtf8("intensityLabel"))
        self.labelsLayout.addWidget(self.intensityLabel)
        self.power = QtGui.QLabel(self.widget)
        self.power.setObjectName(_fromUtf8("power"))
        self.labelsLayout.addWidget(self.power)
        self.widget1 = QtGui.QWidget(Speedo)
        self.widget1.setGeometry(QtCore.QRect(110, 50, 66, 231))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.lcdLayout = QtGui.QVBoxLayout(self.widget1)
        self.lcdLayout.setSpacing(15)
        self.lcdLayout.setMargin(0)
        self.lcdLayout.setObjectName(_fromUtf8("lcdLayout"))
        self.lcdSpeed = QtGui.QLCDNumber(self.widget1)
        self.lcdSpeed.setObjectName(_fromUtf8("lcdSpeed"))
        self.lcdLayout.addWidget(self.lcdSpeed)
        self.lcdTime = QtGui.QLCDNumber(self.widget1)
        self.lcdTime.setObjectName(_fromUtf8("lcdTime"))
        self.lcdLayout.addWidget(self.lcdTime)
        self.lcdVoltage = QtGui.QLCDNumber(self.widget1)
        self.lcdVoltage.setObjectName(_fromUtf8("lcdVoltage"))
        self.lcdLayout.addWidget(self.lcdVoltage)
        self.lcdIntensity = QtGui.QLCDNumber(self.widget1)
        self.lcdIntensity.setObjectName(_fromUtf8("lcdIntensity"))
        self.lcdLayout.addWidget(self.lcdIntensity)
        self.lcdPower = QtGui.QLCDNumber(self.widget1)
        self.lcdPower.setObjectName(_fromUtf8("lcdPower"))
        self.lcdLayout.addWidget(self.lcdPower)

        self.retranslateUi(Speedo)
        QtCore.QMetaObject.connectSlotsByName(Speedo)

    def retranslateUi(self, Speedo):
        Speedo.setWindowTitle(QtGui.QApplication.translate("Speedo", "Speedo", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setText(QtGui.QApplication.translate("Speedo", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.rotations.setText(QtGui.QApplication.translate("Speedo", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.voltageLabel.setText(QtGui.QApplication.translate("Speedo", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.intensityLabel.setText(QtGui.QApplication.translate("Speedo", "Intensity", None, QtGui.QApplication.UnicodeUTF8))
        self.power.setText(QtGui.QApplication.translate("Speedo", "Power", None, QtGui.QApplication.UnicodeUTF8))

