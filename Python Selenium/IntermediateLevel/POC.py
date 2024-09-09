import time

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pythonProject.IntermediateLevel import TestModule

# expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
# uppered_expectedList = list(map(lambda expectedlist1: expectedlist1.upper(),expectedList))
print(TestModule.uppered_expectedList)
actualList =[]

URL = TestModule.service_obj
driver = webdriver.Chrome(service=TestModule.service_obj)
driver.maximize_window()
driver.implicitly_wait(2)

# 5 seconds is max time out. 2 seconds (3 seconds save)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(4)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert TestModule.expectedList == actualList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()  #15
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# def calculate():
# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
add = 0
for price in prices:
    add += int(price.text)
print(add)

# sum1 = reduce([lambda sum, price: [sum + int(price.text)] for price in prices])


# print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert add == totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("Anupama")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

discountedAmount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert totalAmount > discountedAmount

















