import time

# Создаем класс контекст-менеджер
class Time_working:
    def __init__(self):

        # задаем атрибут начала отсчета времени работы программы
        self.start = None


    # Метод входа в контекст-менеджер
    def __enter__(self):
        
        # Программа начала работу => сохраняем время начала работы
        self.start = time.time()    # time.time показывает время в секундах с начала эпохи
        # return self

    # Метод выхода из контекст-менеджера
    def __exit__(self, exc_type, exc_val, exc_tb):

        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(200 * '=')

        # Программа завершила работу => вычисляем время работы программы
        end = time.time()
        time_of_working = end - self.start
        print(f'Время работы программы: {time_of_working} секунд.')


        # Заглушаем вызванное исключение TypeError
        # if exc_type is TypeError:
        #     return True

        # Заглушаем любое исключение:
        if exc_type is TypeError:
            return True

# with Time_working():
#     num_list = [i for i in range(100_000_000)]  # Время работы программы

# # А если добавить такую строку:
# with Time_working() as t1:
#     num_list = [i for i in range(1_000_000)]    # None
#     print(t1)   # Время работы программы

# # Но почему None? Справка -> Почему None




# Создаем исключение (Справка -> exit)
with Time_working() as t1:
    num_list = [i for i in range(1_000_000)]
    num_list -= 'kek'   # Исключение TypeError
    print(1/0)      # Исключение TheroDisionException