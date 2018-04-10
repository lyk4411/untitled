from xmlrpc.client import ServerProxy
from xmlrpc.server import *
otherpeer  = ServerProxy('http://127.0.0.1:4243')
code,data = otherpeer.query('test.txt')
print(code)
print(data)

otherpeer.hello('http://127.0.0.1:4242')
otherpeer.fetch('test.txt','654321')


