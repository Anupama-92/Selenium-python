from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
name = "Selenium"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
# Switching browser to alert mode
alert = driver.switch_to.alert
# Getting the text from alert popup
Text = alert.text
print(Text)
assert name in Text
# accept is a method which helps to click on 'Ok' or 'yes' button
alert.accept()
action = ActionChains(driver)
# action.double_click(driver.find_element(By.))
# action.context_click() - Right click
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("Screen.png")