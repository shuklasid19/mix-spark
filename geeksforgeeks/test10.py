import unittest

class Test():
    pass

class Test1():
    pass


class learnunittest(unittest.TestCase):



    def test_sample(self):
        t1 = Test()
        t2 = t1
        self.assertIs(t1, t2)
        #because of same instance 

    def test_sample1(self):
        t1 = Test()
        t2 = Test()
        self.assertIsNot(t1, t2)
        #2 different instances 

    def test_sample2(self):
        t1 = Test()
        t2 = Test()
        self.assertIs(t1, t2)
        #2 different instances 
    
    def test_sample3(self):
        t1 = Test()
        t2 = Test()
        self.assertIsNot(t1, Test1, msg="instance mismatch")
        #2 different instances  
   



if __name__ == "__main__":
    unittest.main() 