from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
print(q)
q.rotate(3)
print(q)
q.rotate(-1)
print(q)

q.rotate(4)
print(q)


