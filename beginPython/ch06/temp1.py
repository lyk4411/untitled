import re
inputStr = "hello crifan, nihao crifan";
print(re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr))