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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "GTFS Importer"


def description():
    return "Import GTFS data to QGIS"


def version():
    return "Version 1.0"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Maungu Oware"

def email():
    return "oware@appliedgeo.org"

def classFactory(iface):
    # load GtfsImporter class from file GtfsImporter
    from gtfsimporter import GtfsImporter
    return GtfsImporter(iface)
