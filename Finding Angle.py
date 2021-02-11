import numpy as np
import vg

vec1 = np.array([1, 1, 5])
vec2 = np.array([-1, 1, 2])

angle= vg.angle(vec1, vec2)
print(angle)
