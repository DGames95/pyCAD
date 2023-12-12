## how to manage constraints

I want the sketcher to work without contraints and have a constraint solver directly manipulate the sketch

This way if the contraint solver is too much work a basic sketcher is still availbale and independent.

### Sketch

so each sketch has a sketch tree to represent the items making up the sketch

each item must have an index that can be accessed by the solver

becasue some objects are composed of others those objects must be added to the tree

### Composed Objects

a line will have 2 points which should be accessible from the sketch tree for solving constraints

so if I add a line to the sketch tree a subtree will be made of it's components

what comes to mind is all objects will have a method that decomposes it into the composed objects