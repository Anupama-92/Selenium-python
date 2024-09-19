# @class method
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_example(self):
        self.driver.get('https://www.selenium.dev')
        # Your test code

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# Using Explicit Waits Instead of Implicit Waits


driver = webdriver.Chrome()
driver.get('https://www.python.org')

# Use explicit wait instead of implicit wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'id-search-field')))
element.send_keys('Selenium')

# Minimize page loads
# Reduce unnecessary page loads by directly navigating to the relevant page or element instead of starting from a homepage and navigating through multiple links.
# Use direct URLs for testing specific pages instead of navigating through multiple steps.
# Headless Browser Testing

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.selenium.dev')

# Optimize Locator Strategies
# Best Locator Performance Order:
# ID
# Name
# ClassName
# TagName
# CSSSelector
# XPATH

# Reuse Elements and Avoid Re-locating
# If you need to interact with an element multiple times, avoid re-locating it every time.
# Instead, store it in a variable and reuse the reference.

# Parallel testing
# For large test suites, consider using parallel execution to run tests concurrently, reducing total execution time.
# You can use tools like pytest-xdist, Selenium Grid, or concurrent.futures.
# pytest -n 4  # Runs tests in parallel with 4 workers


# Reduce Network Overhead - Use chrome options for disabling unnecessary resources like images,CSS and Java Script
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
