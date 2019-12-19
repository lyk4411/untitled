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