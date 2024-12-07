# Импорт необходимых библиотек
from tkinter import *
import random
import time 


# Создаю окно, задаю его название, задаю его размер
window = Tk()
window.title("Ping-pong")
window.geometry("500x400")


# Следущая строка служит для выведения окна поверх других окон (как картинка-в-картинке)
window.wm_attributes("-topmost", 1)


# Создаю холст и размещаю его
canvas = Canvas(window, width= 500, height=400)
canvas.pack()


# Задаю изображение на фон игры
img_bg = PhotoImage(file = "gory.png")
canvas.create_image(250, 200, image = img_bg)


# Создаю класс Ball для мячика
class Ball:
    def __init__(self, canvas, platform, color, score, lvl):            # Экземпляр класса platform передается для отслеживания соприкосновения мяча и платформы
        self.canvas = canvas 
        self.platform = platform   
        self.oval = canvas.create_oval(200,200,  215,215, fill=color)   # Создал круг
        self.score = score
        self.lvl = lvl


    # Начальная скорость по x и y
        self.x = random.choice((-2, 2))
        self.y = -2


    # Касание нижней части сцены
        self.touch = False 


    # Скорость шара
        self.speed_x_y= 3
        


    # Проверка касания шарика платформы
    def touch_platform(self):
        platform_position = self.canvas.coords(self.platform.rect)      # Определяю координаты платформы
        ball_position = self.canvas.coords(self.oval)                   # Определяю координаты шара


        # Проверка, находится ли мяч в ширине платформы
        if ball_position[2] >= platform_position[0] and ball_position[0] <= platform_position[2]:           # Индексы: x1 = 0, y1 = 1, x2 = 2, y2 = 3
            if ball_position[3] >= platform_position[1] and ball_position[3] <= platform_position[3]:
                self.score.hit()
                if self.score.score % 4 == 0 and self.score.score != 0:
                    self.lvl.lvl_up()
                    self.speed_сhange()
                return True                
        return False



    # Метод для изменения скорости
    def speed_сhange(self):
        self.speed_x_y += random.choice((1, -1, 0))
        self.platform.speed_x += random.choice((1, 0))



    # Движение для мяча
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)                     # move двигает выбранные объекты по холсту на x и y (на холсте canvas переместить self.oval на self.x и self.y)
        position = self.canvas.coords(self.oval)                        # Определяю координаты платформы
        if position[1] <=0: 
            self.y = self.speed_x_y
        if position[3] >= 400:
            self.touch = True
        if position[0] <= 0:
            self.x = self.speed_x_y
        if position[2] >=500:
            self.x = -self.speed_x_y
        # При столкновении:
        if self.touch_platform() == True:
            self.y = -self.speed_x_y





# Создаю класс для платформы
class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas 
        self.rect = canvas.create_rectangle(230,300, 330,310, fill=color)
        self.x = 0


    # Бинд клавиш на выполнение определенных комманд
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
    

    # Начальная скорость платформы
        self.speed_x = 3


    # Функции для движения платформы влево и вправо
    def left(self,event):
        self.x = -self.speed_x


    def right(self, event):
        self.x = self.speed_x


    # Движение для платформы
    def draw(self):
   
        # move - метод класса Canvas, который позволяет перемещать фигуру(1 аргумент ) на какой-то x и какой-то y (2 и 3 аргументы соответственно)
        self.canvas.move(self.rect, self.x, 0)
        
        
        # Узнаю координаты платформы
        position = self.canvas.coords(self.rect)


        # Если платформа выходит за край: 
        if position[0] <= 0 or position[2] >=500:
            self.x = 0



# Создаю класс для очков
class Score:
    def __init__(self, canvas, color):
        self.canvas = canvas 
        self.score = 0
        self.score_text = canvas.create_text(450, 10, text = f'score: {self.score}', font = ("Arial", 15), fill = color)


    # Метод, при отбиении платформой шара
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.score_text, text = f'score: {self.score}')





# Создаю класс для уровня
class Level:
    def __init__(self, canvas, color):
        self.canvas = canvas 
        self.lvl = 0
        self.lvl_text = canvas.create_text(50, 10, text = f'lvl: {self.lvl}', font = ("Arial", 15), fill = color)


    # Метод поднятия уровня
    def lvl_up(self):
        self.lvl += 1
        self.canvas.itemconfig(self.lvl_text, text = f'lvl: {self.lvl}')





# Создаю объекты платформы, очков, уровня и шара    (как можно заметить, используется ассоциация)
platform = Platform(canvas, "purple")
score = Score(canvas, 'black')
lvl = Level(canvas, 'black')
ball = Ball(canvas, platform, "red", score, lvl)





# Самостоятельно делаем window.mainloop()
while True: 
    if ball.touch == False:
        ball.draw()
        platform.draw()
    else:
        break
    window.update()
    time.sleep(0.01)





# # Композиция и ассоциация

# class Head:
#     pass 

# class Legs:
#     pass

# class Hands:
#     pass

# class Body:
#     pass 

# class PeopleCompozition:
#     def __init__(self):
#         # Композиция - создаю экземпляры других классов внутри класса 
#         self.head = Head
#         self.legs = Legs
#         self.hands = Hands 
#         self.body = Body 

# people1 = PeopleCompozition()




# class PeopleAssotiation:
#     def __init__(self, head, legs, hands, body):
#         # Ассоциация = передаю экземпляры класса в параметры
#         self.head = head 
#         self.legs = legs 
#         self.hands = hands 
#         self.body = body

# head1 = Head()
# legs1 = Legs()
# hands1 = Hands()
# body1 = Body()

# people2 = PeopleAssotiation(head1, legs1, hands1, body1)
