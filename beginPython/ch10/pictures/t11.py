import re


def Num2A(match):
    return 'A'


a = re.sub(r'(\d+)', Num2A, 'he123he')
print(a)

a = re.sub(r'(\d+)', r'A', 'he123he')
print(a)