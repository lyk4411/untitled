from xmlrpc.client import ServerProxy
from xmlrpc.server import *

mypeer = ServerProxy('http://127.0.0.1:4243')
code,data = mypeer.query('test.txt')
print(code)
print(data)