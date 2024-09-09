from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarWale:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search_cars(self, brand):
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Type to select car name']")
        search_box.send_keys(brand)
        search_box.send_keys(Keys.RETURN)

    def get_car_prices(self):

        cars = self.driver.find_elements(By.XPATH, "//h3[@class='o-jjpuv o-cVMLxW o-mHabQ o-fzpibK']")
        prices = self.driver.find_elements(By.XPATH, "//span[@class='o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT']")
        for car, price in zip(cars, prices):
            print(f"{car.text}: {price.text}")


    def close(self):
        self.driver.quit()


class ElectricCarWale(CarWale):
    def __init__(self):
        super().__init__()

    def search_cars(self, brand):
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Type to select car name']")
        search_box.clear()
        search_box.send_keys(brand + ' electric cars')
        search_box.send_keys(Keys.RETURN)


if __name__ == "__main__":
    # Regular CarWale
    carwale = CarWale()
    carwale.driver.get("https://www.carwale.com/")
    carwale.search_cars("Toyota")
    carwale.get_car_prices()
    carwale.close()

    # Electric CarWale
    electric_carwale = ElectricCarWale()
    electric_carwale.driver.get("https://www.carwale.com/")
    electric_carwale.search_cars("Nissan")
    electric_carwale.get_car_prices()
    electric_carwale.close()
