from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to the webdriver
driver_path = '/path/to/chromedriver'

# Create a new instance of Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# Open Flipkart
driver.get('https://www.flipkart.com')

# Close the login popup if it appears
try:
    close_login_popup = driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z"]')
    close_login_popup.click()
except:
    pass

# Find the search input field
search_input = driver.find_element_by_xpath('//input[@class="_3704LK"]')

# Type the topic you want to lookup
topic = 'Python programming language'
search_input.send_keys(topic)

# Press Enter to perform the search
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Find and click the first search result
first_result = driver.find_element_by_xpath('//div[@class="_4rR01T"]')
first_result.click()

# Wait for the product page to load
time.sleep(2)

# Find and click the "View all" link in the product description
view_all_link = driver.find_element_by_xpath('//a[@class="_1fQZEK"]')
view_all_link.click()

# Wait for the cached page to load
time.sleep(2)

# Get the title and URL of the cached page
cached_title = driver.title
cached_url = driver.current_url

print("Title of the cached page:", cached_title)
print("URL of the cached page:", cached_url)

# Extract information from the cached page as needed
# For example, you can find elements and extract text using Selenium's methods

# Close the browser
driver.quit()
