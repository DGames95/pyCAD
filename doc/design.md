# Design

## .obj
lets model design to follow standards in obj file format, to use other renderers

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
