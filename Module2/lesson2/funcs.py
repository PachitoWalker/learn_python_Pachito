import tgtoken
import telebot
import random
import os
from bs4 import BeautifulSoup
import requests

token = tgtoken.token
bot = telebot.TeleBot(token)

def answer(message):
    if message.text == 'Получить факт':
        send_fact(message)
    elif message.text == 'Получить пейзаж':
        send_landscape(message)
    elif message.text == 'Получить песню':
        send_mp3(message)
    elif message.text == 'Получить поэму':
        send_poem(message)

def send_poem(message):
    poem_text = '"Мне лень писать, представь что здесь написанно что-то сильное" - Дж.Стетхем'
    bot.send_message(message.from_user.id, poem_text)

def send_fact(message):
    response = requests.get('https://facts.museum/')   # получить информацию о сайте при помощи метода .get библиотеки requests
    response = response.content                        # из всей информации, полученной о сайте, в response должен остаться только content
    html = BeautifulSoup(response, 'lxml')             # BeautifulSoup сообщает, что вообще за информация должна быть в запросе. Сейчас- в requests содержится lxml
    fact = random.choice(html.find_all(class_="col-lg mb-3 p-0"))  #find_all - найти все, где class = col-lg mb-3 p-0 внутри html и 1 случайный записать в fact
    text = fact.find(class_='content').text
    url = fact.find(class_='clearfix links').a.attrs['href']

    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton('Перейти на источник', url = url)

    keyboard.add(button)

    bot.send_message(message.chat.id, text, reply_markup=keyboard)

def save_lanscape(message):
        fileID = message.photo[0].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        id = random.randint(1000000, 9999999)
        with open('imgs\land' + str(id) + '.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)

def send_landscape(message):
    file = open('imgs/' + random.choice(os.listdir('imgs')), 'rb')
    bot.send_photo(message.chat.id, file)
    file.close()

def send_mp3(message):
    name = random.choice(os.listdir(r'D:\ankun\Music'))
    mp3 = open(f'D:\\ankun\\Music\\{name}', 'rb')
    bot.send_audio(message.chat.id, mp3)    

def get_message(message):
    hi = ['Привет', 'Салют', 'Здорова', 'Салам ']   # список приветствий

    text = f'''{random.choice(hi)} ! 
    Я умею:                                                                    
    отправлять поэмы (команда /poem),
    отправлять пезажи (команда /landscape) и принимать их (просто отправь фото .jpg),
    отправлять интересные факты (команда /fact)
    ''' 

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Получить факт')
    button2 = telebot.types.KeyboardButton('Получить пейзаж')
    button3 = telebot.types.KeyboardButton('Получить песню')
    button4 = telebot.types.KeyboardButton('Получить поэму')

    keyboard.add(button1, button2, button3, button4)

    bot.send_message(message.from_user.id, text, reply_markup=keyboard)                              
    # бот отправляет сообщение (bot.send_message),
    #message.from_user.id, кому (тому кто отправил), text - что отправить

def get_interesting_fact(message):
    response = requests.get('https://facts.museum/')   # получить информацию о сайте при помощи метода .get библиотеки requests
    response = response.content                        # из всей информации, полученной о сайте, в response должен остаться только content
    html = BeautifulSoup(response, 'lxml')             # BeautifulSoup сообщает, что вообще за информация должна быть в запросе. Сейчас- в requests содержится lxml
    fact = random.choice(html.find_all(class_="col-lg mb-3 p-0"))  #find_all - найти все, где class = col-lg mb-3 p-0 внутри html и 1 случайный записать в fact
    text = fact.find(class_='content').text
    url = fact.find(class_='clearfix links').a.attrs['href']

    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton('Перейти на источник', url = url)

    keyboard.add(button)

    bot.send_message(message.chat.id, text, reply_markup=keyboard)