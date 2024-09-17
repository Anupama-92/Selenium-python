import threading
from selenium import webdriver

lock = threading.Lock()


def access_website(url):
    with lock:
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

for thread in threads:
    thread.join()
