# 执行测试的类
from beginPython.ch16.widget import Widget


class TestWidget:
    def testSize(self):
        expectedSize = (40, 40);
        widget = Widget()
        if widget.getSize() == expectedSize:
            print ("test [Widget]: getSize works perfected!")
        else:
            print ("test [Widget]: getSize doesn't work!")
# 测试
if __name__ == '__main__':
    myTest = TestWidget()
    myTest.testSize()