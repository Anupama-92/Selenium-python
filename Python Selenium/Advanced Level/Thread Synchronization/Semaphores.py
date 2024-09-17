import threading
from selenium import webdriver

#  Allow only one thread at a time to access the browser
semaphore = threading.Semaphore(1)


def scrape_flipkart():
    with semaphore:
        driver = webdriver.Chrome()
        driver.get('https://www.flipkart.com')
        print(f"Flipkart Title: {driver.title}")
        driver.quit()


def scrape_myntra():
    with semaphore:
        driver = webdriver.Chrome()
        driver.get('https://www.myntra.com')
        print(f"Myntra Title: {driver.title}")
        driver.quit()

# Create threads for scraping
threads=[]
for _ in range(2):
    flipkart_thread = threading.Thread(target=scrape_flipkart())
    myntra_thread = threading.Thread(target=scrape_myntra())
    threads.append(flipkart_thread)
    threads.append(myntra_thread)

# Start Threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
