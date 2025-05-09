# -*- coding: utf-8 -*-

"""
/***************************************************************************
 VROOM_for_QGIS
                                 A QGIS plugin
 This plugin makes it possible to send data from a QGIS layer to VROOM.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2025-04-21
        copyright            : (C) 2025 by Suddber
        email                : suddb@posteo.de
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

__author__ = 'Suddber'
__date__ = '2025-04-21'
__copyright__ = '(C) 2025 by Suddber'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .vroom_for_qgis_algorithm import VROOM_for_QGISAlgorithm


class VROOM_for_QGISProvider(QgsProcessingProvider):

    def __init__(self):
        
        QgsProcessingProvider.__init__(self)

    def unload(self):
        
        pass

    def loadAlgorithms(self):
        
        self.addAlgorithm(VROOM_for_QGISAlgorithm())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        
        return 'VROOM for QGIS'

    def name(self):
        
        return self.tr('VROOM for QGIS')

    def icon(self):
        
        return QgsProcessingProvider.icon(self)

    def longName(self):
        
        return self.name()
