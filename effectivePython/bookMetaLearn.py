# 定义Item元类，继承type
class ItemMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)
# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义cellPhone类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


if __name__ == '__main__':
    b = Book("Python基础教程", 89)
    b.discount = 0.76
    # 创建Book对象的cal_price()方法
    print(b.cal_price())
    cp = CellPhone(2399)
    cp.discount = 0.85
    # 创建CellPhone对象的cal_price()方法
    print(cp.cal_price())