import re

a1 = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
        r'static PyObject*\npy_\1(void)\n{',
        'def myfunc():')

print(a1)


def dashrepl(matchobj):
     if matchobj.group(0) == '-':
         return ' '
     else:
         return '-'

print(re.sub('-{1,2}', dashrepl, 'pro------gram-files'))

print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

inputStr = "hello crifan, nihao crifan";
print(re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr))
print(re.sub(r"crifan", "crifanli", inputStr))

replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
print ("replacedStr=",replacedStr)


import re;

def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";

    def _add111(matched):
        intStr = matched.group(1); #123
        # intStr = matched.group("number");  # 分组名：number
        intValue = int(intStr);
        addedValue = intValue + 111; #234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(\d+)", _add111, inputStr, 2);
    # replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr);
    print ("replacedStr=",replacedStr) ##hello 234 world 567

###############################################################################
if __name__=="__main__":
    pythonReSubDemo();