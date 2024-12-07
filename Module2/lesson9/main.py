def func(a,b, c=3):     #a, b - позиционные аргументы. c - именнованный аргумент
    print(a)
    print(b)
    print(c)

func(1,2)
func(1,2,35)
func(c=45, a=14, b=75)      # все аргументы именнованные




def func(a,b, *args, **kwargs):
    c = kwargs.get('c', 3)      #если c нету, то c = 3. иначе - c
    print(c)
    print(a)
    print(b)
    print(args)
    print(kwargs)

func(1,2,123,231,543,'dsdf',[1,2], c=4, one=1, two='два')   #1- a; 2- b; args - 123, 231,, 543, dsf, [1,2]; kwargs - c=4, one=1, two='два';



# код
val = None
if val == None:
    res= []
else:
    res =val
print(res)

# тот же самый код тернарным оператором в 1 строку
res = [] if val==None else val

print(res)



# генератор массива
print([ i for i in range(1,101) if i%5==0]) #от 1 до 100, делящиеся на 5

print([i**3 if i<50 else i for i in range(1,101) if i%5 ==0])   #куб чисел, делящихся на 5 от 1 до 50, и числа от 50 до 100 делящиеся на 5




len_dict = {i : len(i) for i in ['orange', 'green', 'blue']} 
print(len_dict)     # выводит длину элемента и сам элемент списка


print([i for i in range(1,251) if i % 30 ==0 or i % 31 ==0])




def func():
    return 12,45 
print(type(func()))

some_list = [(1,2,3)]
print(some_list, type(some_list))
some_tuple = tuple(some_list)
print(some_tuple, type(some_tuple))

some_dict = {(1,2,3):"Hello"}
print(some_dict[(1,2,3)])


# Хоть кортеж - неизменяемый тип данных, в него можно передать список и изменять его
tuple_2 = ([1,2,3,4], '1234543')
print(tuple_2)
tuple_2[0].append(5)
print(tuple_2)

l = [1,2,3]
m = [1,2,3]

print(l is m)   # False

l = m 

print(l is m)   # True

l.append(2) 
print(l, m)     # [1,2,3,2] [1,2,3,2]

m = l.copy()

l.append(2) 
print(l, m)     # [1,2,3,2] [1,2,3]