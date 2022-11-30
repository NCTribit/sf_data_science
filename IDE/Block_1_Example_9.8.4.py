import numpy as np


a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])


def check_parallel(vec1, vec2):
    print(vec1, vec2)
    if np.linalg.norm(vec1) + np.linalg.norm(vec2) == np.linalg.norm(vec1 + vec2):
        return True
    else:
        return False
    

print(check_parallel(a, b))
print(check_parallel(b, c))
print(check_parallel(c, a))
    
    
def norm_dif_more_100(vec1, vec2):
    print(vec1, vec2)
    if np.linalg.norm(vec1 - vec2) > 100:
        return True
    else:
        return False

    
print(norm_dif_more_100(a, b))
print(norm_dif_more_100(b, c))
print(norm_dif_more_100(c, a))


def check_perpend(vec1, vec2):
    print(vec1, vec2)
    if np.dot(vec1, vec2) == 0:
        return True
    else:
        return False
    
    
print(check_perpend(a, b))
print(check_perpend(b, c))
print(check_perpend(c, a))