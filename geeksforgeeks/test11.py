import unittest

class Test():
    pass

class Test1():
    pass


class learnunittest(unittest.TestCase):




    def test_sample(self):
        t1 = Test()
        t2 = Test()
        t3 = None
        self.assertIsNot(t3)
        #2 different instances 

    def test_sample2(self):
        t1 = Test()
        t2 = Test()
        t3 = 10
        self.assertIsNotNone(t3)
        #2 different instances 

    def test_sample3(self):
        t1 = Test()
        t2 = Test()
        t3 = 10
        self.assertTrue(t1=t2)
        #2 different instances 

    def test_sample4(self):
        t1 = Test()
        t2 = Test()
        t3 = 10
        self.assertFalse(t1=t1)
        #2 different instances 




if __name__ == "__main__":
    unittest.main() 