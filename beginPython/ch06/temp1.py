import re
inputStr = "hello crifan, nihao crifan";
print(re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr))

inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
print ("replacedStr=",replacedStr) #crifan


def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456";

    def _add111(matched):
        intStr = matched.group("number"); #123
        intValue = int(intStr);
        addedValue = intValue + 111; #234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr);
    print ("replacedStr=",replacedStr) #hello 234 world 567

###############################################################################
if __name__=="__main__":
    pythonReSubDemo();




def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789";

    def _add111(matched):
        intStr = matched.group("number"); #123
        intValue = int(intStr);
        addedValue = intValue + 111; #234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr, 2);
    print ("replacedStr=",replacedStr) #hello 234 world 567 nihao 789

###############################################################################
if __name__=="__main__":
    pythonReSubDemo();