from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open Flipkart's homepage
driver.get('https://www.flipkart.com')

# Close the login popup if it appears
try:
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"✕")]'))
    )
    close_button.click()
except Exception as e:
    print("Login popup did not appear.")

# Find the search box and enter a product name
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('laptop')

# Trigger the search
search_box.submit()

# Wait for the search results to load
try:
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_1AtVbE'))
    )

    # Extract and print the titles of the first few products
    products = driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')
    for product in products[:5]:  # Get the first 5 products
        print(product.text)
finally:
    driver.quit()
