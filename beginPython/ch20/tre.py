import re


def sub_emphasis(match):
    return '<em>%s</em>' % match.group(1)


def sub_url(match):
    print("match.group(0): ",match.group(0))
    print("match.group(1): ",match.group(1))
    return '<a href="%s">%s</a>' % (match.group(1), match.group(1))


def sub_mail(match):
    print("match.group(0): ",match.group(0))
    return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

print(re.sub(r'\*(.+?)\*',sub_url,"*hello, world.*"))
print(re.sub(r'\*(.+?)\*',sub_url,"hello, world."))

text = "JGood isaandsomeboy, heiscool,clever,andoon..."
print(re.sub(r'(\s+)', sub_emphasis, text))




p = re.compile(r'(\w+) (\w+)')
s = 'hello 123, hello 456'


def func(m):
    return 'hi' + ' ' + m.group(2)


print (p.sub(r'hello world', s))  # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
print(p.sub(r'\2 \1', s)) # 引用分组
print(p.sub(func, s))
print(p.sub(func, s, 1))  # 最多替换一次
