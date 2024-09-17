import threading
from selenium import webdriver

lock = threading.Lock()


def access_flipkart():
    with lock:
        driver = webdriver.Chrome()
        driver.get('https://www.flipkart.com')
        print(f"Flipkart title: {driver.title}")
        driver.quit()


def access_myntra():
    with lock:
        driver = webdriver.Chrome()
        driver.get('https://www.myntra.com')
        print(f"Myntra title: {driver.title}")
        driver.quit()
        

# Create threads
thread1 = threading.Thread(target=access_flipkart)
thread2 = threading.Thread(target=access_myntra)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
