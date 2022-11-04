import unittest
from selenium import webdriver

class unidriver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.chrome()
        cls.driver.maximize_window()
        cls.driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
