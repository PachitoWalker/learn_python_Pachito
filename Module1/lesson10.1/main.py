import random
i = 1
while i<= 10:
    print(i**2)
    if (i**2) % 2 != 0:
        i+=1
    else:
        i+=2

num = int(input('Введите число: '))
cur_num = 1
while cur_num <= num:
    print(cur_num)
    cur_num += 1

films = ['форсаж', 'терминатор', 'аватар', 'оно 2', 'властелин колец',
         'железный человек', 'джон уик', 'невидимая сторона', 'Мстители',
         'мандалорец', 'конан-варвар', 'интерстеллар', 'человек-паук', 'матрица',
         'законопослушный гражданин', 'очень странные дела']
print('Привет! Сейчас я буду показывать тебе случайный фильм. Тебе понравится =) ')
while True:
    print(random.choice(films))
    answer = input('Нужно еще? Y/N: ')
    if answer == 'N':
        break
    while answer != 'Y' and answer != 'N':
        answer = input('Пожалуйста, введите ответ в формате Y/N:' )
# day = int(input('Сколько ты получаешь в день? '))
# pay_per_day = int(input('Сколько % ты готов откладывать в день? '))
# mark = int(input('Сколько ты хочешь накопить? '))
# sum = 0
# days = 0

# while sum < mark:
#     sum += day * (pay_per_day / 100)
#     days += 1
    
# print(sum, 'ты накопишь за ', days, ' дней.')