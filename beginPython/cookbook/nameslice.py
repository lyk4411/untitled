a = slice(5, 50, 2)
print(a.start)
s = 'helloworld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])

