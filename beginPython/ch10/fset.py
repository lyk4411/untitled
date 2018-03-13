a = set(range(4))
b = set(range(2,6))
print(a)
print(b)
a.add(frozenset(b))
print(a)

print(frozenset(range(4)))