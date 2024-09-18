from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Custom Metaclass that enforces specific methods in page objects
class PageMeta(type):
    def __new__(cls, name, bases, dct):
        # Enforce that every class has get_title, get_url, and navigate_to methods
        required_methods = ['get_title', 'get_url', 'navigate_to']
        for method in required_methods:
            if method not in dct:
                raise TypeError(f"Class {name} must define {method} method.")
        return super().__new__(cls, name, bases, dct)


# Base class for page objects (optional, for shared functionality)
class BasePage(metaclass=PageMeta):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self):
        raise NotImplementedError

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url


# Flipkart HomePage class using the custom metaclass
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.flipkart.com"

    def navigate_to(self):
        self.driver.get(self.url)

    def search_item(self, item):
        # Example of interacting with search input
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys(item)
        search_box.submit()
        time.sleep(2)  # Let page load


# Flipkart LoginPage class using the custom metaclass
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.flipkart.com/account/login"

    def navigate_to(self):
        self.driver.get(self.url)

    def login(self, username, password):
        # Example login interaction with login form
        email_input = self.driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        email_input.send_keys(username)
        password_input.send_keys(password)
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        time.sleep(2)  # Wait for the login process


# Example test script to validate the metaclass-enforced page objects
if __name__ == '__main__':
    driver = webdriver.Chrome()

    try:
        # HomePage Test
        home_page = HomePage(driver)
        home_page.navigate_to()
        print(f"Home Page Title: {home_page.get_title()}")
        print(f"Home Page URL: {home_page.get_url()}")
        home_page.search_item("laptop")  # Search for laptops on Flipkart

        # LoginPage Test
        login_page = LoginPage(driver)
        login_page.navigate_to()
        print(f"Login Page Title: {login_page.get_title()}")
        print(f"Login Page URL: {login_page.get_url()}")
        # Simulate login (use valid credentials)
        # login_page.login("testuser", "testpassword")

    finally:
        time.sleep(5)  # Keep the browser open for a while to observe
        driver.quit()
