import random

num_list = [1, 2, 3, 4]

# Создаю итератор
list_iter = iter(num_list)  

print(list_iter)    # Вывод: ячейка памяти

# print(next(list_iter))  # Вывод: 1, сколько бы не повторялся код


# ===========================================================================


# print(next(list_iter))  # Вывод:1
# print(next(list_iter))  # Вывод:2
# print(next(list_iter))  # Вывод:3
# print(next(list_iter))  # Вывод:4
# print(next(list_iter))  # Вывод: StopIteration


# ============================================================================

# for i in list_iter:
#     print(i)    # Вывод: 1, 2, 3, 4


# ============================================================================

# Создаю свой класс-итератор (генерирует опред. кол - во случайных чисел)


class RandomIter:
    def __init__(self, limit):
        self.limit = limit      # limit - ограничение, сколько чисел генерировать
        self.reload = limit     # reload - 'перезарядка' итератора


    def __iter__(self):
        self.limit = self.reload    # limit и reload это одно и то же
        return self                 # вернет ссылку на объект
    

    def __next__(self):
        
        # Если дошли до конца итератора:
        if self.limit == 0:
            
            # Вызываем ислючение StopIteration
            raise StopIteration    
        
        # Уменьшаю limit на 1 (ведь 1 число сейчас будет сгенерированно и возвращенно)
        self.limit -= 1

        # Возвращаю рандомное число
        return random.randint(1,100)


rand_iter = RandomIter(10)


for rand_int in rand_iter:
    print(rand_int)

print('='*200)

for rand in rand_iter:
    print(rand)