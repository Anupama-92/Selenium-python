from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Reading Text file
driver.get('file:C:/Users/Anupama Saranu/Desktop/Test.txt')
text_content = driver.find_element(By.TAG_NAME,'body').text
print(text_content)