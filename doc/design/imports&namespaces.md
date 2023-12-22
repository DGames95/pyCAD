# Imports and namespaces

- deciding what to import and in what order is somewhat of a challenge and a bit messy
- folders are going quite deep and certain aspects e.g. geomtery should be brought up to the pyCAD namespace
- balance between ease of use but not confusing error messages where it is hard to know what class you are actually using..


#### here document the namespaces that should be exposed to the user and what is contained to make scripting simple as possible

#### note relative imports
dont use absolute imports within the kernel even though they work in tests
e.g. NOT: from point import Point2D INSTEAD: from .point import Point2D

### Point vs Point2D and Point3D (and other)
within the kernel the distinction between Point2D and 3D is nice but for the user it seems a bit clunky since 
we are just using Geom2D.Point2D already. So it will be imported in this module as Point for now

## pyCAD namespace

classes:

- App

modules:

- Geom2D
- Geom3D

## cad_kernel namespace

classes:

-

modules:

- renderer