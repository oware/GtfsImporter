# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GtfsImporterDialog
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import sys
import os.path
import zipfile

from ui_gtfsimporter import Ui_GtfsImporter


class GtfsImporterDialog(QDialog, Ui_GtfsImporter):
    
    browsePathSetting="/plugins/GtfsImporter/"
    
    def __init__(self, iface):
        QDialog.__init__(self)
         # Save reference to the QGIS interface
        self.iface = iface
        
        settings = QSettings()
        self._home = settings.value(GtfsImporterDialog.browsePathSetting).toString()
        
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Signals
        QObject.connect(self.browseGtfs, SIGNAL("clicked()"), self._browseGtfsFile)
        QObject.connect(self.buttonBox, SIGNAL("accepted()"), self._importVector)
        
    def _browseGtfsFile(self):
        self._gtfsfile = QFileDialog.getOpenFileName(self,"Select GTFS.zip file",
            self._home, "GTFS files (*.zip);;All files (*.*)")
        if self._gtfsfile:
            self.gtfsFile.setText(self._gtfsfile)
            
    def _importVector(self):
        """
        Reads gtfs zip, extracts files and loads vector layers
        """
        _zipname = str(self.gtfsFile.text())
        if _zipname:
            _zip = zipfile.ZipFile(_zipname, "r")
            for filename in _zip.namelist():
                if filename == 'stops.txt':
                    _zip.extract(filename)
                    stops_txt = os.path.abspath(filename)
                    uri = stops_txt + "?delimiter=%s&xField=%s&yField=%s" % (",", "stop_lon", "stop_lat")
                    vl = self.iface.addVectorLayer(uri, "stops", "delimitedtext")
                elif filename == 'shapes.txt':
                    # Write shapes layer
                    shapes_txt = _zip.open(filename, "r")
                    #QMessageBox.information(self, "Info", str(len(shapes_txt.readlines())))
                    # Add fields
                    fields = { 0 : QgsField("shape_id", QVariant.String)}
                    
                    # Create vector file writer
                    writer = QgsVectorFileWriter("shapes.shp", "CP1250", fields, QGis.WKBLineString, None, "ESRI Shapefile")
                    
                    # Get shape_ids
                    shape_ids = []
                    for line in shapes_txt:
                        if 'shape_id' not in line:
                            line_ = line.split(',')
                            shape_ids.append(line_[0])
                    shape_ids_ = set(shape_ids)
                    #QMessageBox.information(self, "Info", str(len(shape_ids_)))
                    
                    # Add polyline
                    shapes = shapes_txt.readlines()
                    for shapeid in shape_ids_:
                        polyline = []
                        for line in shapes:
                            if 'shape_id' not in line:
                                line_ = line.split(',')
                                if line_[0] == shapeid:
                                    polyline.append(QgsPoint(float(line_[2]), float(line_[1])))
                                    
                        fet = QgsFeature()
                        fet.setGeometry(QgsGeometry.fromPolyline(polyline))
                        fet.addAttribute(0, QVariant(shapeid))
                        writer.addFeature(fet)
                    del writer
                    
                    # Load layer
                    v2 = self.iface.addVectorLayer("shapes.shp", "shapes", "ogr")
                    
                else:
                    pass
                    
        
