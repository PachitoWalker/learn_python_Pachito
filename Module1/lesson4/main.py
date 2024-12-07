import random

# days = 7
# temp_sum = 0
# for i in range (days):
#     temp = int(input("Сколько градусов на улице сегодня? "))
#     temp_sum += temp 

# print("Средняя температура на улице за 7 дней: ", temp_sum / days)



# Вариант преподавателя

# wheather = []
# DaysCount = 7

# for i in range(DaysCount):
#     x = int(input("Введите температуру: "))
#     wheather.append(x) 

# meanTemp = sum(wheather) / DaysCount
# print("Средняя температура за " + str(DaysCount) + "дней :" + str(meanTemp))

# a = int(input("a "))
# b = int(input("b "))

# if a > b:
#     b += 1
# elif a == b:
#     a += 1
#     b += 1
# else:
#     print('a меньше b')

# print("a ", a , ". b ", b)


prog = random.randint(1,10)
print(prog)
user = int(input('Введите число от 1 до 10: '))


if user == prog:
    print("Поздравляю, вы угадали!")
# elif prog - user == 1 or prog - user == -1:       # конечно, можно было бы сделать так. но есть способ попроще)
elif abs(prog - user) == 1:     # иначе если МОДУЛЬ числа равен 1. Напомню, что модуль вссегда пложителен. Модуль -1 = 1. Модуль -15 = 15
    print("Вы почти угадали!")
else:
    print("Вы не угадали! попробуйте снова!")