from xmlrpc.client import ServerProxy
otherpeer  = ServerProxy('http://127.0.0.1:4242')
otherpeer.hello('http://127.0.0.1:4243')

# code,data = otherpeer.query('temp2.py')
# print(code)
# print(data)
print(otherpeer.fetch('temp2.py', 'ccc'))

# otherpeer.hello('http://127.0.0.1:4242')
# otherpeer.fetch('test.txt','654321')


