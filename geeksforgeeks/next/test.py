import unittest
import main

class checkstrings(unittest.TestCase):

    def test_string(self):
        first_val = "dig"
        second_val = "gibyte"
        message=  "not equal "
        result = main.check(first_val, second_val)
        self.assertIn(result, "diggibyte", message)

    def test_string1(self):
        first_val = "di"
        second_val = "gibyte"
        message=  "not equal "
        result = main.check(first_val, second_val)
        self.assertNotIn(result, "diggibyte", message)

    def test_sum(self):
        a = 10
        b = 20
        result = main.check2(a, b)
        self.assertEqual(result, 30)

    def test_sum2(self):
        a = 10
        b = 30
        result = main.check2(a, b)
        self.assertNotEqual(result, 10)



if __name__ == "__main__":
    unittest.main()