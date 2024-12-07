from pprint import pprint

def is_odd(a):
    # Проверить на нечетность можно 2 способами. Первый:
    # if a % 2 > 0:
    #     return True
    # else:
    #     return False
    
    # Второй. Работает, тк a % 2 != 0 само по себе логическое выражение
    return a % 2 == 0
print(is_odd(5))



data = [5, 1, 2, 4, 3, 5, 10, 8, 9]
# key - аргумент, который принимает метод сортировки.
print(sorted(data, key = is_odd))


# По умолчанию массивы со строками сортируются по алфавиту
a = ['asdf', 'oldj', 'blo', 'karv']
print(sorted(a))


# key = len сортирует по длине. reverse = True - перевернет массив
print(sorted(a, key = len, reverse= True))


# И вот наконец - то лямбда-функция: делает то же, что и в строке 18 с объявленной функцией is_odd, но без ее объявления. 
print(sorted(data, key= lambda n: n % 2 == 0))





telNums = [
    {
        'name':'iPhone 14',
        'brand':'Apple',
        'price':1200
    },
    {
        'name':'Samsung Galaxy A53',
        'brand':'Samsung',
        'price':500
    },
    {
        'name':'Google Pixel 7',
        'brand':'Google',
        'price':650
    },
    {
        'name':'iPhone 12',
        'brand':'Apple',
        'price': 1000
    }
]


# Отсортирует telnums по цене (по умолчанию - по возрастанию ее). pprint делает выводы в консоли более читаемым, можешь сам сравнить этот вывод с print и pprint
pprint(sorted(telNums, key = lambda p: p['price'])) 



# Функция filter()
data = [2, 1, 2, 4, 3, 6, 10, 8, 9]

# В отличии от sorted, filter возвращает ячейку памяти, это ленивые вычисления. Если из этой ячейки сделать список, то он, в отличии от sorted, выведет только то, что соответствует условию
pprint(list(filter(lambda n: n % 2 == 0, data)))

# Выведет толькосмартфоны с брендом Apple из списка telNums
pprint(list(filter(lambda apple: apple['brand'] == 'Apple', telNums)))



# Функция map()
# 1 2 3 4  -> ['1', '2', '3', '4'] ? [1 2 3 4]

# Вот 1 способ положить эти числа в переменную
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(f'Первое число: {num1}, второе число: {num2}, третье число: {num3}')

# А вот второй: split - делить строку по пробелам => input().split() - делить ввод по пробелам. map(int, input.split()) делит по пробелам ввод, преобразует их в int и задает по порядку в указанные переменные
num1, num2, num3 = map(int, input().split())
print(f'Первое число: {num1}, второе число: {num2}, третье число: {num3}')



names = ['Ваня', 'Петя', 'Настя']
surnames = ['Петров', 'Иванов', 'Сидорова']

# А здесь map не запихивает получившиеся значение в переменные. Я из этих значений делаю список. Так же здесь видно, что lambda может быть не одна.
fulnames = list(map(lambda name, surname: f'{name} {surname}', names, surnames))
print(fulnames)

# А вот так писать нельзя: вылетит с исключением.
# full_names = list(lambda name, surname: f'{name} {surname}', names, surnames)   # брать name из names и surname из surnames, вывести name + ' ' + surname
# print(full_names)