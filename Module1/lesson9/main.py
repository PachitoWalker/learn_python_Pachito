import requests
from bs4 import BeautifulSoup
import random 

def get_interesting_fact():
    response = requests.get('https://facts.museum/')   # получить информацию о сайте при помощи метода .get библиотеки requests
    response = response.content                        # из всей информации, полученной о сайте, в response должен остаться только content
    html = BeautifulSoup(response, 'lxml')             # BeautifulSoup сообщает, что вообще за информация должна быть в запросе. Сейчас- в requests содержится lxml
    fact = random.choice(html.find_all(class_="col-lg mb-3 p-0"))   #find_all - найти все, где class = col-lg mb-3 p-0 внутри html и 1 случайный записать в fact
    print(fact.text) 
    print(fact.a.attrs['href'])

def get_event():
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-title'))
    print(fest.text)
    print(fest.a.attrs['href'])
    
def get_bash():
    response = requests.get('https://bash.ru.net/random')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    text = random.choice(html.find_all(class_='card-body')) # найти случайную карточку на сайте с классом card-body
    txt = text.find(class_='card-body') # внутри той же карточки найти такой же тег(да, их 2, одинаковых) card-body
    vote = text.find(class_="card-footer text-center row").find(class_='btn btn-sm')    # внутри 1 карточки card-body найти тег с 1 классом, а внутри него тег со 2 классом

    print(txt.text, vote.text)
    

get_bash()