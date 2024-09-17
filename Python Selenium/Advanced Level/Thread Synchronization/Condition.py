import threading
from selenium import webdriver

condition = threading.Condition()

def scrape_flipkart():
    with condition:
        driver = webdriver.Chrome()
        driver.get('https://www.flipkart.com')
        print(f"Flipkart Title: {driver.title}")
        driver.quit()
        # Notify that Flipkart scraping is done
        condition.notify_all()

def scrape_myntra():
    with condition:
        # Wait until Flipkart scraping is done
        condition.wait()
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
