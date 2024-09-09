from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
edge_options = webdriver.EdgeOptions()
# edge_options.add_argument("headless")
edge_options.add_argument("--ignore-certificate-errors")
service_obj = Service()
driver = webdriver.Edge(service=service_obj,options=edge_options)
driver.maximize_window()
driver.implicitly_wait(5)
# driver.get("https://www.bio-techne.com/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("Screen.png")
