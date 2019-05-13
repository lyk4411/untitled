from functools import partial


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop

# Example use
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age
String = partial(typed_property, expected_type = str)
Integer = partial(typed_property, expected_type = int)
class Person1:
    name = String('name')
    age = Integer('age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p = Person('Dave', 39)
    p.name = 'Guido'
    print(p.name)
    try:
        p.age = 'Old'
    except TypeError as e:
        print(e)

    p1 = Person1('Dave', 39)
    p1.name = 'Guido'
    print(p1.name)


