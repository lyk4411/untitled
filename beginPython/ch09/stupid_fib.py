import random
import time


def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b  # yield把结果b从函数扔出去，返回值用send接收过来
        print('让我思考{0}秒'.format(sleep_cnt))
        time.sleep(sleep_cnt)
        a, b = b, a + b
        index += 1


print('-' * 10 + 'test yield send' + '-' * 10)
sfib = stupid_fib(10)
fib_res = sfib.__next__()  # 相当于sfib.send(None)
while True:
    print(fib_res)
    print("=======")
    try:
        fib_res = sfib.send(random.uniform(0, 0.5))
    except StopIteration:
        break
