import unittest
import calc


class test_calc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    
    def test_div(self):
        result = calc.division(10, 2)
        self.assertEqual(result, 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, -1), -2)
        self.assertEqual(calc.subtract(-1, 1), 0)
    
    
    
    def test_division(self):
        self.assertEqual(calc.division(10, 5), 15)
        self.assertEqual(calc.division(-1, 1), 0)
        self.assertEqual(calc.division(-1, -1), -2)
       
    
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(-1, 1), -1)
       


 

if __name__ == "__main__":
    unittest.main()
