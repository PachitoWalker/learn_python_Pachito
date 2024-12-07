from vktoken import token
import vk_api
from api_centbank import get_curs

# Создаем объект для управления ботом
vk = vk_api.VkApi(token=token)

# Авторизуем токен
vk._auth_token()

# Получение сообщений из чата. Заходим в документацию по ссылке: https://dev.vk.com/ru/guide
# messages = vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})

# Вывод сообщений (id написавшего, текст последнего сообщения, номер сообщения с учетом удаленных)
# print(messages.get('items')[0].get('last_message').get('from_id'), messages.get('items')[0].get('last_message').get('text'), messages.get('items')[0].get('last_message').get('id'))



# Создаем цикл работы бота
while True:
    messages = vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})
    # Проверка, что есть хотя бы одно новое сообщение
    if messages['count'] > 0:
        user_id = messages.get('items')[0].get('last_message').get('from_id')
        text_message = messages.get('items')[0].get('last_message').get('text')
        num_of_message = messages.get('items')[0].get('last_message').get('id')

        # Отправим сообщение пользователю, что его сообщение получено
        # vk.method('messages.send', {'peer_id': user_id, 'random_id':num_of_message, 'message': 'Ваше сообщение получено!'})

        if text_message.lower() == 'привет':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': num_of_message, 'message': 'Добрый день!'})
        elif text_message.lower() == 'курс доллара':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': num_of_message, 'message': get_curs('R01235')})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': num_of_message, 'message': 'Я вас не понимаю!'})