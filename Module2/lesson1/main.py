# # # first_var = 22 # целое число - int
# # # second_var = 3.14 # число с плавающей точкой - float
# # # print(type(first_var), type(second_var)) #type - функция, которая указывает тип данных

# # # print (first_var + second_var)
# # # print (first_var - second_var)
# # # print (first_var * second_var)
# # # print (first_var / second_var)

# # # third_var = 'Привет, мир!' # строка - str
# # # sub_string_1 = third_var[0:6]   # это срез - 1 число - с какоко элемента (его индекс) начать срез, 2 - до какого индекса не включительно. 
# # #                                 # вывод - Привет
# # # sub_string_2 = third_var[8:11]  # мир

# # # print('M' + sub_string_2[1:] + ', n' + sub_string_1[1:] + '!')
# # # print(f'M{sub_string_2[1:]}, n{sub_string_1[1:]}!')  # это форматированная строка. перед самой строкой пишется 'f', а в скобках {} пишется
# # #                                                     # переменная. вывод с прошлой строкой один, но пишется легче

# # # print(f'Сумма {first_var} и {second_var} равна {first_var + second_var}')
# # # try:
# # #     in_var_1 = int(input('Введите первое число'))
# # #     in_var_2 = int(input('Введите второе число'))
# # # except ValueError:
# # #     print('Вы ввели недопустимое значение')
# # # else:
# # #     if in_var_1 < in_var_2:
# # #         print(f'{in_var_2} больше {in_var_1}')
# # #     elif in_var_1 == in_var_2:
# # #         print('Числа равны')
# # #     else:
# # #         print(f'{in_var_2} меньше {in_var_1}')

# # var_1 = 0.3 + 0.3 + 0.3
# # var_2 = 0.9

# # if var_1 == var_2:      
# #     print('Переменные равны')
# # else:
# #     print('Не равны')
# # # вывод - не равны. Но почему? Данный 'баг' с дробными числами есть во всех языках программирования. что бы его избежать, можно использовать:
# # if abs(var_1 - var_2) < 0.0001:
# #     print('Переменные равны')
# # else:
# #     print(var_1)
# #     print('Не равны')
# # # вывод - равны.


# for i in range(5):  #0,1,2,3,4.
#     print('smth')

# for i in range(2, 7, 2):    #2,4,6
#     print(i)

# home_list = ['кухня', 'ванная', 'гостинная', 'спальня', 'кладовка']
# home_list[2] = 'детская'    # заменяем элемент под индексом 2(гостинная) на 'детская'
# home_list.append('прихожая')    # добавить в список 'прихожая

# print(home_list)

# for room in home_list:
#     print(room)

def add(x,y):
    return x + y

print(add(5,8))


def hello():
    name = input('Как тебя зовут?')
    print(f'Приятно познакомиться, {name}')
    hello()

hello()