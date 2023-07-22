from bot.test.cars import Cars
from bot.test.what import What
from selenium.webdriver.common.by import By

bot = Cars()
bot.land()

bot.chooseLocation()
bot.showPopular()

bot.pause()