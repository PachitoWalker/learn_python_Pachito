import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vktoken import token
from api_centbank import get_curs
import random 


vk_token = token

# Создаю сессию работы с ботом
vk_session = vk_api.VkApi(token=vk_token)

# Создаю объект для работы с ботом
vk = vk_session.get_api()

# Создаю соединение через longpoll
longpoll = VkLongPoll(vk_session)


# Создаю обработчик событий (.listen() помогает прослушивать обрабатываемое событие)
for event in longpoll.listen():
    
    # Проверяю, что если пришло именно сообщение:
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        
        # Обрабатываю сообщение (получаю его текст)
        msg = event.text.lower()

        # Получаю id пользователя, который отправил сообщение
        user_id = event.user_id
        
        # Создаем случайный id для бота
        random_id = random.randint(1, 10_000)



# ================================================================ Команды =======================================================================
        
        #  Обрабатываю сообщение, где ксть 'привет'
        # \n - перенос на следеущую строку. Простой \ позволяет писать в print не в 1 строку, а в несколько
        if 'привет' in msg:
            # Создаю приветственное сообщение
            hello_message = f'''Привет! Я BOOOOOOOOOOOT, и могу: 
                -k : получить курс валют'''

            vk.messages.send(user_id = user_id, random_id = random_id, message = hello_message)



        # Обрабатываю команду курса валют (-k)
        if msg == '-k':  
            response = f'''{get_curs("R01235")} рублей за 1 доллар 
                {get_curs("R01239")} рублей за 1 евро 
                {get_curs("R01375")} рублей за 10 юаней 
                {get_curs("R01035")} рублей за 1 фунт стерлингов '''
            

            vk.messages.send(user_id = user_id, random_id = random_id, message = response)



        # Вывожу id и сообщение юзера
        print(user_id, msg)