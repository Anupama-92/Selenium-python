# Basic example for Metaclasses
# # Define a custom metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


# Define a class using the custom metaclass
class MyClass(metaclass=MyMeta):
    pass


# Instantiating the class
obj = MyClass()


# Enforcing Consistency Across Page Objects

from selenium import webdriver


# Define a metaclass to enforce a required method in classes
class PageMeta(type):
    def __new__(cls, name, bases, dct):
        # Ensure all page objects have a 'get_title' method
        if 'get_title' not in dct:
            raise TypeError(f"Class {name} must define a 'get_title' method.")
        return super().__new__(cls, name, bases, dct)


# A page object class using the custom metaclass
class LoginPage(metaclass=PageMeta):
    def __init__(self, driver):
        self.driver = driver

    # Required 'get_title' method
    def get_title(self):
        return self.driver.title


# A class that will raise an error because 'get_title' is missing
class HomePage(metaclass=PageMeta):
    def __init__(self, driver):
        self.driver = driver


# Example usage
driver = webdriver.Chrome()

try:
    login_page = LoginPage(driver)  # Works fine
    print("LoginPage class created successfully")

    home_page = HomePage(driver)  # Raises TypeError
    print("HomePage class created successfully")
except TypeError as e:
    print(e)

driver.quit()


