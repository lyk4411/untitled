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

# print(re.sub(r'\*(.+?)\*',sub_url,"*hello, world.*"))
print(re.sub(r'\*(.+?)\*',sub_url,"hello, world."))