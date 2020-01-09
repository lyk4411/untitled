class Student():
    def __init__(self, name):
        print("Student init")
        super(Student, self).__init__()

if __name__ == "__main__":
    s1 = Student("XIAOMIN")
    s1.english =90


class Person(object):
    __slots__ = ('_name', '_age', '_sex')  ##限制基类变量只能有这三个属性，实例对象无法增加新的属性，这就防止了用户误输入

    def __init__(self, name):
        self._name = name
        print("Person init")


class Student(Person):
    __slots__ = ('_grade', '_english', '_chinese')  ##限制基类变量只能有这三个属性，实例对象无法增加新的属性，这就防止了用户误输入

    def __init__(self, name):
        print("Student init")
        # Person.__init__(self, name)
        super(Student, self).__init__(name)

    @property  ##property 方法访问变量
    def english(self):
        return self._english

    @english.setter  ##property 方法设置变量，这里面对参数进行了校验
    def english(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数才行呐')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._english = value


if __name__ == "__main__":
    s1 = Student("XIAOMIN")
    p1 = Person("lll")
    # p1.aaa = 1

class anmon(object):
    '''
    this is doc.
    '''
    def __init__(self, name):
        self._name = name
        print("anmon init")

    def anon_a(self):
        self.anon_a = 'aaaa'

if __name__ == "__main__":
    print(anmon.__dict__)
    a2 = anmon('xiaoli')
    print(a2.__dict__)
    a2.anon_a()
    print(a2.__dict__)


class anmon(object):
    '''
    this is doc.
    '''

    def __init__(self, name):
        self._name = name
        print("anmon init")

    def anon_a(self):
        self.anon_a = 'aaaa'


if __name__ == "__main__":
    a2 = anmon('xiaoli')
    print(dir(anmon))
    print(dir(a2))

