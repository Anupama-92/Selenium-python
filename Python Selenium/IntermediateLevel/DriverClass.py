from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser="chrome"):
        self.browser = browser.lower()

    def get_driver(self):
        if self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            return webdriver.Firefox()
        elif self.browser == "edge":
            return webdriver.Edge()
        else:
            raise ValueError("Unsupported browser type")

# # Example usage:
# if __name__ == "__main__":
#     # Instantiate the WebDriverFactory class
#     driver_factory = WebDriverFactory()
#
#     # Get the WebDriver instance for the desired browser
#     driver = driver_factory.get_driver()
#
#     # Example: Open a website
#     driver.get("https://www.example.com")
#
#     # Don't forget to close the WebDriver instance when done
#     driver.quit()
