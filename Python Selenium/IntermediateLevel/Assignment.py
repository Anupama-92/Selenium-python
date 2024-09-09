#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from DriverClass import WebDriverFactory
import ProjectModule as pm


class addProject:
    def __init__(self):
        # Create an instance of WebDriverFactory
        self.driver_factory = WebDriverFactory()
        self.driver = self.driver_factory.get_driver()

    def get(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(pm.login["url"])
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, pm.f_xpath["email"]).send_keys(pm.login["email"])
        self.driver.find_element(By.XPATH, pm.f_xpath["Submit"]).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
        self.driver.find_element(By.XPATH, pm.f_xpath["password"]).send_keys(pm.login["password"])
        self.driver.find_element(By.XPATH, pm.f_xpath["SignIn"]).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, pm.f_xpath["yes"]).click()
        self.driver.implicitly_wait(20)
        # driver.find_element(By.XPATH,"//input[@id='6']").click()
        self.driver.find_element(By.CSS_SELECTOR, pm.f_xpath["pmicon"]).click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("undefined")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, pm.f_xpath["addproject"]).click()
        # Adding new project in Project Management

        clientname = self.driver.find_element(By.XPATH, pm.f_xpath["clientName"])
        clientname.send_keys(pm.Proj1["clientName"])
        client = self.driver.find_element(By.CSS_SELECTOR, pm.f_xpath["client"])
        action = ActionChains(self.driver)
        action.move_to_element(client).click().perform()
        projectname = (self.driver.find_element(By.XPATH, pm.f_xpath["projectName"]))
        projectname.send_keys(pm.Proj1["projectName"])
        testdescription = (self.driver.find_element(By.XPATH, pm.f_xpath["testDescription"]))
        testdescription.send_keys(pm.Proj1["testDescription"])
        notes = self.driver.find_element(By.XPATH, pm.f_xpath["notes"])
        notes.send_keys(pm.Proj1["notes"])
        email = self.driver.find_element(By.XPATH, pm.f_xpath["emailid"])
        email.send_keys(pm.Proj1["email"])
        pmoelement = self.driver.find_element(By.XPATH, pm.f_xpath["pmod"])
        pmoelement.click()
        time.sleep(3)
        # pmo = ["Divya Bandaru", "Pravallika Kanaparthi"]
        # for option in pmo:
        #     label = self.driver.find_element(By.XPATH, pm.f_xpath["pmos"].format(option))
        #     label.click()
        body1 = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body1).click().perform()
        dropdown_element = self.driver.find_element(By.XPATH, pm.f_xpath["technologiesd"])
        dropdown_element.click()
        technologies = [".Net", "Angular"]
        for option in technologies:
            label = self.driver.find_element(By.XPATH, pm.f_xpath["technologiess"].format(option))
            label.click()
        body = self.driver.find_element(By.XPATH, "//body")
        action.move_to_element(body).click().perform()
        # Start Date
        startdate = wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH,
                                                         "//mat-datepicker-toggle[@class ='mat-datepicker-toggle ng-tns-c53-1']//span[@class='mat-button-wrapper']//*[name()='svg']"))

        )
        startdate.click()
        date_to_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='August 10, 2024']")))
        # "//button[@class='mat-calendar-body-cell mat-calendar-body-active' and @aria-label='May 2, 2024']")))
        date_to_select.click()
        # End Date
        # end_date = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,
        #                                              "//mat-datepicker-toggle[@class ='mat-datepicker-toggle ng-tns-c53-2']//span[@class='mat-button-wrapper']//*[name()='svg']")))
        #
        # end_date.click()
        # end_date_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='August 20, 2024']")))
        #                                                          #"//button[@class='mat-calendar-body-cell' and @aria-label='May 25, 2024']")))
        # end_date_select.click()
        file_input = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='Choose File']")))
        file_input.click()
        self.driver.execute_script("arguments[0].value = arguments[1]", file_input, pm.login["filepath"])
        add = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        add.click()


if __name__ == "__main__":
    project = addProject()
    project.get()












