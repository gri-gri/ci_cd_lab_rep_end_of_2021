import unittest
from main import Point, Field


class TestPointClassMethods(unittest.TestCase):
    def test_create_empty(self):
        a = Point()
        self.assertEqual(a.x, None)
        self.assertEqual(a.y, None)
    
    def test_create_valid(self):
        a = Point(x=4, y=5)
        self.assertEqual(a.x, 4)
        self.assertEqual(a.y, 5)
    
    def test_create_invalid(self):
        with self.assertRaises(ValueError):
            a = Point("fsd")

class TestFieldClassMethods(unittest.TestCase):
    class DummyPoint:
        pass

    class StubPoint(Point):
        def __init__(self):
            self.x = 4
            self.y = 5

    class FakePoint(Point):
        def __init__(self):
            self.x ,self.y = input("Input x and y for dot:").split()

    def test_creating_empty(self):
        a = Field([])
        self.assertEqual(a.field, [])
    
    def test_creating_with_dummy(self):
        dum = self.DummyPoint()
        a = Field([dum])
        self.assertEqual(a.field, [dum])
    
    def test_creating_with_one_point(self):
        stub = self.FakePoint()
        a = Field([stub])
        self.assertEqual(a.field, [stub])





if __name__ == "__main__":
    unittest.main()
