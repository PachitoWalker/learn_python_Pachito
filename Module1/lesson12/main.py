import telebot
import random
from bs4 import BeautifulSoup
import requests
import os
from token import token

token = token.token
bot = telebot.TeleBot(token)

def get_interesting_fact():
    response = requests.get('https://facts.museum/')   # получить информацию о сайте при помощи метода .get библиотеки requests
    response = response.content                        # из всей информации, полученной о сайте, в response должен остаться только content
    html = BeautifulSoup(response, 'lxml')             # BeautifulSoup сообщает, что вообще за информация должна быть в запросе. Сейчас- в requests содержится lxml
    fact = random.choice(html.find_all(class_="col-lg mb-3 p-0"))   #find_all - найти все, где class = col-lg mb-3 p-0 внутри html и 1 случайный записать в fact
    return(fact.text) 
    # print(fact.a.attrs['href'])
    
@bot.message_handler(commands=['landscape'])
def message_processing(message):
    file = open('imgs/' + random.choice(os.listdir('imgs')), 'rb')
    bot.send_photo(message.chat.id, file)
    file.close()

@bot.message_handler(commands=['fact'])
def message_processing(message):
    bot.send_message(message.chat.id, get_interesting_fact())

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = '"Мне лень писать, представь что здесь написанно что-то сильное" - Дж.Стетхем'
    bot.send_message(message.from_user.id, poem_text)
    
@bot.message_handler(content_types=['text'])    # создаем декоратор для сообщений, bot - переменная, где хранится бот, метод message_handler, content_types - что обрабатывает бот
def get_text_message(message):
    if message.text == 'привет' or message.text == 'Привет':    # если мы извлекли из сообщентй, отправленных боту 'привет', то
        hi = ['Привет', 'салют', 'здорова', 'салам ']   # список приветствий
        bot.send_message(message.from_user.id, random.choice(hi))   # бот отправляет сообщение (bot.send_message),
                                                                            #message.from_user.id, кому (тому кто отправил), text - что отправить
    elif message.text == 'Как дела?' or message.text == 'Как ты?':
        bot.send_message(message.from_user.id, 'Хорошо, спасибо что спросил)')
    else:
        bot.send_message(message.from_user.id, 'меня тебя не понимати')


id = 4

@bot.message_handler(content_types=['photo'])
def save_photo(message):
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        id =+ 1
        with open('imgs\land' + str(id) + '.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)


bot.polling()