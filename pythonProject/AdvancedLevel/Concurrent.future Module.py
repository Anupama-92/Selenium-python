# Scraping Multiple Web Pages Concurrently Using ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver


# Function to open a website and print its title
def fetch_title(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Title of {url}: {driver.title}")
    driver.quit()


# List of URLs to scrape
urls = [
    'https://www.flipkart.com',
    'https://www.myntra.com',
    'https://www.python.org'
]

# Using ThreadPoolExecutor to open URLs concurrently
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks for each URL
    futures = [executor.submit(fetch_title, url) for url in urls]

    # Wait for all futures to complete
    for future in futures:
        future.result()


# Running Tests Concurrently Using ThreadPoolExecutor
# Function to simulate a test case
def run_test(test_id):
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    print(f"Running test {test_id}, Page title: {driver.title}")
    driver.quit()


# List of test IDs
test_ids = [1, 2, 3, 4, 5]

# Running tests concurrently using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(run_test, test_id) for test_id in test_ids]

    # Wait for all futures to complete
    for future in futures:
        future.result()


# Scraping Multiple Pages Using map() with ThreadPoolExecutor
# Function to fetch page title
def get_title(url):
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    driver.quit()
    return title


# List of URLs to scrape
urls = ['https://www.flipkart.com', 'https://www.myntra.com', 'https://www.python.org']

# Using ThreadPoolExecutor to map the URLs to the get_title function
with ThreadPoolExecutor(max_workers=3) as executor:
    titles = executor.map(get_title, urls)

# Print the results
for title in titles:
    print(f"Page title: {title}")

