import random
from time import  *
date1 = (2008,1,1,0,0,0,-1,-1,-1)
date2 = (2009,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
time2 = mktime(date2)

print(random.random())
print(time2)
rt = random.uniform(time1,time2)
print(rt)