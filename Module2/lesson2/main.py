from funcs import *


# команда для получения приветствия
@bot.message_handler(commands=['start', 'help'])    # создаем декоратор для сообщений, bot - переменная, где хранится бот, метод message_handler, content_types - что обрабатывает бот
def one(message):
    get_message(message)

# команда для получения песни
@bot.message_handler(commands=['mp3'])
def two(message):
    send_mp3(message)


# команда на получение изображения пейзажа
@bot.message_handler(commands=['landscape'])
def three(message):
    send_landscape(message)


# если в бота отправляется фото, то оно должно загружаться в базу пейзажей
@bot.message_handler(content_types=['photo'])
def four(message):
    save_lanscape(message)


# команда для получения какого-либо интересного факта
@bot.message_handler(commands=['fact'])
def five(message):
    send_fact(message)


# команда для получения поэмы 
@bot.message_handler(commands=['poem'])
def six(message):
    send_poem(message)


@bot.message_handler(content_types=['text'])
def eight(message):
    answer(message)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)