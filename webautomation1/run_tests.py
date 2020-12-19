from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import sys


class DemoBlazeSite(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = 'https://www.demoblaze.com/index.html'
        self.username = 'QA-'+str(random.randint(1000,9000))


    def tearDown(self):
        "Tear down the test"
        self.driver.close()

    def goto_homepage(self):
        self.driver.get(self.base_url)

    def open_signup_modal(self):
        signupmenu = self.driver.find_element_by_id('signin2')
        signupmenu.click()

    def open_login_modal(self):
        signupmenu = self.driver.find_element_by_id('login2')
        signupmenu.click()

    def perform_signup(self, name):
        username = self.driver.find_element_by_id('sign-username')
        username.send_keys(name)
        sleep(2)
        password = self.driver.find_element_by_id('sign-password')
        password.send_keys('123456')
        sleep(2)
        submitbtn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[2]')
        submitbtn.click()
        sleep(2)

    def perform_login(self, name):
        username = self.driver.find_element_by_id('loginusername')
        username.send_keys(name)
        sleep(2)
        password = self.driver.find_element_by_id('loginpassword')
        password.send_keys('123456')
        sleep(2)
     

    def test_signup(self):
        "test sign up functionality for positive & negative scenarios"
        self.goto_homepage()
        self.open_signup_modal()

# this is positive case
        self.perform_signup(self.username)
        obj = self.driver.switch_to.alert
        msg = obj.text
        obj.accept()
        assert "Sign up successful." in msg

#  this is negative case
        self.perform_signup('')
        obj = self.driver.switch_to.alert
        msg = obj.text
        obj.accept()
        assert "Please fill out Username and Password." in msg

# this is negative case
        self.perform_signup(self.username)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "This user already exist." in msg

    def test_login(self):
        "test sign up functionality for positive & negative scenarios"
        self.goto_homepage()
        self.open_login_modal()

# this is negative case
        self.perform_login('')
        obj = self.driver.switch_to.alert
        msg = obj.text
        obj.accept()
        assert "Please fill out Username and Password." in msg

# this is negative case
        name = 'QA-'+str(random.randint(1000,9000))
        self.perform_login(name)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "User does not exist." in msg

# this is positive case
        self.perform_login(self.username)
        welcomebtn = self.driver.find_element_by_id('nameofuser')
        assert 'Welcome '+name in welcomebtn.text


    def test_add_phone(self):
        "test adding one phone"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        phones = self.driver.find_element_by_xpath('//*[@id="itemc"][1]')
        phones.click()
        sleep(2)
        phone = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a[3]')
        phone.click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(2)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "Product added." in msg

    def test_add_laptop(self):
        "test adding one laptop"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        laptops = self.driver.find_element_by_xpath('//*[@id="itemc"][2]')
        laptops.click()
        sleep(2)
        laptop = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a[1]')
        laptop.click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(2)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "Product added." in msg

    def test_add_monitor(self):
        "test adding one monitor"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        monitors = self.driver.find_element_by_xpath('//*[@id="itemc"][3]')
        monitors.click()
        sleep(2)
        monitor = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a[2]')
        monitor.click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        sleep(2)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "Product added." in msg

    def test_cart_amount(self):
        "test total amount of products sin cart"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[4]/a').click()
        self.assertequal(self.driver.find_element_by_id('totalp'),1670)

    def test_place_order(self):
        "test order placing functionality"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[4]/a').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/button').click()
        self.driver.find_element_by_id('name').send_keys(self.username)
        self.driver.find_element_by_id('country').send_keys('BD')
        self.driver.find_element_by_id('city').send_keys('Dhaka')
        self.driver.find_element_by_id('card').send_keys('64346346343')
        self.driver.find_element_by_id('month').send_keys('December')
        self.driver.find_element_by_id('year').send_keys('2020')
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
        sleep(2)
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "Thank you for your purchase!" in msg

    def test_send_message(self):
        "test sending message from contact"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        contactbtn = self.driver.find_element_by_xpath('/html/body/nav/div/div/ul/li[2]/a')
        contactbtn.click()
        email = self.driver.find_element_by_id('recipient-email')
        email.send_keys('testemail@gmail.com')
        self.driver.find_element_by_id('recipient-name').send_keys(self.username)
        self.driver.find_element_by_id('message-text').send_keys('This is a test message')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/button[2]').click()
        obj = self.driver.switch_to.alert
        obj.accept()
        msg = obj.text
        assert "Thanks for the message!!" in msg

    def test_logout(self):
        "test logout feature"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        logoutbtn = self.driver.find_element_by_id('logout2')
        logoutbtn.click()
        sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DemoBlazeSite)
    unittest.TextTestRunner(verbosity=2).run(suite)
