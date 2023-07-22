from bot.test.cars import Cars
from bot.test.what import What
from selenium.webdriver.common.by import By

bot = Cars()
bot.land()

expand = bot.chromeDriver.find_element(By.XPATH, "//button[@data-ftid='sales__filter_advanced-button']")
expand.click()

bot.clicknsend(What.mark, "Toyota")
bot.clicknsend(What.model, "Harrier")
bot.clicknsend(What.unsold)
bot.clicknsend(What.fuel, "Гибрид")
bot.clicknsend(What.mileage, "1000")
bot.clicknsend(What.year, "2007")
bot.clicknsend(What.submitmain)

bot.checkPage()
bot.clicknsend(What.nextpage)
bot.checkPage()

bot.pause()