def minimize():
    current = yield
    while True:
        value = yield current
        print("inner value:", value)
        print("inner current:", current)
        current = min(value, current)

it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))