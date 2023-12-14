creating wrappers for 2D and 3D geometry that use numpy

2D and 3D are just separate since they are used in separate context reducing complexity

default type for floats will by np.float64: high precision,
favour not to make it configurable because no macros in python

11/12/2023: decide not to make a math module rather just implement bare requirements using numpy, math library is it's own whole thing


### Vectors

So the idea is vector is a wrapper for a numpy array with 2x1 or 3x1 size and extra methods to quickly get x, y, z, translate, etc. 

so when using numpy use vector.data as the vector itself.
