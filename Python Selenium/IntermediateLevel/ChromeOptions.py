from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="C:\\Users\\Anupama Saranu\\Downloads\\chromedriver-win64\\chromedriver-win64")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maxmized")
chrome_options.add_argument("--ignore-certificate-errors")
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)

