from xmlrpc.client import ServerProxy
from xmlrpc.server import *
s = SimpleXMLRPCServer(("",4242))
def twice(x): return x * 2

s.register_function(twice)
s.serve_forever()