# LoggingMixin: This mixin adds logging functionality, allowing any class that inherits from it to log its actions.
import logging


class LoggingMixin:
    def log(self,message):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"[LOG]: {message}")
        print(f"[LOG]: {message}")

# ScreenshotMixin: This mixin adds the functionality to take screenshots.
# It's useful in Selenium for capturing the state of a page after a test step.


class ScreenshotMixin:
    def take_screenshot(self, file_name="screenshot.png"):
        self.driver.save_screenshot(file_name)
        print(f"Screenshot saved as {file_name}")

