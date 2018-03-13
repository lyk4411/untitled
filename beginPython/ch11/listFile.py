f = open(r'F:/Users/lyk/PycharmProjects/untitled/beginPython/ch11/temp.txt','w')
f.write('first line\n')
f.write('second line\n')
f.write('third line\n')
print(f.tell())
f.close()
lines = list(open(r'F:/Users/lyk/PycharmProjects/untitled/beginPython/ch11/temp.txt'))
print(lines)

a,b,c = open(r'F:/Users/lyk/PycharmProjects/untitled/beginPython/ch11/temp.txt')

print(a)
print(b)
print(c)
