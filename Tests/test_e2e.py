import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from utilities.BaseClass import Baseclass


class TestOne(Baseclass):
    def test_e2e(self):
        pm_icon = self.driver.find_element(By.CSS_SELECTOR, "img[alt='Project Management']")
        pm_icon.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)


