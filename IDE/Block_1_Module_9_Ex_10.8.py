import numpy as np


vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
def min_max_dist(*vectors):
    min = None
    max = None
    for i in range(len(vectors)):
        # print('f ', i)
        for j in range(i+1, len(vectors)):
            # print('s ', j)
            if min is None:
                min = np.linalg.norm(vectors[i] - vectors[j])
            elif min > np.linalg.norm(vectors[i] - vectors[j]):
                min = np.linalg.norm(vectors[i] - vectors[j])
            if max is None:
                max = np.linalg.norm(vectors[i] - vectors[j])
            elif max < np.linalg.norm(vectors[i] - vectors[j]):
                max = np.linalg.norm(vectors[i] - vectors[j])
    return(min, max)


def min_max_dist_v2(*vectors):
    dists = list()
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            dists.append(np.linalg.norm(vectors[i] - vectors[j]))
    return min(dists), max(dists)


print(min_max_dist(vec1, vec2, vec3))