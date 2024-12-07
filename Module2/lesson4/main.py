from tkinter import *
import random

# Создаем окно, задаем размер и размещаем
window = Tk()

w = 600
h = 600

window.geometry(f'{w}x{h}')


# создаем холст
canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)  #Что бы разместить холст в окно, используем in_


# Фон игры
bg_photo = PhotoImage(file='bg_x.png')

# Добавляем рыцаря
class Knight:
    def __init__(self) -> None:
        # Координаты рыцаря:
        self.x = 70
        self.y = h//2

        # Скорость рыцаря:
        self.v = 0

        # Изображение рыцаря
        self.photo = PhotoImage(file='knight.png')
    
    def up(self, event):
        self.v = -2

    def down(self, event):
        self.v = 2

    def stop(self, event):
        self.v = 0

knight = Knight()


# Создаем класс для драконов
class Dragon:
    def __init__(self) -> None:
        self.y = random.randint(100, 500)
        self.x = 750    # специально x за холстом, что бы не было видно, откуда драгон появился
        self.v = random.randint(1, 4)
        self.photo = PhotoImage(file='dragon.png')

dragons = []
for i in range(4):
    dragons.append(Dragon())



# Создаем функцию для отрисовки игры
def game():
    canvas.delete('all')    #Удаляем все с холста (каждый раз, с каждым кадром, будет отрисовываться новая картинка)
    canvas.create_image(300,300, image=bg_photo)    #добавляем фон на холст
    knight.y += knight.v    #задаем скорость рыцарю
    canvas.create_image(knight.x, knight.y, image=knight.photo)     #добавляем рыцаря на холст

    
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)
        
        
    window.after(5, game)   #Создаем задержку для отрисовки кадров игры (картинка меняется каждые x мс)


game()

window.bind('<Key-Up>', knight.up)      #Биндим кнопки. Когда окно открыто и мы нажимаем <Key-Up> (стрелочка
window.bind('<Key-Down>', knight.down)  #вверх), то используется метод up объекта knight. аналогично со всеми
window.bind('<KeyRelease>', knight.stop)#<KeyRelease> - кнопка не нажата

window.mainloop()