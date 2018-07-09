from xmlrpc.client import ServerProxy
otherpeer  = ServerProxy('http://127.0.0.1:4242')
otherpeer.hello('http://127.0.0.1:4243')

code,data = otherpeer.query('temp2.py')
print(code)
print(data)
print(otherpeer.fetch('temp2.py', 'ccc'))

# otherpeer.hello('http://127.0.0.1:4242')
# otherpeer.fetch('test.txt','654321')

# C:\Users\lyk\AppData\Local\Programs\Python\Python36> python  F:/Users/lyk/PycharmProjects/untitled/beginPython/ch27/temp1.py http://127.0.0.1:4242 F:\Users\lyk\PycharmProjects\untitled\beginPython\ch27\c ccc

# python  F:/Users/lyk/PycharmProjects/untitled/beginPython/ch27/temp1.py http://127.0.0.1:4243 F:\Users\lyk\PycharmProjects\untitled\beginPython\ch27\a  aaa