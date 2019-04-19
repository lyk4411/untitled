from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random
def foo(i):
    print('%s is running %s'%(os.getpid(),i))
    time.sleep(random.randint(1, 3))
    return i**2
if __name__ == '__main__':
    print('cpu_num:',os.cpu_count())
    executor=ProcessPoolExecutor()
    print('executor',executor,type(executor))
    # futures=[]
    # for i in range(10):
    #     future=executor.submit(foo,i)
    #     futures.append(future)
    futures=[executor.submit(foo,i) for i in range(10)]
    executor.shutdown()
    #程序运行到这里有明显的时间间隔，可见是在shutdown存在的情况下，程序将future全部执行完，才继续往下走的
    print('主')
    print(futures)
    for future in futures:
        print(future.result())