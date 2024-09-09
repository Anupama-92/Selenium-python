from selenium import webdriver
import re

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

page_source = driver.page_source

pattern = r'font-size'

matches = re.findall(pattern, page_source)

if matches:
    print("Pattern found on the page!")
    print("Number of matches:", len(matches))
else:
    print("Pattern not found on the page.")

driver.quit()
