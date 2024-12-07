class Singletone(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance 
    
# s и sl - одно и то же
s = Singletone()
print("Created", s, id(s))
sl = Singletone()
print("created", sl, id(sl))



def repair_deco(func):  # Декоратор 
    def wrapper(x,y):  # Функция, принимает аргументы func x и y
        return func(x,y) - 1    # Возвращает результат func(x,y), отнимая от нее 1
    return wrapper  # Заменяем "сломанную" функцию на рабочую


@repair_deco
def add(x,y):
    return x + y + 1

print(add(1,2))

# =======================================================
from datetime import datetime

# ------------------ Создаю декоратор для отслеживания времени работы функции -------------------------
def time_of_working(func):  
    def wrapper(x):     # x - аргумент функции, которую я передаю
        start_time = datetime.now()
        res = func(x)   # резулютат = запуск функции с ее аргументом x
        end_time = datetime.now()
        print(f"time: {end_time - start_time}")
        return res
    return wrapper


# ------------------ Пишу два способа генерации массива: через генератор и через for и проверяю декоратором, какой работает быстрее --------------------

@time_of_working
def get_list_1(num):
    return([x for x in range(num) if x % 2])

@time_of_working
def get_list_2(num):
    new_list = []
    for x in range (num):
        if x % 2:
            new_list.append(x)
    return new_list


list_1 = get_list_1(59939999)    # Работает быстрее ( как и ожидалось) )
list_2 = get_list_2(59939999)