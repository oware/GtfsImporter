# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gtfsimporter.ui'
#
# Created: Thu Oct 17 06:13:07 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GtfsImporter(object):
    def setupUi(self, GtfsImporter):
        GtfsImporter.setObjectName(_fromUtf8("GtfsImporter"))
        GtfsImporter.resize(492, 148)
        self.buttonBox = QtGui.QDialogButtonBox(GtfsImporter)
        self.buttonBox.setGeometry(QtCore.QRect(140, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gtfsLabel = QtGui.QLabel(GtfsImporter)
        self.gtfsLabel.setGeometry(QtCore.QRect(10, 30, 111, 17))
        self.gtfsLabel.setObjectName(_fromUtf8("gtfsLabel"))
        self.gtfsFile = QtGui.QLineEdit(GtfsImporter)
        self.gtfsFile.setGeometry(QtCore.QRect(130, 20, 251, 27))
        self.gtfsFile.setObjectName(_fromUtf8("gtfsFile"))
        self.browseGtfs = QtGui.QPushButton(GtfsImporter)
        self.browseGtfs.setGeometry(QtCore.QRect(390, 20, 93, 27))
        self.browseGtfs.setObjectName(_fromUtf8("browseGtfs"))
        self.label = QtGui.QLabel(GtfsImporter)
        self.label.setGeometry(QtCore.QRect(10, 70, 131, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(GtfsImporter)
        self.checkBox.setGeometry(QtCore.QRect(150, 70, 96, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(GtfsImporter)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 70, 96, 22))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.retranslateUi(GtfsImporter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GtfsImporter.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GtfsImporter.reject)
        QtCore.QMetaObject.connectSlotsByName(GtfsImporter)

    def retranslateUi(self, GtfsImporter):
        GtfsImporter.setWindowTitle(QtGui.QApplication.translate("GtfsImporter", "Import GTFS data", None, QtGui.QApplication.UnicodeUTF8))
        self.gtfsLabel.setText(QtGui.QApplication.translate("GtfsImporter", "Input GTFS file", None, QtGui.QApplication.UnicodeUTF8))
        self.browseGtfs.setText(QtGui.QApplication.translate("GtfsImporter", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GtfsImporter", "Features to import", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("GtfsImporter", "Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("GtfsImporter", "Stops", None, QtGui.QApplication.UnicodeUTF8))

