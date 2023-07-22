from bot.test.cars import Cars
from bot.test.what import What
from selenium.webdriver.common.by import By


bot = Cars()
bot.land()

try:
    bot.logoff()
except:
    print("not logged in")

bot.favorite("79538911817", "WSAD72214pl@")

bot.pause()