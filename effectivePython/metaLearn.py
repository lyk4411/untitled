class LowercaseMeta(type):
    """ 修改类的属性名称为小写的元类 """
    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'):    # 排除magic method
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v
        return type.__new__(mcs, name, bases, lower_attrs)


class LowercaseClass(metaclass=LowercaseMeta):
    BAR = True

    def HELLO(self):
        print('hello')

print(dir(LowercaseClass))    # 你会发现"BAR"和"HELLO"都变成了小写
LowercaseClass().hello()


class ListMeta(type):
    """ 用元类实现给类添加属性 """
    def __new__(mcs, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(mcs, name, bases, attrs)

class MyList(list, metaclass=ListMeta):
    pass

l = MyList()
l.add(1)
print(l)
l.append(2)
print(l)


def class_decorator(cls):
    cls.add = lambda self, value: self.append(value)
    return cls

@class_decorator
class MyList(list):
    pass


l = MyList()
l.append(1)
print(l)
l.append(2)
print(l)


class LazybonesError(BaseException):
    """ 给懒虫们的提示 """
    pass


class MustHaveDocMeta(type):
    def __init__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith('__'):    # skip magic or private method
                continue
            if not callable(attr_value):    # skip non method attr
                continue
            if not getattr(attr_value, '__doc__'):
                raise LazybonesError(
                    'Hi Lazybones, please write doc for your "{}" method'.format(attr_name)
                )
        type.__init__(cls, name, bases, attrs)


class ClassByLazybones(metaclass=MustHaveDocMeta):
    """ 这个类的定义是无法通过的，直接会报异常，让你不给方法写docstring """
    def complicate(self):
        """
        :return:
        """
        pass