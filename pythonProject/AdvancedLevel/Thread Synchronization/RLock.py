import threading
from selenium import webdriver

lock = threading.RLock()


def synchronized_task(url):
    with lock:
        driver = webdriver.Chrome()
        driver.get(url)
        print(f"Thread accessing {url}")
        driver.quit()


urls = ['https://www.selenium.dev', 'https://www.example.com']

threads = []
for url in urls:
    thread = threading.Thread(target=synchronized_task, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
