# 代码 1

class Desc(object):
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class aDesc(object):
    x = Desc()


if __name__ == '__main__':
    t = aDesc()
    t.x

# 以下为输出信息：
