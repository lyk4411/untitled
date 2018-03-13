def h():
    print ('Wen Chuan')
    m = yield 5  # Fighting!
    print (m)
    d = yield 12
    print ('We are together!')


c = h()
#print(c.send(None))
m = c.__next__()
d = c.send("Fighting......")

print('we will not forget the data  ..... ',m,' and ',d)

#print(c.send("hello world."))