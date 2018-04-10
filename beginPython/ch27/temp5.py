from xmlrpc.client import ServerProxy
s =ServerProxy('http://localhost:4242')
print(s.twice(2))
print(s.twice(20))
print(s.twice(200))