import unittest

def add(x, y):
    return x+y

class simpletest(unittest.TestCase):
    def test_add1(self):
        self.assertEquals(add(4, 5), 9)


if __name__ == "__main__":
    unittest.main()