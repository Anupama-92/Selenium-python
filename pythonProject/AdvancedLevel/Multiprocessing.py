from multiprocessing import Pool
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Pool


# A sample function for squaring numbers


def square(n):
    return n * n


if __name__ == "__main__":
    # Creating a pool of 4 processes
    with Pool(4) as p:
        results = p.map(square, [1, 2, 3, 4])
    print(results)




# Function to scrape a website
def scrape_website(url):
    driver = webdriver.Chrome()  # Launch a new Chrome browser instance
    driver.get(url)              # Navigate to the specified URL
    print(f"Title of {url}: {driver.title}")  # Print the title of the page
    driver.quit()                # Close the browser


# List of URLs
urls = ['https://www.example.com', 'https://www.python.org', 'https://www.selenium.dev']

# Using Pool to manage processes
if __name__ == '__main__':
    with Pool(processes=3) as pool:  # Create a pool with 3 processes
        pool.map(scrape_website, urls)  # Map the URLs to the scrape_website function

# Scraping multiple websites using multiprocessing to run browser instances independently in separate processes.


# Function to scrape a website
def scrape_website(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Title of {url}: {driver.title}")
    driver.quit()


# List of URLs to scrape
urls = ['https://www.example.com', 'https://www.python.org', 'https://www.selenium.dev']

# Creating processes for each URL
processes = [Process(target=scrape_website, args=(url,)) for url in urls]

# Starting the processes
for process in processes:
    process.start()

# Waiting for all processes to complete
for process in processes:
    process.join()


# Synchronous(Single-Threaded)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

nums = [30, 35, 40]

for num in nums:
    print(f"Fibonacci of {num}: {fib(num)}")

# Using Multiprocessing (CPU-bound)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

nums = [30, 35, 40]

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        results = pool.map(fib, nums)
        for num, result in zip(nums, results):
            print(f"Fibonacci of {num}: {result}")
