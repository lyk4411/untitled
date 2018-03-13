def fun2():
     print ('first')
     yield 5
     print ('second')
     yield 23
     print ('end...')


g1 = fun2()
print(g1.__next__())
print(g1.__next__())
print(g1.__next__())

