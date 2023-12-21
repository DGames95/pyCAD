# The main init of the pyCAD package
# define all items that should be outwardly accessible

from .app.app import App  # main application
from .app.units import Units  # Enum used for converting units to mm
from .config import CADConfig

from .cad_kernel.sketch import geometry2 as Geom2D
from .cad_kernel.part import geometry3 as Geom3D

#


# here is defined what is accessible when importing the package with * only keep necesary public elements
__all__ = []