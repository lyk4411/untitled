

aa = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6},{'a':1, 'b':2,  'd':4, 'f':6},
      {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6},{'a':1, 'b':2,  'd':4, 'e':5, 'f':6}]
vec = ['a','c','e','f']
print([[(word in f and f[word]or 0) for word in vec] for f in aa])
