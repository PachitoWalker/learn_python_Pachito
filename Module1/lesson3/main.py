import random 

facts = ["fact1", "fact2", "fact3", "fact4"]
# print(random.choice(facts))

rand = random.randint(1,10)
# print(rand)

# print(facts)
random.shuffle(facts)
# print(facts)

# ==================================================================================================================================

# sum = 0
# for month in range(1, 7):
#     zp = int(input('Введите свой доход за этот месяц: '))
#     sum = sum + zp 

# itog = sum * 0.3
# print("За пол года вы отложили: ", itog)


# ===================================================================================================================================

# Способ перевернуть массив:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rev = []

for i in range(len(array), 0, -1):
    # print(array[i-1])
    rev.append(array[i-1])

print(array)
print(rev)