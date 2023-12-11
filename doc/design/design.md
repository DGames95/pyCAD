# Design

## general structure
build a simple vertical structure leaving each part open for extension as much as possible. 
try an MVP like creating a cube using extrude tool and render to obj file format

## follow file formats
logically common file formats will contain all geometry info in a structured way. So we can draw inspiration from these (and must support them)

STEP for 3D geometry and 
DXF for sketches (nice to have)

obj and stl focus on vertexes and faces whereas step follows the mathematical defintiions more closely. 
DXF

## Pattern
what cointains state? 

should items contain methods for all tools? e.g. item.extrude(vector, distance) or tools.extrude(item, (vector, distance))
extensibility vs simplicity? hybrid?

should items be aware that they are selected? or should that only be tracked in the document?

## logic questions
How to manage dependent values? reference? copy?

warn users if changes affect multiple entities

## Topology

Delaunay triangulation

point to point = edge

how to tell if a group of edges is enclosed to make a face?:
same plane

how to tell if a group of faces forms a solid?:

well, how does obj do it?

v = vertex, f = vertexes

### Outline

documents contain any objects

camera object must be added to each document for 3D view

each item contains it's own position data

base types: vector, point, plane etc. 

primitives = predefined shapes 2D and 3D

sketch = points, lines, curves
solids
part = multiple contiguous solids

assembly = parts constrained together
