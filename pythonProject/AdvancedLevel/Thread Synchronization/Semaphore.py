import threading
from selenium import webdriver

semaphore = threading.Semaphore(2)  # Allow 2 threads to access at once


def access_website(url):
    with semaphore:
        driver = webdriver.Chrome()
        driver.get(url)
        print(f"Thread {threading.current_thread().name} accessing {url}")
        driver.quit()


urls = ['https://www.example.com', 'https://www.python.org', 'https://www.selenium.dev']

threads = []
for url in urls:
    thread = threading.Thread(target=access_website, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
