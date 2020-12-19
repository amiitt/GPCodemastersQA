from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import sys


class SauceDemo(unittest.TestCase):
    def setUp(self):
        "Setup for the test"
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.base_url = 'https://www.saucedemo.com/'
        self.lockedout_username = 'locked_out_user'
        self.standard_username = 'standard_user'
        self.password = 'secret_sauce'


    def tearDown(self):
        "Tear down the test"
        self.driver.close()

    def goto_homepage(self):
        self.driver.get(self.base_url)

    def perform_login(self, name):
        username = self.driver.find_element_by_id(name)
        username.send_keys(self.lockedout_username)
        sleep(2)
        password = self.driver.find_element_by_id('password')
        password.send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_id('login-button').click()
     

    def test_login_as_locked_out_user(self): 
        "test as locked-out user"
        self.goto_homepage()
        self.perform_login(self.lockedout_username)
        sleep(2)
        assert 'Epic sadface: Sorry, this user has been locked out.' in self.driver.page_source

    def test_login_as_standard_user(self):
        "test as standard user"
        self.goto_homepage()
        self.perform_login(self.standard_username)
        sleep(2)
        assert 'Epic sadface: Sorry, this user has been locked out.' not in self.driver.page_source

    def test_sorting_by_price(self):
        "test price filtering"
        self.goto_homepage()
        self.perform_login(self.standard_username)
        sleep(2)
        select = Select(self.driver.find_element_by_class_name('product_sort_container'))
        select.select_by_value('hilo')
        sleep(2)
        price_elements = self.driver.find_element_by_class_name('inventory_item_price')
        price_list = []
        for element in price_elements:
            price_list.append(element.text)

        print(price_list)
        assert price_list == sorted(price_list,reverse=True)

    def test_logout(self):
        "test logout"
        self.goto_homepage()
        self.open_login_modal()
        self.perform_login(self.username)
        sleep(2)
        logoutbtn = self.driver.find_element_by_id('logout_sidebar_link')
        logoutbtn.click()
        sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SauceDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)
