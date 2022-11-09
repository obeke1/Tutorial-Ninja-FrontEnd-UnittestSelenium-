#importing packages
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.readURL import readURL

#Creating a class for Cart Objects
class CartObjects:
    btn_Phones_linktext="Phones & PDAs"
    img_PalmTreoPro_xpath="//img[@title='Palm Treo Pro']"
    img_firstPalmTreoProPicture_xpath="//ul[@class='thumbnails']/li[1]"
    btn_next_xpath="//button[@title='Next (Right arrow key)']"
    btn_close_xpath="//button[@title='Close (Esc)']"
    txt_quantity_name="quantity"
    btn_AddtoCart_id="button-cart"
    link_laptops_linktext="Laptops & Notebooks"
    link_showAllLaptops_linktext="Show All Laptops & Notebooks"
    img_hplp3065_xpath="//img[@title='HP LP3065']"
    img_firsthplp3065Picture_xpath="//ul[@class='thumbnails']/li[1]"
    select_calendar_xpath="//i[@class='fa fa-calendar']"
    select_MonthYear_xpath="//*[@class='picker-switch']"
    nextClickCalendar_xpath="//th[@class='next']"
    calendarDate_xpath="//td[text()='1']"
    btn_cart_xpath="//span[@id='cart-total']"
    link_checkout_xpath="//p[@class='text-right']/a[2]"
    radio_guest_xpath="//input[@value='guest']"
    btn_account_xpath="//input[@id='button-account']"
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_id="input-payment-email"
    txt_telephone_name="telephone"
    txt_address_name="address_1"
    txt_city_name="city"
    txt_postalcode_name="postcode"
    select_country_name="country_id"
    select_region_name="zone_id"
    btn_guest_id="button-guest"
    btn_shipping_id="button-shipping-method"
    checkbox_agree_xpath="//input[@name='agree']"
    btn_payment_id="button-payment-method"
    finalPrice_xpath="//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]"
    btn_confirmation_id="button-confirm"
    successMessage="//div[@id='content']/p[1]"
    btn_completeShipping_xpath="//a[@class='btn btn-primary']"
    month_year=readURL.month_year() #call/invoke the month_year() method from the utilities readURL.py file
    #create the constructor init and include driver as a parameter
    def __init__(self,driver):
       self.driver = driver
    #Move the cursor to/over Laptops and Notebooks(Mouse Actions)
    def clicklaptops_Notebooks(self):
        self.laptopsNotebook=self.driver.find_element(By.LINK_TEXT,self.link_laptops_linktext)
        self.action=ActionChains(self.driver)   #Mouse Action
        self.action.move_to_element(self.laptopsNotebook).perform()
    #Click on the Show All Laptops(Link)
    def clickShowAllLaptops(self):
        self.showAlllaptops=self.driver.find_element(By.LINK_TEXT,self.link_showAllLaptops_linktext)
        self.showAlllaptops.click()
    #Click on the Laptop(hplp3065)
    def clickhplp3065(self):
        self.hplp3065=self.driver.find_element(By.XPATH,self.img_hplp3065_xpath)
        self.hplp3065.location_once_scrolled_into_view  #scroll the particular element you would like to scroll too
        self.hplp3065.click()
    # Click on the Laptop(hplp3065) first picture
    def clickfirsthplp3065Picture(self):
        self.firsthplp3065=self.driver.find_element(By.XPATH,self.img_firsthplp3065Picture_xpath)
        self.firsthplp3065.click()
    # Click on the next arrow until the last image/picture
    def clicknextbtn(self):
        self.btn_next = self.driver.find_element(By.XPATH, self.btn_next_xpath)
        for next in range(0, 2):
            self.btn_next.click()
        # take/save a screenshot of the last image/picture and save it in a screenshots/Cart Product folder
        self.driver.save_screenshot('../screenshots/Cart Product/' + 'cartProduct' + str(random.randint(0, 101)) + '.png')
    #Click on the close(x)
    def clickbtnClose(self):
        self.btn_Close = self.driver.find_element(By.XPATH, self.btn_close_xpath)
        self.btn_Close.click()
    #Select the calendar
    def clickCalendar(self):    # Calendar
        self.calendar = self.driver.find_element(By.XPATH,self.select_calendar_xpath)
        self.calendar.location_once_scrolled_into_view #scroll to the calendar element inorder to view it
        self.calendar.click()
    #  Select the month and year
    def clickMonthyear(self): #month year selector
        self.monthyear=self.driver.find_element(By.XPATH, self.select_MonthYear_xpath)
        self.nextcalendar=self.driver.find_element(By.XPATH,self.nextClickCalendar_xpath)
        while self.monthyear.text != self.month_year:#use the variable month_year for the invoked/called method
            self.nextcalendar.click()
    #Select the specific date(01)
    def clickcalendarDate(self):
        self.calendarDate=self.driver.find_element(By.XPATH,self.calendarDate_xpath)
        self.calendarDate.click()
    #Providing the quantity of the item you want to buy
    def setquantity(self, quantity):
        self.quantity = self.driver.find_element(By.NAME, self.txt_quantity_name)
        self.quantity.clear()
        self.quantity.send_keys(quantity)
    #Click on the Add to Cart button
    def clickAddtoCart(self):
        self.AddtoCart = self.driver.find_element(By.ID, self.btn_AddtoCart_id)
        self.AddtoCart.click()
    #Click on the Cart icon to complete shipping
    def clickCart(self):
        self.btnCart=self.driver.find_element(By.XPATH,self.btn_cart_xpath)
        self.btnCart.click()
    #Click on the Check out
    def clickCheckout(self):
        self.checkout=self.driver.find_element(By.XPATH, self.link_checkout_xpath)
        self.checkout.click()
    #Click on the Guest radio button
    def clickradiobtnGuest(self):
        self.radiobtnGuest=self.driver.find_element(By.XPATH,self.radio_guest_xpath)
        self.radiobtnGuest.click()
    #Click on the Continue button
    def clickbtnaccount(self):
        self.btnaccount=self.driver.find_element(By.XPATH,self.btn_account_xpath)
        self.btnaccount.click()
    #set Guest First Name
    def setfirstName(self,firstname):
        self.firstname=self.driver.find_element(By.NAME,self.txt_firstname_name)
        self.firstname.location_once_scrolled_into_view
        self.firstname.clear()  #clear the firstname textfield if there's any default value
        self.firstname.send_keys(firstname)
    #Set Guest Last Name
    def setlastName(self,lastname):
        self.lastname=self.driver.find_element(By.NAME,self.txt_lastname_name)
        self.lastname.clear()  #clear the lastname textfield if there's any default value
        self.lastname.send_keys(lastname)
    #Set Guest Email
    def setEmail(self,email):
        self.email=self.driver.find_element(By.ID,self.txt_email_id)
        self.email.clear()     #clear the email textfield if there's any default value
        self.email.send_keys(email)
    #set Guest Telephone
    def setTelephone(self,telephone):
        self.telephone = self.driver.find_element(By.NAME,self.txt_telephone_name)
        self.telephone.clear()  # clear the telephone textfield if there's any default value
        self.telephone.send_keys(telephone)
    #set Guest Address
    def setAddress(self,address):
        self.address = self.driver.find_element(By.NAME,self.txt_address_name)
        self.address.clear()  # clear the address textfield if there's any default value
        self.address.send_keys(address)
    #set Guest City
    def setCity(self,city):
        self.city = self.driver.find_element(By.NAME,self.txt_city_name)
        self.city.clear()  # clear the city textfield if there's any default value
        self.city.send_keys(city)
    #set Guest Postal Code
    def setpostalCode(self,postalCode):
        self.postalCode = self.driver.find_element(By.NAME,self.txt_postalcode_name)
        self.postalCode.clear()  # clear the postal Code textfield if there's any default value
        self.postalCode.send_keys(postalCode)
    #select Guest Country
    def selectCountry(self,country):
        self.country = self.driver.find_element(By.NAME,self.select_country_name)
        self.countrydp=Select(self.country)
        self.countrydp.select_by_visible_text(country)
    #Select Guest Region
    def selectRegion(self,region):
        self.region= self.driver.find_element(By.NAME,self.select_region_name)
        self.regiondp=Select(self.region)
        self.regiondp.select_by_visible_text(region)
    #Click on the Guest Button
    def clickguestButton(self):
        self.guestButton=self.driver.find_element(By.ID,self.btn_guest_id)
        self.guestButton.click()
    #Click on the shipping Button
    def clickshippingButton(self):
        self.button_shipping = self.driver.find_element(By.ID,self.btn_shipping_id )
        self.button_shipping.click()
    # Click the agree terms and conditions check box
    def clickagreeTerms(self):
        self.check_agree = self.driver.find_element(By.XPATH,self.checkbox_agree_xpath)
        self.check_agree.click()
    # Payment button
    def clickPayment(self):
        self.button_payment = self.driver.find_element(By.ID,self.btn_payment_id)
        self.button_payment.click()
    # Final price
    def getfinalPrice(self):
        self.finalprice = self.driver.find_element(By.XPATH, self.finalPrice_xpath)
        # Print the final price of the product in the console
        print("The final price of the product is" + self.finalprice.text)
    # Confirmation button
    def clickConfirmation(self):
        self.button_confirmation = self.driver.find_element(By.ID, self.btn_confirmation_id)
        self.button_confirmation.click()
    # Success Message
    def printsuccessMessage(self):
        self.success_text = self.driver.find_element(By.XPATH,self.successMessage )
        print(self.success_text.text)
    #Click on the Complete shipping
    def completeShipping(self):
        self.completeShipping=self.driver.find_element(By.XPATH,self.btn_completeShipping_xpath)
        self.completeShipping.click()

























