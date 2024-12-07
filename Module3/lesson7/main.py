# # Создаю класс для описания товара
# class Product:

#     # Инициализирую имя, вес и цену товара
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price

    

#     # Магический метод add
#     def __add__(self, other):
        
#         # Проверяю, что работаю именно с объектом класса
#         if isinstance(other, Product):      # Тут внимательно: Проверяем, что второй объект - класс Product, и тогда self.price 1 объекта класса Product (по умолчанию, ведь у меня __add__ находится
#                                             # в классе Product, и начинает выполнятся только если 1-й объект - его экземпляр) складываем с other.price (тот же self.price для other объекта)
#             return self.price + other.price   
        

#         if isinstance(other, int):          # Этот же блок выполняется в случае, если второй объект - экземпляр класса int (ты же помнишь, да, что int - это тоже класс?). Тогда нужно сложить 
#                                             # self.price 1 объекта класса Product (уже объяснял почему) со значением other - в данной ситуации other это целое число.
#             return self.price + other
        


# product1 = Product('Видеокарта', 2000, 25000)
# product2 = Product('Процессор', 200, 20000)


# # 1 способ. Плохо, тк price может быть приватным полем. Зато не нужен магический метод __add__
# total_price = product1.price + product2.price
# print('1 способ. Сумма: ', total_price)   


# # 2 способ. Предпочиттельней
# total_price = product1 + product2   # сработает, т.к есть метод __add__ в классе
# print('2 способ. Сумма: ',total_price)


# # Непредвиденная ситуация:
# total_price = product1 + 3000       # сработает, т.к указали в __add__ что делать, если 2-е значение - int
# print('Сумма: ',total_price)





# =====================================================================================================================================================================================================
# Алхимия



# Импорт необходимых библиотек
import tkinter 
import random 


# Создаю окно и задаю его геометрию
window = tkinter.Tk()
window.geometry("800x700")





# Создание классов элементов
class Fire:
    image = tkinter.PhotoImage(file='images/fire.png').subsample(8, 8)  # метод subsample, если очень грубо говоря, уменьшает изображение в a раз по оси x и в b раз по оси y
    
    
    # Если экземпляры Fire и Earth соединились:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay()
        elif isinstance(other, Water):
            return Vapor()
        else:
            pass



class Earth:
    image = tkinter.PhotoImage(file='images/Earth.png').subsample(8, 8)



    # Если экземпляры Fire и Earth соединились:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay()
        elif isinstance(other, Wind):
            return Dust()
        else:
            pass



class Water:
    image = tkinter.PhotoImage(file='images/water.png').subsample(8, 8)


    def __add__(self, other):
        if isinstance(other, Wind):
            return Ice()
        elif isinstance(other, Fire):
            return Vapor()
        else:
            pass



class Wind:
    image = tkinter.PhotoImage(file='images/wind.png').subsample(8, 8)

    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()
        else:
            pass



class Ice:
    image = tkinter.PhotoImage(file='images/ice.png').subsample(8, 8)

    

class Clay:
    image = tkinter.PhotoImage(file='images/clay.png').subsample(8, 8)



class Dust:
    image = tkinter.PhotoImage(file='images/dust.png').subsample(8, 8)



class Vapor:
    image = tkinter.PhotoImage(file='images/vapor.png').subsample(8, 8)





# Создаю функцию для движения
def move(event):    
    
    
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)   # список, find_ovelapping создает что-то на подобии хитбокса, возвращает id пересекающихся хитбоксов
                                                                                        # event.x и event.y - координаты курсора
    
    
    # Перетакскиваем изображение за курсором
    
    canvas.coords(images_id[0], event.x, event.y)
    print(images_id)


    # Соединение элементов
    if len(images_id) == 2:
        
        # присваиваем id пересекающихася элементов переменным
        elem_id_1 = images_id[0]
        elem_id_2 = images_id[1]


        element1 = elements[elem_id_1 - 1]
        element2 = elements[elem_id_2 - 1]


        # Создаем новый элемент
        new_element = element1 + element2


        # Проверка, появился ли новый елемент
        if new_element:
            element_types = []
            for elem in elements:
                element_types.append(type(elem))
            # Проверка, что такой же элемент еще не создан
            if type(new_element) in element_types:
                pass
            else:   
                # Если да, то отрисовываем новый элемент
                canvas.create_image(event.x, event.y, image = new_element.image)
                elements.append(new_element)
                print(elements)





# Создание и размещение холста 
canvas = tkinter.Canvas(window, width = 800, height= 700)   
canvas.pack()


# Создаю список с элементами
elements = [Earth(), Water(), Wind(), Fire()]


# Размещаю элементы из списка на холсте
for elem in elements:
    canvas.create_image(random.randint(50, 750), random.randint(50, 650), image = elem.image)


# Бинд левой кнопки мыши с перемещением картинки
window.bind('<B1-Motion>', move)


window.mainloop()