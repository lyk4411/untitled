
def fib():
    a,b = 0,1
    while 1:
        a,b = b,a+b
        yield a
for f in fib():
    if f < 10000:
        print(f)
    else:
        break