from concurrent.futures import ThreadPoolExecutor
import time

# A sample function to simulate a task


def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")

# Using ThreadPoolExecutor to manage threads


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task, "A")
    executor.submit(task, "B")