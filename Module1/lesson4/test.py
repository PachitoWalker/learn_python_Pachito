a = 5 ** 3  #5 в степени 3
print(a)


print("Как сказал один поэт \"я хз\" ") # что бы написать цитату, можно использовать либо другой вид кавычек, либо "экранировать" 
                                        # с помощью знака "\"
print("Первая строка \nВторая строка")  # \n позволяет вывести текст после этого символа на другую строку

# Но вот проблема: нужно написать такой путь  "С\user\name". Python посчитает, \name - это знак перевода на следущую строку символов
# ame. что бы это исправть, можно сделать строку необработанной, добавив передней r
print(r"C\user\name")

# что бы повторить n раз одну строку, надо перед ней написать n *. пример:
print(3 * 'up')   #вывод - upupup

print(list(range(10)))  # выведется список, начинающийся 1 и заканчивающийся 10. То есть range можно использовать и без for.

