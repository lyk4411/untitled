class Dict(dict):
    '''
    通过使用__setattr__,__getattr__,__delattr__
    可以重写dict,使之通过“.”调用
    '''

    def __setattr__(self, key, value):
        print("In '__setattr__")
        self[key] = value

    def __getattr__(self, key):
        try:
            print("In '__getattr__")
            return self[key]
        except KeyError as k:
            return None

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            return None

    # __call__方法用于实例自身的调用,达到()调用的效果
    def __call__(self, key):  # 带参数key的__call__方法
        try:
            print("In '__call__'")
            return self[key]
        except KeyError as k:
            return "In '__call__' error"


s = Dict()
print(s.__dict__)
# {}

s.name = "hello"  # 调用__setattr__
# In '__setattr__

print(s.__dict__)  # 由于调用的'__setattr__', name属性没有加入实例属性字典中。
# {}

print(s("name"))  # 调用__call__
# In '__call__'
# hello

print(s["name"])  # dict默认行为
# hello

print("======================================")
print(s.__dict__)

# print(s)
print(s.name)  # 调用__getattr__
# In '__getattr__
# hello

del s.name  # 调用__delattr__
print(s("name"))  # 调用__call__
# None