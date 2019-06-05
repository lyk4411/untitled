

aa = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6},{'a':1, 'b':2,  'd':4, 'f':6},
      {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},{'a':1, 'b':2,  'd':4, 'e':5, 'f':6}]
vec = ['a','c','e','f']
print([[(word in f and f[word] or 0) for word in vec] for f in aa])

from numpy import *
l1 = [[1,2,3],[4,5,6]]
print(l1)
m1 = matrix(l1)
print(m1)

m2=[[1,2],[3,4],[5,6]]
print(m1 * m2)

print("shape(m1):",shape(m1))
print("shape(m2):",shape(m2))

a1 = m1.A
a2 = array([[1,2,3],[1,2,3]])

print(a1 * a2)