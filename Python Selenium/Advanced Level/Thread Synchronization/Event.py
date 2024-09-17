import threading
from selenium import webdriver

event = threading.Event()


def scrape_flipkart():
    driver = webdriver.Chrome()
    driver.get('https://www.flipkart.com')
    print(f"Flipkart Title: {driver.title}")
    driver.quit()
    # Set the event to signal that Flipkart scraping is done
    event.set()


def scrape_myntra():
    # Wait until the event is set
    event.wait()
    driver = webdriver.Chrome()
    driver.get('https://www.myntra.com')
    print(f"Myntra Title: {driver.title}")
    driver.quit()


# Create threads
thread_flipkart = threading.Thread(target=scrape_flipkart)
thread_myntra = threading.Thread(target=scrape_myntra)

# Start threads
thread_flipkart.start()
thread_myntra.start()

# Wait for threads to complete
thread_flipkart.join()
thread_myntra.join()
