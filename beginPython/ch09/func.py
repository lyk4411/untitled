import time

def func(n):
    for i in range(0, n):
        arg = yield i
        print('func:', arg)

f = func(5)
while True:
    print('main:', next(f))
    print('send_func:', f.send(100))
    time.sleep(1)
    print("==================")