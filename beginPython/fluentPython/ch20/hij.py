class Desc(object):
    def __init__(self, name):
        self.name = name
        print("__init__(): name = ", self.name)

    def __get__(self, instance, owner):
        print("__get__() ...")
        return self.name

    def __set__(self, instance, value):
        self.value = value


class ATestDesc(object):
    _x = Desc('x')

    def __init__(self, x):
        self._x = x


if __name__ == '__main__':
    t = ATestDesc(10)
    t._x
    print(t.__dict__)
    print(ATestDesc.__dict__)

