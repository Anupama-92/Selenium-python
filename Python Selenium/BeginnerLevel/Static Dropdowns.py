from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome_driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Anupama")
driver.find_element(By.NAME, "email").send_keys("Saranu")
driver.find_element(By.ID, "exampleCheck1").click()

# If it has select tag, then that is static dropdown
# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
sleep(5)
dropdown.select_by_visible_text("Female")
sleep(5)
dropdown.select_by_index(0)
# dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message
