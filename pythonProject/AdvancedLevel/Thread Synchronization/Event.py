import threading
from selenium import webdriver

event = threading.Event()


def access_website(url):
    event.wait()  # Wait for event to be set
    driver = webdriver.Chrome()
    driver.get(url)
    print(f"Accessing {url}")
    driver.quit()


urls = ['https://www.example.com', 'https://www.python.org']

threads = []
for url in urls:
    thread = threading.Thread(target=access_website, args=(url,))
    threads.append(thread)
    thread.start()

event.set()  # Allow all threads to proceed
for thread in threads:
    thread.join()
