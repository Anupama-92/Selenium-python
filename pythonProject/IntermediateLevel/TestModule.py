from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
uppered_expectedList = list(map(lambda expectedlist1: expectedlist1.upper(),expectedList))

service_obj = Service("C:/Users/Anupama Saranu/Documents/chromedriver.exe")


