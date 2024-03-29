import unittest
# 执行测试的类
from beginPython.ch16.widget import Widget


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget = None
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
# 构造测试集
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase("testSize"))
    return suite
# 测试
if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')