# Example of implementing an inlined-callback function

# Sample function to illustrate callback control flow

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

# Inlined callback implementation
from queue import Queue
from functools import wraps

class Async:
    __slots__ = ['func','args']
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        # print('result_queue.get():', result_queue.get())
        while True:

            # print('before result_queue.get():', result)

            result = result_queue.get()
            # print('after result_queue.get():', result)
            # print('result:', result)
            try:
                a = f.send(result)
                # print('after send result: ', result)
                # print('after send a: ', a)
                # print('after send f: ', f)

                # print('f: ', f, ' result: ', result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

# Sample use
def add(x, y):
    return x + y

@inlined_async
def Htest():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')

if __name__ == '__main__':
    # Simple test
    print('# --- Simple test')
    Htest()

    # print('# --- Multiprocessing test')
    # import multiprocessing
    # pool = multiprocessing.Pool()
    # apply_async = pool.apply_async
    # Htest()

