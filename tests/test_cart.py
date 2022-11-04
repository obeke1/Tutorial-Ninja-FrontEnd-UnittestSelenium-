import unittest
import HtmlTestRunner
import time
from selenium import webdriver
import sys
sys.path.append("C://Users/User/PycharmProjects/Tutorial-Ninja-FrontEnd(UnittestSelenium)")
from pages.cartObjects import CartObjects
from utilities.readConfigGuest import readGuestConfig
from utilities.readURL import readURL
from utilities.cartLogger import cartLog
#from tests.driver import unidriver

class test_Cart(unittest.TestCase):

    url = readURL.url()

    cl=cartLog.CartLog()

    firstName = readGuestConfig.getfirstName()
    lastName = readGuestConfig.getlastName()
    email = readGuestConfig.getEmail()
    telephone = readGuestConfig.getTelephone()
    address = readGuestConfig.getAddress()
    city = readGuestConfig.getCity()
    postcode = readGuestConfig.getpostalCode()
    country = readGuestConfig.getCountry()
    region = readGuestConfig.getRegion()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cls.url)

    def testCart(self):

        self.driver.get(self.url)
        self.cl.info("........ Starting the cart testing ...........")
        self.cl.info("......... Starting to select the product and add them to the cart ........")
        #assigning a variable for the class method(CartObjects) from pages
        self.co = CartObjects(self.driver)
        self.co.clicklaptops_Notebooks()
        time.sleep(2)
        self.co.clickShowAllLaptops()
        time.sleep(2)
        self.co.clickhplp3065()
        time.sleep(2)
        self.co.clickfirsthplp3065Picture()
        time.sleep(2)
        self.co.clicknextbtn()
        time.sleep(2)
        self.co.clickbtnClose()
        time.sleep(2)
        self.cl.info("........ Starting adding the product to the Cart ...........")
        self.co.clickCalendar()
        time.sleep(2)
        self.co.clickMonthyear()
        time.sleep(2)
        self.co.clickcalendarDate()
        time.sleep(2)
        self.co.setquantity("2")
        time.sleep(2)
        self.co.clickAddtoCart()
        time.sleep(2)
        self.co.clickCart()
        time.sleep(2)
        self.co.clickCheckout()
        time.sleep(2)
        self.cl.info("........ Starting providing the personal details as register user or guest ...........")
        self.co.clickradiobtnGuest()
        time.sleep(2)
        self.co.clickbtnaccount()
        time.sleep(2)
        self.co.setfirstName(self.firstName)
        time.sleep(2)
        self.co.setlastName(self.lastName)
        time.sleep(2)
        self.co.setEmail(self.email)
        time.sleep(2)
        self.co.setTelephone(self.telephone)
        time.sleep(2)
        self.co.setAddress(self.address)
        time.sleep(2)
        self.co.setCity(self.city)
        time.sleep(2)
        self.co.setpostalCode(self.postcode)
        time.sleep(2)
        self.co.selectCountry(self.country)
        time.sleep(2)
        self.co.selectRegion(self.region)
        time.sleep(2)
        self.co.clickguestButton()
        time.sleep(2)
        self.cl.info("........ Starting the shipping process...........")
        self.co.clickshippingButton() #click on the
        time.sleep(2)
        self.co.clickagreeTerms()
        time.sleep(2)
        self.cl.info("........ Starting the payment process ...........")
        self.co.clickPayment()
        time.sleep(2)
        self.co.getfinalPrice()
        time.sleep(2)
        self.co.clickConfirmation()
        time.sleep(2)
        self.co.printsuccessMessage()
        time.sleep(2)
        self.co.completeShipping()

        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../reports"))
