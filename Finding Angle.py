import numpy as np
import vg
import itertools


vec1 = np.array([1,1, 1])
vec2 = np.array([1,1,0])

vec_concat = np.hstack((vec1, vec2))


l = [1,-1]
comb = np.array(list(itertools.product(l, repeat=vec_concat.shape[0])))

vec_comb = np.einsum('i, ji -> ji', vec_concat, comb)
angle_comb = vg.angle(vec_comb[:,:3], vec_comb[:, 3:])
print(angle_comb)


