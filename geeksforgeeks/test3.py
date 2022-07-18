#check if a string contains a substring with assertIn(key,container,message)

import unittest

class Teststring(unittest.TestCase):
   

    def test_pos(self):
        key= "alb"
        container = "albertdelrio"
        message = "key is in container"
        
        self.assertIn(key, container , message)

    def test_negative(self):
        key="gfg"
        container=  "geeksforgeeks"
        message = "key is not a container."

        self.assertIn(key, container, message)

if __name__ == "__main__":
    unittest.main()