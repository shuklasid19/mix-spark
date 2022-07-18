
import unittest

def calculate_area_traiangle(width, height):
    return width*height


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

"""   
class testarea(unittest.TestCase):
    def test_area(self):
        ractangle = Rectangle(3,2)
        self.assertEqual(ractangle.get_area(), 6, 'incorrect area')

    def test_area(self):
        ractangle = Rectangle(3,2)
        self.assertNotEqual(ractangle.get_area(), 6, 'incorrect area')


class testgetarea2(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(0, 0)

    
    def test_normal_case(self):
        self.rectangle.set_width(2)
        self.rectangle.set_height(4)
        self.assertEqual(self.rectangle.get_area(), 6, "incorrect area")

    def test_neg(self):
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "incorrect negative")


"""
unittest.main()