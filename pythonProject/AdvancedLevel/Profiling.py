# Profiling involves measuring the time taken by different parts of the code and understanding which segments might cause slow execution or inefficiencies.
# cProfile
import cProfile
from selenium import webdriver
import timeit


def open_browser():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')
    driver.quit()


# Profile the function that opens the browser
cProfile.run('open_browser()')

# Using timeit for Precise Timing - More specific performance of small code blocks

# Measure the time it takes to execute the function
execution_time = timeit.timeit(open_browser, number=1)
print(f"Execution time: {execution_time} seconds")


