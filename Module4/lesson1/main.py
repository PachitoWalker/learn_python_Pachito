import time

# Создаюю функцию для подсчета уникальных символов
def letterCount(line):
    for letter in set(line):
        # Подсчет символов
        counter = 0
        for nextletter in line:
            if letter == nextletter:
                counter += 1
        print(counter, letter)



# Замеряю время работы программы
start_time = time.time()
letterCount('aabcccdde'*10000)  # У меня вышло примерно 202 секунды. Если же сделать из line множество - set(line) в 5 строке, то выходит примерно
print(time.time() - start_time)

print(set('aaaabbbcccccdddddde'*10000))      