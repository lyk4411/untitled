class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

    def __getattribute__(self, attr):
        return('invoke __getattribute__', attr)


insA = ClassA('ClassA')
print(insA.__dict__)
# ('invoke __getattribute__', '__dict__')

print(insA.classname)
# ('invoke __getattribute__', 'classname')

print(insA.grade)
# ('invoke __getattribute__', 'grade')

print(insA.__dict__)
