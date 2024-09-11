from multiprocessing import Pool

# A sample function for squaring numbers


def square(n):
    return n * n


if __name__ == "__main__":
    # Creating a pool of 4 processes
    with Pool(4) as p:
        results = p.map(square, [1, 2, 3, 4])
    print(results)


from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Pool


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
