import re

st = 'alpha,beta,,,,,,,gamma ,delta'
print(st.split(","))
print(re.split('[,]+',st,maxsplit=3))
print(re.split('[,]+',st,maxsplit=2))
print(re.split('[,]+',st,maxsplit=1))

# print(re.escape('www.python.org'))
# print(re.escape('I\'m fine, thank you, and you?'))

#
# print(re.split('[,]+',st))
#
# print(re.split('o(o)','foobarpp'))

m = re.match(r'www\.(.*)\..{3}','www.python.org')
print(m.group(0))
print(m.group(1))
print(m.span(0))
print(m.span(1))


ep = r'\*([^\*]+?)\*'
str1 = re.sub(ep,r'<em>\1</em>','hello, *wo*r*ld*!')
print(str1)
