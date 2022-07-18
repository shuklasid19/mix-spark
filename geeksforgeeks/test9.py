import unittest



class learnunittest(unittest.TestCase):



    def test_sample(self):
        a = 1
        b = 1
        self.assertEqual(a, b)

    def test_sample1(self):
        a = 1
        b = 1
        #self.assertNotEqual(a, b,msg="one a aint equal to b")
        self.assertIs(a,b)

    



if __name__ == "__main__":
    unittest.main() 