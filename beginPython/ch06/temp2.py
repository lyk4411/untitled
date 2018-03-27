import re,sys

field_pat = re.compile(r'\[(.+?)\]')

scope = {}
def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code,scope))
    except SyntaxError:
        exec (code,scope)
        print("code:"+code)
        return '********'


lines = []
fp = "[x=2]" \
     "[y=3]" \
     "the sum of [x] and [y] is [x+y]"
for line in fp:
    lines.append(line)

text = ''.join(lines)
print(field_pat.sub(replacement,text))
