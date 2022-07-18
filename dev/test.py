import unittest
import main

#we can name whatver we want 
#we inherit TestCase class

class Testmain(unittest.TestCase):
    def setUp(self):
        print("about to test a function")

    """test methods name should start with
    if we want to check,the assertEquals checks the value if they are equal or not
    we can do multiple test we have to run unittest.main()
    """
    def test_do_stuff(self):
        """
    it will check in the assertequal our result is 15 nd if we 
    comapare it with given value if those are both equal then good
    otherwise false so it will pass too 15 == 15
    """
        test_param = 10
        result = main.do_stuf(test_param)
        self.assertEqual(result, 15)



#another method for adding string given as argument
    def test_do_stuff2(self):
        """the asserttrue tell if its true or false it will check if its an instanece
        or not valuerror which it will return and well get true so test passsed 
        """
        test_param = 'shkshks'
        result = main.do_stuf(test_param)
        self.assertIsInstance(result, ValueError)
        #if we add another test
        
    def test_to_stuff3(self):
        test_param = None
        result = main.do_stuf(test_param)
        self.assertEqual(result, 'please enter your number')
    
    def test_to_stuff4(self):
        test_param = ''
        result = main.do_stuf(test_param)
        self.assertEqual(result, 'please enter your number')

    def tearDown(self):
        print('cleaning out')




if __name__ == "__main__": 
    unittest.main()