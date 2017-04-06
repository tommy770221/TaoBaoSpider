# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://tw.weibo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登入").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | cbox1490450557501 | ]]
        driver.find_element_by_id("memberid").clear()
        driver.find_element_by_id("memberid").send_keys("tommy770221@gmail.com")
        driver.find_element_by_id("passwd").clear()
        driver.find_element_by_id("passwd").send_keys("henry1021")
        driver.find_element_by_id("login").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("div.sBox > input[name=\"searchInput\"]").click()
        driver.find_element_by_css_selector("div.sBox > input[name=\"searchInput\"]").clear()
        driver.find_element_by_css_selector("div.sBox > input[name=\"searchInput\"]").send_keys(u"老人")
        driver.find_element_by_css_selector("div.sBox > button[name=\"search\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
        driver.find_element_by_link_text(u"快乐老人报").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
