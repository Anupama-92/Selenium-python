from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

# A sample function to simulate a task


def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")

# Using ThreadPoolExecutor to manage threads


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")


# Scraping the titles of multiple websites using threading.
# Function to scrape a website
def scrape_website(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Title of {url}: {driver.title}")
    driver.quit()


# List of URLs to scrape
urls = ['https://www.example.com', 'https://www.python.org', 'https://www.selenium.dev']

# Creating threads for each URL
threads = [threading.Thread(target=scrape_website, args=(url,)) for url in urls]

# Starting the threads
for thread in threads:
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

# Using ThreadPoolExecutor with Selenium
# Using ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(scrape_website, urls)



