def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))

print("*"*200)


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))
print("*"*20)
print(g.send(7))
print("*"*20)
print(g.send(7))