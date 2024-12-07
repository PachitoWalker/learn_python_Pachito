# # import math
import random

# # # def my_add(x,y):
# # #     c = x + y
# # #     return c

# # # a = int(input('Input A: '))
# # # b = int(input('Input B: '))
# # # z = my_add(a,b)
# # # print(z)

# # def circle_square(r):
# #     return math.pi * r * r 

# # print (circle_square((2)))

# def add(x,y):
#     return x + y
# def sub(x,y):
#     return x - y

# a = int(input('Input A:'))
# b = int(input('Input B:'))
# op = input('Input operation:')

# if op=='+':
#     print(add(a,b))
# elif op =='-':
#     print(add(a,b))
# else:
#     print('i don\'t know')
array = [10,1000,2,4,1,7,2,4,23,56]
def my_min(array):
    min = 1000000
    for i in array:
        if i < min:
            min = i
    return min

print(my_min(array)) 


def my_max(array):
    max = 0.000001
    for i in array:
        if i > max:
            max = i
    return max

print(my_max(array))


def generate_array(lbound,rbound,count):
    # array=[]
    # for i in range(count):
    #     array.append(random.randint(lbound,rbound))
    # return array 

    return [random.randint(lbound, rbound) for i in range(count)]

print(generate_array(1,100,6))