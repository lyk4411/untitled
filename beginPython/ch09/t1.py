import time

def func(n):
    for i in range(0, n):
        arg = yield i
        print('func:', arg)

f = func(5)
print('init:', f.send(None))
while True:
    print('main:', f.send(100))
    time.sleep(1)
    print("===============")