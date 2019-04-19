import collections


def flatten(items, ingore_types=(str, bytes)):
    for x in items:
        # isinstance(x, collections.Iterable) 检查是否有某个元素是可迭代的；
        # 如果有，那么就用yield from将这个可迭代对象作为一种子例程进行递归，它将所有的值都产生出来
        if isinstance(x, collections.Iterable) and not isinstance(x, ingore_types):
            # not isinstance(x, ingore_types)是为了避免将字符串和字节串解释为可迭代对象，进而将他们展开为单独的一个个字符
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)


items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):  # 输出了整个字符串(并没有迭代字符串)
    print(x)