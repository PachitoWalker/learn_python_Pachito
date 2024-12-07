import requests
from bs4 import BeautifulSoup   # Так как данные в url у нас на xml, а не json, используем BeautifulSoup
from datetime import datetime


def get_curs(numb):
    return xml.find('valute', {"id":numb}).value.text  # в xml найти тег value id:numb, и из него вернуть то что под тегом value


today = datetime.today()
print(today)
today = today.strftime(r'%d/%m/%Y')
print(today)
playload = {'date_req': today}


url = "http://www.cbr.ru/scripts/XML_daily.asp?"
response = requests.get(url, params=playload)



if response.status_code == 200:
    xml = BeautifulSoup(response.content, 'html.parser')    #получить xml content (как в 1 модуле)

    print(get_curs("R01010"), 'рублей за Автралийский доллар')
    print(get_curs("R01235"), 'рублей за долллар США')