import unittest

class test(unittest.TestCase):

    def test_equal(self):
        val = 4
        self.assertEqual(val, 4)

    def test_neg(self):
        firstvalue = 'geeks'
        secondvalue = 'geeks'

        message = 'first value and second val are not equal'

        self.assertEqual(firstvalue , secondvalue, message)

    def test_po(self):
        first = 'geeks'
        second = "geeks"

        message = "first value and second val are not equal"

        #self.assertEqual(first, second, message)
        #self.assertTrue(first, second, message)
        #self.assertFalse(first, second, message)
        self.assertIs(first, second, message)


    
if __name__ == "__main__":
    unittest.main()