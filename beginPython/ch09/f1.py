import time


def func(n):
    for i in range(0, n):
        arg = yield i
        print('func:', arg)

f = func(10)
#print(f.__next__())

while True:
    print('main:', f.__next__())
    print('main:', f.send(100))
    time.sleep(1)
    print("=================")