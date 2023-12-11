## Events

We want a smart way to propagate changees throughout any model

every part after a part depends on the previous geometry. so they need to be notified of changes. 

Also, if we update a constraint or tool, we might want the renderer to automatically update. 

Similarly for the camera, if we input movement we want the camera to update its position and render new image

## Defining objects in multiple ways

we need a way to define objects in different ways.

e.g. line can be between two points, a point, direction and magnitude, a single point (and origin).

simplest solution is a builder pattern that just always convert it to a single form. However, that means it will not always be updated
second way is to do it in class and just have different classes for each, then pass the dependents by reference. 

else, a data structure is needed to track the relationships between all the objects.
