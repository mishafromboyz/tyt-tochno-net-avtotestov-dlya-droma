from bot.booking import cars
from bot.booking.cars import Cars
from bot.booking.what import What
from selenium.webdriver.common.by import By


bot = Cars()
bot.land_first_page()

bot.r_send(What.mark, "Toyota")
bot.r_send(What.model, "Harrier")
bot.r_send(What.unsold)
bot.r_send(What.fuel, "Гибрид")
bot.r_send(What.mileage, "1000")
bot.r_send(What.year, "2007")
bot.r_send(What.submit)

bot.checkPage()
bot.r_send(What.nextpage)
bot.checkPage()

#elements = bot.chromeDriver.find_elements(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a")


#print(elements)
#bot.pause()

"""
for n in range(1, 20):
    elements = bot.chromeDriver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" + str(n) + "]").get_attribute("innerHTML")
    if(re.search("км", elements) == None or re.search("class=\"css-z5srlr e162wx9x0\"", elements) != None):
        print("net probega ili prodan")
    elements = bot.chromeDriver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a[" + str(n) + "]/div[2]/div[1]/div/span").text

    year = re.split(" ", elements)
    if (int(year[len(year)-1]) < 2007):
        print("stara mashina")
"""


#case-sensitive
"""
bot.r_find(What.mark, "BMW")
print("set mark")
bot.r_find(What.model, "Z4")
print("set model")
bot.r_find(What.fuel, "Гибрид")
print("set fuel")

bot.r_find(What.mileage, "1000")
print("set mileage")
bot.r_find(What.year, "2007")
print("set year")
bot.r_find(What.unsold)
print("set unsold")
bot.r_find(What.submit)
"""


wait = input("onhold")
#bot.toyota()

"""
with Booking() as bot:
    bot.land_first_page()
    bot.toyota()
    print("exiting")
"""
