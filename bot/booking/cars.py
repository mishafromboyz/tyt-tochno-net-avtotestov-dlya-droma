from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import bot.booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
#from selenium.webdriver.support.wait import WebDriverWait

from bot.booking.what import What
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
                                                     "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" + str(
                                                         n) + "]").get_attribute("innerHTML")
            if (re.search("км", elements) == None or re.search("class=\"css-z5srlr e162wx9x0\"", elements) != None):
                print("net probega ili prodan")
            elements = self.chromeDriver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" + str(
                                                         n) + "]/div[2]/div[1]/div/span").text

            year = re.split(" ", elements)
            if (int(year[len(year) - 1]) < 2007):
                print("stara mashina")





"""
    def r_find(self, field: str, val: str = None):
        element = self.chromeDriver.find_element(By.XPATH, field)
        element.click()

        if (val == None):
            return

        if (field == What.mileage):
            element = element.find_element(By.XPATH, "//input[@data-ftid='sales__filter_mileage-from']")
            element.send_keys(val)
            return

        if (field == What.mark or field == What.model):
            mod_xpath = str("/html/body/div[2]/div[5]/div[1]/div[1]/div[3]/form/div/div[1]/div[1]/div/div[2]/div//*[@class='css-1r0zrug e1uu17r80']//*[contains(text(), '" + val + "')]")
        else:
            mod_xpath = str("//*[@class='css-17vx1of e1x0dvi10'][contains(text(), '" + val + "')]")

        i = int(0)
        j = int(0)
        while (True):
            try:
                element = element.find_element(By.XPATH, mod_xpath)
                element.click()
                break
            except:
                while (j < 10):
                    element.send_keys(Keys.DOWN)
                    j += 1
                    print(i + j, "try")
                i += j
                j = 0
                print("got out of j loop, i =" + str(i) +"\ncouldnt find" + val)
                continue
"""

"""
legacy
    def find(self, what: str, name: str):
        # sm what.py dlya pervogo argsa, vtoroi - prosto string
        # knopka vsegda naidetsya na stranice

        element = self.chromeDriver.find_element(By.XPATH, what)
        element.click()

        try:
            element = element.find_element(By.XPATH, "//*[@class='css-1r0zrug e1uu17r80']//*[contains(text(), '" + name + "')]")
            element.click()
        except:
            print("not most popular")

        return
        # a element v dropdowne - net
        i = int(0)
        j = int(0)
        # i - debug, j - iterator
        while (True):
            try:
                element = element.find_element(By.XPATH, "//*[@class='css-17vx1of e1x0dvi10']//*[contains(text(), '" + name + "')]")
                element.click()
                break
            except:
                while (j < 50):
                    element.send_keys(Keys.DOWN)
                    j += 1
                    print(i + j, "try")
                i += j
                j = 0
                print("got out of j loop, i =", i)
                continue
        #wait = input("onhold")



    def toyota(self):
        mark = self.chromeDriver.find_element(By.CSS_SELECTOR, "div[data-ftid='sales__filter_fid']")
        mark.click()

        mark = self.chromeDriver.find_element(By.XPATH, "//div[@class='css-12vehp8 e1x0dvi10'][contains(text(), 'Toyota')]")
        mark.click()
        el = WebDriverWait(self.chromeDriver, timeout=10).until_not(lambda d: mark.find_element(By.XPATH, "//*[@data-ftid='sales__filter_mid'][@disabled]"))
        print("mid is enabled")
        model = self.chromeDriver.find_element(By.CSS_SELECTOR, "div[data-ftid='sales__filter_mid']")
        model.click()
        i = 0
        while (True):
            j = 0
            try:
                model.send_keys("toyota")
                mark.find_element(By.XPATH, "//div[@class='css-17vx1of e1x0dvi10'][contains(text(), 'Harrier')]")
                break
            except:
                j = 0
                while(j < 50):
                    model.send_keys(Keys.DOWN)
                    j += 1
                    print(i+j, "try")
                i += j
                print("got out of j loop, i =", i)
                continue
        wait = input("onhold")

        mark = self.chromeDriver.find_element(By.XPATH, "//div[@class='css-17vx1of e1x0dvi10'][contains(text(), 'Harrier')]")
        mark.click()

        mark = self.chromeDriver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        mark.click()


        #toyota = self.find_element(By.XPATH, "//")
        #toyota.click()

        #currency_element = self.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        #currency_element.click()
"""
