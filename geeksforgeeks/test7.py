import unittest
from unittest import result

def sum(a, b):
    return a+b


class sumtest(unittest.TestCase):

    def test_sumfunc_1(self):

        #Arrange
        a = 10
        b = 20

        #Act
        result = sum(a,b)

        #assert
        self.assertEqual(result, a+b)


    def test_sumfunc_2(self):

        #Arrange
        a = 10
        b = 20

        #Act
        result = sum(b,a)

        #assert
        self.assertEqual(result, a+b)



if __name__=="__main__":
    unittest.main()