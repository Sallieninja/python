# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_authentication_user(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_authentication_user(self):
        success = True
        wd = self.wd
        wd.get("https://openh.ru/")
        wd.find_element_by_css_selector("button._3F-tM_2").click()
        wd.find_element_by_css_selector("label._22wzbVk").click()
        wd.find_element_by_id("login").click()
        wd.find_element_by_id("login").clear()
        wd.find_element_by_id("login").send_keys("sallieninja@gmail.com")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("alexey1992")
        wd.find_element_by_xpath("//form[@class='_2iJt_4P']//button[.='Войти']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
