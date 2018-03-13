class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

insA = ClassA('ClassA')

print(insA.__dict__)
# {'classname': 'ClassA'}

insA.tag = 'insA'

print(insA.__dict__)
# {'tag': 'insA', 'classname': 'ClassA'}