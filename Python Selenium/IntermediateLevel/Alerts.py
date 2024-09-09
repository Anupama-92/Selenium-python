from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Chrome_driver - Chrome browser
x = 5
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
name = "Selenium"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
# Switching browser to alert mode
alert = driver.switch_to.alert
# Getting the text from alert popup
Text = alert.text
print(Text)
assert name in Text
# accept is a method which helps to click on 'Ok' or 'yes' button
alert.accept()
# Dismiss is a method which helps to click on 'cancel' button
# alert.dismiss()
