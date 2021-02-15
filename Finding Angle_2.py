import itertools as it
import numpy as np
import vg

vector1 = np.array([1,1,5])
vector2 = np.array([-1,-1,2])

def vector_variants(vector):
    pairs = [[i, -i] for i in vector]
    return [[i,j,k] for i in pairs[0] for j in pairs[1] for k in pairs[2]]

v1_variants = vector_variants(vector1)
v2_variants = vector_variants(vector2)

combos = np.array(it.product(v1_variants, v2_variants))
angles = [vg.angle(item[0], item[1]) for item in combos]