import unittest

class Area:
    def __init__(self, width=100, length=100):
        self._width = width
        self._length = length

    def getWidth(self):
        return self._width

    def getLength(self):
        return self._length

    def getArea(self):
        return self._width * self._length

    def setWidth(self, width):
        if width <= 0:
            raise (ValueError, "Illeage Width value")
        self._width = width

    def setLenth(self, length):
        if length <= 0:
            raise (ValueError, "Illeage Length value")
        self._length = length





class AreaTestCase(unittest.TestCase):
    def setUp(self):
        self.area = Area()

    def tearDown(self):
        self.area = None

    def testArea(self):
        self.assertEqual(self.area.getArea(), 10000)

    def testWidth(self):
        self.area.setWidth(10)
        self.assertEqual(self.area.getWidth(), 10)

    def testLength(self):
        self.area.setLenth(10)
        self.assertEqual(self.area.getLength(), 10)


if __name__ == "__main__":
    unittest.main()
