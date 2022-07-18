#it makes prequisite checks if values are there or not
#setup and teardown make sure prerequisite are avialable
#and to clean before moving on to another values
#flush

import unittest


def sum(a, b):
    return a+b


class sumtest(unittest.TestCase):

    def setUp(self):
        print("im in setup")
        self.a = 20
        self.b = 20


    def tearDown(self):
        print("TEARDOWN called")
        self.a = 0
        self.b = 0


    def test_sumfunc_1(self):
        #Act
        print("test_sumfunc1")
        result = sum(self.a,self.b)
        #assert
        self.assertEqual(result, self.a+self.b)


    def test_sumfunc_2(self):
        print("testsum2")
        #Arrange
        #Act
        result = sum(self.b,self.a)
        #assert
        self.assertEqual(result, self.a+self.b)


if __name__=="__main__":
    unittest.main()