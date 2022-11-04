import unittest
from utilities.readURL import readURL

from selenium import webdriver

class testTitle(unittest.TestCase):

    url = readURL.url()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cls.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_title(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.actualTitle = self.driver.title
        #assertEqual
        self.assertEqual("Your Store",self.actualTitle,"The title isn't the same")

if __name__  == "__main__":
    unittest.main()


