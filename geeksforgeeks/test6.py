#arrange #act #assert
import unittest




class test(unittest.TestCase):
    def test_func1(self):
        pass

    def test_func2(self):
        pass

#this one wont count it wont consider it 
    def func3(self):
        pass

    def test_func3(self):
        pass

#we can define multple clases it doesnt matther
#each test run independet of each other test  not impact on output input
#even if they are on same calss or multiple class
#readily increases if we run multiple classes

class anothertest(unittest.TestCase):
    def test_func5(self):
        pass





if __name__ == "__main__":
    unittest.main()

