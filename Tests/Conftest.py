import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://chorusqa.cogninelabs.com/")
    driver.maximize_window()
    # driver.find_element(By.XPATH, "//input[@type='email']").send_keys("chorus.automation@cognine.com")
    # driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    # driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Welcome2Cognine")
    # driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    # driver.implicitly_wait(5)
    # driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
    # driver.implicitly_wait(20)

    request.cls.driver = driver
    yield
    driver.close()

