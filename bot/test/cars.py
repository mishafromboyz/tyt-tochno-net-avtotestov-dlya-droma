from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import bot.test.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from prettytable.prettytable import PrettyTable

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

    def land(self, url: str = None):
        if (url != None):
            self.chromeDriver.get(const.BASE_URL + url)
        else:
            self.chromeDriver.get(const.BASE_URL)

        self.chromeDriver.implicitly_wait(1)


    def clicknsend(self, field: list, val: str = None):
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

    def login(self, login: str = None, password: str = None):
        """
        наверное не только в добавлении в избранное может потребоваться метод который будет просто логинить
        """

        self.pause()
        element = self.chromeDriver.find_element(By.XPATH,
                                                "/html/body/div[2]/div[2]/div[1]/div/div[3]")
        element.click()
        self.pause()
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[3]/div[2]/div[1]/form/div[3]/div[2]/input")
        self.pause()
        element.click()
        if (login == None):
            login = input("enter login:")
        element.send_keys(login)

        element = element.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/form/div[4]/div[2]/input")
        element.click()
        if (password == None):
            password = input("enter password:")
        element.send_keys(password)

        element = element.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/form/div[5]/button")
        element.click()

    def logoff(self):
        element = self.chromeDriver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[3]/div[1]")
        element.click()


    def favorite(self, login: str = None, password: str = None):
        """
        хз правильно или нет понял задание, сделал так что среднее обьявление из карусели добавилось.
        требует логин и пароль, если не выдать то попросит в консоли
        """
        #vibrat obyavlenie
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[4]/div[3]/div/a[4]")
        element.click()

        #zaloginitsya
        self.login(login, password)

        #dobavit' v izbrannoe
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[3]/div[2]/div/div")
        element.click()


    def chooseLocation(self, location: str = "Приморский край"):
        # выбрать другой город
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[5]/div[1]/div[1]/div[2]/a[7]")
        element.click()

        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[5]/div[2]/div/div[4]/div/div/div[1]/div/div/input")
        element.send_keys(location)
        element.send_keys(Keys.ENTER)

    def showPopular(self, amount: int = 20):
        # нажать на показать все
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[5]/div[1]/div[1]/div[7]/div[4]/div[5]/div")
        element.click()

        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[5]/div[1]/div[1]/div[7]").get_attribute("innerHTML")
        result = []
        i = int(0)
        j = int(0)
        while (j<=4):
            i = int(0)
            j += 1
            try:
                while (True):
                    i += 1
                    print(i, j)
                    try:
                        element = self.chromeDriver.find_element(By.XPATH,
                                               "/html/body/div[2]/div[5]/div[1]/div[1]/div[7]/div["
                                                + str(j) + "]/div["
                                                + str(i) + "]/div/div/span[1]")
                        newkey = element.text
                        print("mark" + str(i) + ": " + newkey)
                        try:
                            element = self.chromeDriver.find_element(By.XPATH,
                                                "/html/body/div[2]/div[5]/div[1]/div[1]/div[7]/div["
                                                + str(j) + "]/div["
                                                + str(i) + "]/div/div/span[2]")
                            newvalue = element.text.strip()
                            print("amount: " + str(newvalue) + '\n')

                            result.append((newkey, int(newvalue)))
                        except:
                            print("mark not present")
                            continue
                    except:
                        print("end of list reached")
                        break
            except:
                print("end of table reached")
                break
        self.pause()

        result.sort(key=lambda val: val[1], reverse=True)
        table = PrettyTable(("Фирма", "Обьявления"))
        for i in range(0, 20):
            table.add_row(result[i])
        print(table)











