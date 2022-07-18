import unittest

def add(x, y):
    return x+y

class testing(unittest.TestCase):

    def teststring(self):
        sub = "diggi"
        container = "diggibyte"
        self.assertIn(sub, container, "not equal")

    def teststring1(self):
        self.assertEqual(add(4,5),9)

    def testvl(self):
        self.assertNotEqual(add(4,5),10)

    def testv2(self):
        sub = "geek"
        container="geeksforgeeks"
        self.assertIsNot(sub, container, "not equal")



    

if __name__ =="__main__":
    unittest.main() 
