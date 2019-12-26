def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)

from inspect import isgeneratorfunction
print(isgeneratorfunction(fab))

print("================================================================")

def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2


# 使用for循环
print(list(yield_test(2)))
print("================================================================")

for i in yield_test(5):
    print(i, ",")

print("================================================================")
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)
print("================================================================")
