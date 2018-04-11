from xmlrpc.client import ServerProxy

mypeer = ServerProxy('http://127.0.0.1:4242')
mypeer.hello('http://127.0.0.1:4243')

code,data = mypeer.query('test.txt')
print(code)
print(data)

print(mypeer.fetch('test.txt',123456))

