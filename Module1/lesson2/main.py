# film = ['Бриллиантовая рука', 'Бэтмен', 'Звездные войны']
# print(film)

# # Выведется элемент из film с index 0. Это 'Бриллиантовая рука'
# print(film[0])

# # Присваиваем переменной favorite значение Бэтмен из массива
# favorite = film[1]
# print(film)

# # Привсваиваем этой же переменной значение Звездные войны, при этом удаляя этот элемент из массива
# favorite = film.pop(2)
# print(film)

# # Удалить элемент из массива film с индексом 0 (сейчас это Бриллиантовая рука)
# del film[0]
# print(film)

# # Удалить элемент из массива film со значением Бэтмен
# film.remove('Бэтмен')
# print(film)





# ==================================================================================================================================


# facts = [
#     'fact1',
#     'fact2',
#     'fact3',
#     'fact4'
# ]

# num_fact = int(input('Введите номер факта, который вы хотите узнать'))
# print(facts[num_fact - 1])      



# ====================================================================================================================================



marks = [4,5,4,5,5,3,4,5]
print(marks.count(5))


print('Средний балл: ', sum(marks) / len(marks), '. Лучшая оценка: ', max(marks), '. Худшая оценка: ', min(marks))

marks.sort()
print(marks)