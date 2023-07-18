from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import bot.test.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from bot.test.what import What
import re

#dobavit' v constructor drugie drivera
#posmotret' pro silent rejim
#proskrollil bmw
#poprobovat ploni xpath
class Cars:
    def __init__(self, driver_path=r"C:\seleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        #super(Booking, self).__init__()
        self.chromeDriver = webdriver.Chrome()
        #self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.chromeDriver.quit()

    @staticmethod
    def pause():
        wait = input('paused')

    def land_first_page(self):
        self.chromeDriver.get(const.BASE_URL)
        self.chromeDriver.implicitly_wait(3)
        full = self.chromeDriver.find_element(By.XPATH, "//button[@data-ftid='sales__filter_advanced-button']")
        full.click()

    def r_send(self, field: list, val: str = None):
        element = self.chromeDriver.find_element(By.XPATH, field[0])
        wait = WebDriverWait(element, 2).until(lambda d: element.is_enabled())
        element.click()

        if (val == None):
            return

        element.send_keys(val)
        if (field == What.mileage):
            return

        element = self.chromeDriver.find_element(By.XPATH, field[1] + "[contains(text(), '" + val + "')]")
        element.click()

    def checkPage(self):
        for n in range(1, 20):
            elements = self.chromeDriver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" +
                                                      str(n) + "]").get_attribute("innerHTML")
            if (re.search("км", elements) == None or re.search("class=\"css-z5srlr e162wx9x0\"", elements) != None):
                print("net probega ili prodan")
            elements = self.chromeDriver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" +
                                                      str(n) + "]/div[2]/div[1]/div/span").text

            year = re.split(" ", elements)
            if (int(year[len(year) - 1]) < 2007):
                print("stara mashina")





