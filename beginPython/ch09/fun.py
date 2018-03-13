def fun():
     print ('start...')
     m = yield 5
     print (m)
     print ('middle...')
     d = yield 12
     print (d)
     print ('end...')


m=fun()
print(m.__next__())
m.send('message')

