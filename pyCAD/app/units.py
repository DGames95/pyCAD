"""
Units enums for conversion of units to mm and radian. use: Units.Length.mm.value to get the conversion factor for mm
"""

from enum import Enum

class Units:
    class Length(Enum):
        """Enum for unit conversion with mm as base unit for length"""
        mm = 1
        cm = 10
        m = 1000
        km = 1000000
        um = 0.001
        inch = 25.4
        ft = 304.8
        yd = 914.4
        mile = 1609344
        mil = 0.0254

    class Angle(Enum):
        """Enum for unit conversion with radian as base unit for angle"""
        rad = 1
        deg = 0.0174533
        grad = 0.0157079
        arcmin = 0.000290888
        arcsec = 0.00000484814
        