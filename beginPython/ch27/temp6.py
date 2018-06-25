from xmlrpc.client import ServerProxy

mypeer = ServerProxy('http://localhost:4243')
# mypeer.hello('http://127.0.0.1:4243')

code,data = mypeer.query('test.txt')
print(code)
print(data)

code,data = mypeer.query('temp1.py')
print(code)
print(data)


# print(mypeer.fetch('test.txt',123456))

