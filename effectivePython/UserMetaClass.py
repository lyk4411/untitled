

class Field:
    """ 负责保存数据库表的字段名和字段类型 """
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


# 编写ModelMetaclass元类
class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        if name == 'Model':
            return type.__new__(mcs, name, bases, attrs)
        print('Found model: %s' % name)

        mappings = {}    # 保存field
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, Field):
                print('Found maping: %s ==> %s' % (attr_name, attr_value))
                mappings[attr_name] = attr_value

        for k in mappings.keys():
            attrs.pop(k)    # 去除field属性

# 把所有的Field移到__mappings__里，防止实例的属性覆盖类的同名属性
        attrs['__mappings__'] = mappings
        attrs['__tablename__'] = name.lower()  # 使用类名小写作为表名
        return type.__new__(mcs, name, bases, attrs)


# 编写基类Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):    # 为了实现可以用"."访问属性
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, k, v):
        self[k] = v

    def save(self):
        fields = []
        params = []
        args = []

        for field_name, field in self.__mappings__.items():
            fields.append(field.name)
            params.append('?')
            args.append(getattr(self, field_name, None))

# 拼成sql语句
        sql = 'inset into %s (%s) values (%s)' % (
            self.__tablename__, ','.join(fields), ','.join(params)
        )
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# python3.5
class User(Model):
    id = IntegerField('id')
    name = StringField('name')

u = User(id=1, name='laowang')
u.save()

""" 输出如下
Found model: User
Found maping: id ==> <IntegerField:id>
Found maping: name ==> <StringField:name>
SQL: inset into user (id,name) values (?,?)
ARGS: [1, 'laowang']
"""