a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

from copy import deepcopy
c = deepcopy(a)
print(c)
print(c[2])
print(c[2][0])
print(c[2][0][2])
d = c[2][0][2]