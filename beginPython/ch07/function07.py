class Class:
    def method(self):
        print('I have a self.')


def function():
    print('I don''t......')


instance = Class()
instance.method()
Class.method(instance)

instance.method1 = function
instance.method1()
