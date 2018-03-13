from pip._vendor.distlib.compat import raw_input
import sys
a = ()
b = 1
c = 2
d = a + (b,)
print(d)
d = d + (c,)
print(d)
d = d + (c,)
print(d)