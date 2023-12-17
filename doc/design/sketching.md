## how to manage constraints

I want the sketcher to work without contraints and have a constraint solver directly manipulate the sketch

This way if the contraint solver is too much work a basic sketcher is still availbale and independent.

### Sketch

SketchObject = the thing that exists in 3D
Sketch = the thing tracking the dependencies and constraints

### Composed Objects

a line will have 2 points which should be accessible from the sketch tree for solving constraints

so if I add a line to the sketch tree a subtree will be made of it's components

what comes to mind is all objects will have a method that decomposes it into the composed objects

decided that there will only be one level of dependencies


## Solution and constraint structure

sketch exists on a plane. A sketch stores it's objects in a SketchTree. The sketch also has a solver attached.

The solver tracks the constraints. Each constraint points to each object that is constrained.
When the sketch is updated, it calls the solver. The solver loops through the constraints adding them to a constraint matrix. this is then solved. and the results are returned to the solver. The solver then goes and notifies each constraint and they propagate the change to their objects.

Constraints edit their geometry.

Multiple constraints and degrees of freedom?

### Constraints

15/12: deciding to do explicit constraints. One class for each type with switch statement for all types

### Degrees of freedom

I want objects to be generally oblivious to the solver and constraints.

The solver should also track the degrees of freedom of each object.


### Solution Steps

1. 

### Deletion
Deleting an item with dpeendencies will not delete it's dependencies for now, in case they were in use by something else
e.g. deleting a line will leave it's two points

### Dependency vs dependent

In the app we call things that something depends on dependencies. There are no dependents in the code.
Dependent is the the term for going backwards along the dependency. 

e.g. line is a dependent of points, the points are the dependencies of the line