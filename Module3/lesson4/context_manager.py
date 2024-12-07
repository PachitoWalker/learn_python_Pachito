# Один вариант открытия файла
file = open('my_file.txt', 'w')
file.write('Hello world!')
file.close()


# А вот другой, и, на самом деле, более предпочтительный. Смотри Справку
with open('my_file.txt', 'w') as file:
    file.write('Hello World!')
    print(file.closed)      # False - файл открыт

print(file.closed)          # True - файл закрыт



# Создаем свой контекствный менеджер
import contextlib

@contextlib.contextmanager
def str_reverse(my_str):
    print('Входим в контекстный менеджер')
    yield my_str[::-1]
    print('Выходим из контекстного менеджера')

with str_reverse('Hello, world!') as reversed_str:
    print(f'Выполняется код: {reversed_str}')




# =====================================

def some_func(*args, **kwargs):
    print('args: ', args, '. Kwargs: ', kwargs)
    print('Type args: ', type(args), '. Type kwargs: ', type(kwargs))

some_func(1, 2, a=3, b=5, c=6, e=7, f=8)
