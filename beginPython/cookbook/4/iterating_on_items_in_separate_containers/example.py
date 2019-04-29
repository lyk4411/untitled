# Example of iterating over two sequences as one

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

print("=============================")
c = set()
d = set()
c.add(1)
c.add(2)
c.add(3)
c.add(4)
d.add(1)
d.add(2)
d.add(3)
d.add(4)
d.add(5)
for x in chain(c, d):
    print(x)
