BASE_URL = "http://auto.drom.ru/"

class What:
    """
    Набор икспасов/классов для поиска элементов.
    Сделано чтобы не надо было копаться в скриптах и менять переменные там
    часть реализована в виде классов, часть - в виде икспасов
    где то прочитал что полные икспасы быстрее
    зато классы по идее более устойчивы к изменениям в разметке сайта
    на практике без понятия как лучше
    """
    mark = ["//*[@data-ftid='sales__filter_fid']//input", "//*[@class='css-144l089 e1x0dvi10']"]
    model = ["//*[@data-ftid='sales__filter_mid']//input", "//*[@class='css-144l089 e1x0dvi10']"]
    fuel = ["//*[@data-ftid='sales__filter_fuel-type']", "//*[@class='css-17vx1of e1x0dvi10']"]
    unsold = ["//*[@class='css-dixqn0 e1lp1m2z0']"]
    mileage = ["//*[@data-ftid='sales__filter_mileage-from']"]
    year = ["//*[@data-ftid='sales__filter_year-from']", "//*[@class='css-u25ii9 e154wmfa0']//*"]
    submitmain = ["//*[@data-ftid='sales__filter_submit-button']"]
    nextpage = ["//*[@data-ftid='component_pagination-item-next']"]

    listofcars = ["/html/body/div[2]/div[4]/div[1]/div[1]/div[5]/div/div[1]/a["] #не забыть закрыть скобку
    profile = ["/html/body/div[2]/div[2]/div[1]/div/div[3]"]
    loginandpassword = ["/html/body/div[1]/div[3]/div[2]/div[1]/form", "/div[3]/div[2]/input", "/div[4]/div[2]/input"]
    submitlogin = ["/html/body/div[1]/div[3]/div[2]/div[1]/form/div[5]/button"]
    favorite = ["/html/body/div[2]/div[3]/div[2]/div/div"]

    othercity = ["/html/body/div[2]/div[5]/div[1]/div[1]/div[2]/a[7]"]
    searchforcity = ["/html/body/div[5]/div[2]/div/div[4]/div/div/div[1]/div/div/input"]
    showall = ["/html/body/div[2]/div[5]/div[1]/div[1]/div[7]/div[4]/div[5]/div"]
    colofcars = ["/html/body/div[2]/div[5]/div[1]/div[1]/div[7]/div["] #не забыть закрыть скобку