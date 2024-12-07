from bs4 import BeautifulSoup
from tkinter import *
import requests
from datetime import datetime


window = Tk()
window.configure(bg='black')    # сделать фон окна черным
window.geometry("900x650+300+300")  # окно с размеров 900x560 с x= 300, y = 300

label = Label(window, text="Курс валют \n ИМБанк:", font = ("Comic", 24), fg = "black")  #Создать текст с тестом = ..., шрифтом =... размером 24, цветом шрифта = black
label.place(y=0, x= 550)   # разместить текст на y=25, x=450


img = PhotoImage(file="bank_logo.png")  # Фотография = PhotoImage(file = 'путь до фото')
logo = Label(window, image=img) # logo = виджет в окне, с фотографией = img
logo.place(x=0, y=0)    #разместить

url = "http://www.cbr.ru/scripts/XML_daily.asp?"    # url

today = datetime.today().strftime("%d/%m/%Y")   # сегодняшняя дата в формате день/месяц/год
param = {'date_req':today}  # параметр = по ключу date_req получить today

response = requests.get(url, params=param)  # ответ = из запроса получить(запрос по ссылке, параметры = параметр)
xml = BeautifulSoup(response.content, 'lxml')   # xml = разбор контента в ответе на lxm

def get_course(chr):
    chr = xml.find("charcode", text=chr)    # chr = в xml найти тег charcode, text = chr
    chr = chr.parent    # chr = тег выше прошлого chr
    chr = chr.value     # chr = значение прошлого chr
    return chr.text     # вернуть текст прошлого chr



textt = Label(window, text= 'Курс валют на сегодня: ', font=('Comic', 24), fg='black')
textt.place(x=450, y = 100)
usd_course = Label(window, text = '$ = ' + str(get_course('USD')[0:5]), font=('Comic', 24), fg = 'red')
usd_course.place(y=175, x=450)

eur_course = Label(window, text = '€ = ' + str(get_course('EUR')[0:5]), font=('Comic', 24), fg = 'red')
eur_course.place(y=225, x=450)

print(get_course("USD"))

window.mainloop()