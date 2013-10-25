# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GtfsImporter
                                 A QGIS plugin
 Convert GTFS data to shapefile
                              -------------------
        begin                : 2013-10-16
        copyright            : (C) 2013 by Maungu Oware
        email                : oware@appliedgeo.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from gtfsimporterdialog import GtfsImporterDialog


class GtfsImporter:
    
    def __init__(self, iface):
        self._iface = iface
        
    def initGui(self):
        self._action = QAction(QIcon(":/plugins/GtfsImporter/icon.png"),
        "Gtfs Importer", self._iface.mainWindow())
        self._action.setWhatsThis("Convert Gtfs data to shapefile")
        QObject.connect(self._action, SIGNAL("activated()"), self.run)
        self._iface.addPluginToMenu("&Gtfs Importer", self._action)
        
    def unload(self):
        self._iface.removePluginMenu("&Gtfs Importer", self._action)
        
    def run(self):
        try:
            dlg = GtfsImporterDialog(self._iface)
            dlg.exec_()
        finally:
            pass
