# 代码 2

class Desc(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print("__get__...")
        print('name = ', self.name)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc('x')

    def __init__(self):
        self.y = Desc('y')

if __name__ == '__main__':
    t = TestDesc()
    t.x
    t.y

