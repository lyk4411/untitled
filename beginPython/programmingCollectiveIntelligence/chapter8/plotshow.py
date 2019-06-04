#
# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1 ,11)
# y =  2  * x +  5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x ,y)
# plt.show()


from pylab import *

from beginPython.programmingCollectiveIntelligence.chapter8 import numpredict

a = array([1,2,3,4])
b = array([4,3,2,1])
plot(a,b)
show()
t1 = arange(0.0, 10.0, 0.1)
plot(t1, sin(t1))
show()

