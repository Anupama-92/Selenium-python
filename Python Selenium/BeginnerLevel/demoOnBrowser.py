from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome_driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# Firefox Browser
# service_obj = Service()
# driver = webdriver.Firefox(service=service_obj)

# Edge Browser
# service_obj = Service()
# driver = webdriver.edge(service=service_obj)

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print(driver.title)  # Print title of browser tab
print(driver.current_url)
# driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
# Alternate way
# service_obj = Service("E:\Learnings\Selenium+Python\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.saucedemo.com/")
