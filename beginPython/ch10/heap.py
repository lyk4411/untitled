from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print(heap)

heappush(heap,0.5)
print(heap)
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)



heap = [5,8,9,3,5,0,1,2,5]
heapify(heap)
print(heap)