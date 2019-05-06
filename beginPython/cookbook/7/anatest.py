names = ['abalajfdlan','hello world','wodemaya','nihao']

print(sorted(names,key = lambda name: name.split()[-1].lower()))

print('abalajfdlan'.split())
print('hello world'.split())
print('hello world'.split()[-1])

funcs = [lambda x : x + n for n in range(5)]
for f in funcs:
    print(f(0))

print("===========================================")
funcs = [lambda x, n = n : x + n for n in range(5)]
for f in funcs:
    print(f(0))