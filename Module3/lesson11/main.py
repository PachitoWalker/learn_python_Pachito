# Импортирую библиотеку для работы с SQlite
import sqlite3

# Создаю класс сотрудника
class User:
    def __init__(self, name, surname, gender):
        self.name = name 
        self.surname = surname 
        self.gender = gender



# Метод для создания таблицы:
def create_table(cursor):
    # Пишу sql-запрос для создания таблицы
    command = '''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT); 
    '''

    # Исполняю его
    cursor.execute(command)



# Метод для добавления сотрудника
def add_user(cursor, user):
    # Пишу sql-запрос для добавления user в таблицу
    command = '''
    INSERT INTO users (name, surname, gender)
    VALUES (?, ?, ?);
    '''

    cursor.execute(command, (user.name, user.surname, user.gender))



# Метод для выгрузки пользователей
def get_user_list(cursor):
    # Пишу sql-запрос для получения всех user из таблицы
    command = '''
    SELECT *
    FROM users;
    '''

    # Сохраняю возвращенные запросом данные в переменную
    data = cursor.execute(command)

    # Формирую список пользователей из полученных данных
    users_list = data.fetchall()

    # Вывожу данные
    print(users_list)



# Создаем cursor для работы с sqlite3
with sqlite3.connect('data.bd') as cursor:
    # Создаю таблицу
    create_table(cursor)

    # Добавляю users в таблицу
    add_user(cursor, User('Василий', 'Петров', 'Мужчина'))
    add_user(cursor, User('Григорий', 'Дуньков', 'Мужчина'))
    add_user(cursor, User('Екатерина', 'Смирнова', 'Девушка'))

    # Вывожу пользователей
    get_user_list(cursor)