from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable.prettytable import PrettyTable

from bot.test.what import What
from bot.test.what import BASE_URL

import re
import os


class Cars:
    def __init__(self, driver_path=r"C:\seleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        # super(Booking, self).__init__()
        self.chromeDriver = webdriver.Chrome()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.chromeDriver.quit()

    @staticmethod
    def pause():
        """
        колхозный брейкпоинт
        """
        wait = input('paused')

    def land(self, url: str = None):
        """
        откроет страницу переданную в параметры. если ничего не передать откроет auto.drom
        """
        if (url != None):
            self.chromeDriver.get(BASE_URL + url)
        else:
            self.chromeDriver.get(BASE_URL)

        # возможно придется поиграть с этим значением. мне хватает 1, вам может понадобиться больше
        self.chromeDriver.implicitly_wait(1)

    def clicknsend(self, field: list, val: str = None):
        """
        выберет элемент field, если такой есть в what.py, попытается ввести значение val, если оно передано, и нажмет на кнопку.
        """
        element = self.chromeDriver.find_element(By.XPATH, field[0])
        wait = WebDriverWait(element, 2).until(lambda d: element.is_enabled())
        element.click()

        #если мы не передаем ключи, то значит, что элемент - кнопка. можно выходить
        if (val == None):
            return

        element.send_keys(val)
        #пробегу достаточно ключей, можно выходить
        if (field == What.mileage):
            return

        element = self.chromeDriver.find_element(By.XPATH, field[1] + "[contains(text(), '" + val + "')]")
        element.click()

    def checkPage(self):
        """
        проверит элементы на странице на наличие аттрибутов из тестового.
        """
        for n in range(1, 20):

            elements = self.chromeDriver.find_element(By.XPATH,
                                                      What.listofcars[0] + str(n) + "]").get_attribute("innerHTML")
            #это название класса снятой с продажи машины
            if (re.search("км", elements) == None or re.search("class=\"css-z5srlr e162wx9x0\"", elements) != None):
                print("net probega ili prodan")
                return
            #это путь к названию машины
            elements = self.chromeDriver.find_element(By.XPATH,
                                                      What.listofcars[0] + str(n) + "]/div[2]/div[1]/div/span").text

            year = re.split(" ", elements)
            if (int(year[len(year) - 1]) < 2007):
                print("stara mashina")
                return

        print("vse norm")

    def login(self, login: str = None, password: str = None):
        """
        наверное не только в добавлении в избранное может потребоваться метод который будет просто логинить
        """

        element = self.chromeDriver.find_element(By.XPATH, What.profile[0])
        element.click()
        element = self.chromeDriver.find_element(By.XPATH, What.loginandpassword[0] + What.loginandpassword[1])
        element.click()

        if (login == None):
            login = input("enter login:")
        element.send_keys(login)

        element = element.find_element(By.XPATH, What.loginandpassword[0] + What.loginandpassword[2])
        element.click()
        if (password == None):
            password = input("enter password:")
        element.send_keys(password)

        element = element.find_element(By.XPATH, What.submitlogin[0])
        element.click()

    def logoff(self):
        """
        тестовое требует залогиниться прежде чем добавить в избранные, поэтому надо быть разлогиненным
        """
        #по этому пути находится кнопка разлогинивания
        element = self.chromeDriver.find_element(By.XPATH, What.profile[0] + "/div[1]")
        element.click()

    def favorite(self, login: str = None, password: str = None):
        """
        хз правильно или нет понял задание, сделал так чтобы среднее обьявление из карусели добавилось.
        требует логин и пароль, если не выдать то попросит в консоли
        """
        # по этому пути находится четвертое обьявление из карусели. кейс специфичный, поэтому не стал выносить в переменную
        element = self.chromeDriver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[4]/div[3]/div/a[4]")
        element.click()

        self.login(login, password)

        element = self.chromeDriver.find_element(By.XPATH, What.favorite[0])
        element.click()

    def chooseLocation(self, location: str = "Приморский край"):
        """
        выбирает город. по умолчанию приморский край
        """
        element = self.chromeDriver.find_element(By.XPATH, What.othercity[0])
        element.click()

        element = self.chromeDriver.find_element(By.XPATH, What.searchforcity[0])
        element.send_keys(location)
        element.send_keys(Keys.ENTER)

    def showPopular(self, amount: int = 20):
        """
        проходится по таблице с производителями автомобилей, пишет в список пар. сортирует список и создает таблицу из <amount> самых популярных
        """
        element = self.chromeDriver.find_element(By.XPATH, What.showall[0])
        element.click()

        """
        так как это таблица нам нужен цикл в цикле.
        так как мы не знаем сколько в каждой колонке элементов, трай кетч в конце каждой нас устраивает
        а вот трай кетч для марок, которых нет поганит всю асимптоматику сложности по времени
        оно работает, просто каждый не найденный элемент похоже тригеррит implicit wait
        а как сделать по другому я пока не понимаю
        """
        result = []
        j = int(0)
        while (j <= 4):
            i = int(0)
            j += 1
            try:
                while (True):
                    i += 1
                    print(i, j)
                    try:
                        element = self.chromeDriver.find_element(By.XPATH, What.colofcars[0] + str(j) + "]/div["
                                                                 + str(i) + "]/div/div/span[1]")
                        newkey = element.text
                        print("mark" + str(i) + ": " + newkey)
                        try:
                            element = self.chromeDriver.find_element(By.XPATH, What.colofcars[0] + str(j) + "]/div["
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
        for i in range(0, amount):
            table.add_row(result[i])
        print(table)
