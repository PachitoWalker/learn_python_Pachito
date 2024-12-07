# Геттеры и сеттеры

class Year:
    # Инициализирую переменные для сезона и кол-ва дней в году
    def __init__(self, season, days):
        self.__season = season
        self.__days = days



    # Создаю сеттер для указания сезона
    def set_season(self, new_season):
        if new_season in ('Зима', 'Лето', 'Весна', 'Осень'):    # Проверяю, что сезон реально существует
            self.__season = new_season                          # Если сезон реален и написан без ошибок, то изменить сезон
        else:                                                   # Если же данного сезона нет, то вернуть исключение "Такого сезона нет"
            raise Exception('Такого сезона нет, пожалуйста, проверьте правильность введенной информации!!! ')
        


    # Создаю сеттер для указания кол-ва дней 
    def set_days(self, new_days):
        if new_days in (365, 366) and type(new_days) == int:    # Если это реальное кол-во дней в году, то
            self.__days = new_days                              # Изменить кол-во дней
        else:                                                   # В ином случае вернуть исключение "В коду не может быть столько дней"
            raise Exception('Простите, но в году не может быть столько дней! Перепроверьте правильность введенной информации!!! ')



    # Создаю геттер для получения сезона
    def get_season(self):
        return 'Сейчас '+ str(self.__season.lower()) + '.'



    # Создаю геттер для получения кол-ва дней
    def get_days(self):
        return 'В этом году '+ str(self.__days) + ' дней.'
    

# Проверка работоспособности:
my_year =Year('Осень', 365)

print(my_year.get_season())
print(my_year.get_days())

# my_year.set_season('Хз')        # Возникает исключение, потому что сезона "Хз" нет
# my_year.set_days('Сколько-то')  # Возникает исключение, потому что количество дней "Сколько-то" не может быть

my_year.set_season('Весна')
my_year.set_days(366)

print(my_year.get_season())
print(my_year.get_days())


# ===============================================================================================================================================================================================
print(200*'=')

# Создаю класс Человека
class Human:
    # Инициализирую его возраст и имя
    def __init__(self, name, age):
        self.__age = age  
        self.__name = name
        


    # Создаю геттер для имени с помощью @property
    @property
    def name(self):
        return 'Имя: ' + str(self.__name) + ', '
    

    # Создаю геттер для возраста с помощью @property
    @property
    def age(self):
        return str(self.__age) + ' лет.' 



    # Создаю сеттер для возвраста с помощью @property
    @name.setter
    def name(self, new_name):
        if new_name[:1] == new_name[:1].upper():                                # Проверка, что имя начинается с заглавной буквы
            self.__name = new_name                                              # Если да, изменить имя
        else:                                                                   # Иначе вызвать исключение "Имя не может начинаться с маленькой буквы"
            raise Exception('Имя не может начинаться с маленькой буквы!!!')
        
    
    # Создаю сеттер для возраста с помощью @property
    @age.setter
    def age(self, new_age):
        if new_age >= 0 and new_age <= 150 and type(new_age) == int:            # Если новый возраст больше 0 и меньше 150, а так же является целым числом
            self.__age = new_age                                                # Изменить возраст
        else:                                                                   # Иначе вызвать исключение "Некорректный возраст!!!"
            raise Exception('Некорректный возраст!!!')
        


# Проверка
mitya = Human('Митя', 16)

print(mitya.name, mitya.age)

# mitya.age = -1                  # Вызовет исключение "Некорректный возраст"
# mitya.name = 'теперьнемитя'     # Вызовет исключение "Некорректное имя"

mitya.age = 20
mitya.name = 'Дмитрий'

print(mitya.name, mitya.age)