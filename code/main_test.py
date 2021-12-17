import pytest
from code.main import Point, Field


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
