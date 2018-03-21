import unittest

# 执行测试的类
from beginPython.ch16.widget import Widget


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

    def suite(self):
        return WidgetTestSuite()


class WidgetTestSuite(unittest.TestSuite):
    def __init__(self):
        unittest.TestSuite.__init__(self, map(WidgetTestCase,
                                              ("testSize",
                                               "testResize")))



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestSuite)

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)