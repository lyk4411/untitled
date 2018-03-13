

class ClassA(object):
    def __init__(self, classname):
        self.classname = classname

    def __setattr__(self, name, value):
        # self.name = value  # 如果还这样调用会出现无限递归的情况
        print('invoke __setattr__')


insA = ClassA('ClassA') # __init__中的self.classname调用__setattr__。
# invoke __setattr__

print(insA.__dict__)
# {}

insA.tag = 'insA'
# invoke __setattr__

print(insA.__dict__)
# {}