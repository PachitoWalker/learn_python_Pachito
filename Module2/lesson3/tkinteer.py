import tkinter

window = tkinter.Tk()
window.geometry('1600x900')

canvas = tkinter.Canvas(window, width=600, height=600, background='white')
canvas.pack()

canvas.create_rectangle(10, 10, 110, 110, fill='yellow', outline='red')
canvas.create_rectangle(200, 10, 300, 110, fill='blue', outline='red')
canvas.create_rectangle(400, 10, 500, 110, fill='green', outline='red')

canvas.create_polygon(10,180,60,120,110,180, fill='yellow', outline = 'blue')

# рисуем домик)
canvas.create_rectangle(250, 250, 350, 350, fill= 'brown', outline='black')
canvas.create_polygon(200, 250, 300, 200, 400, 250, fill= 'brown', outline='black')
canvas.create_rectangle(275, 275, 325, 325, fill= 'yellow', outline='black')


class House:
    def __init__(self, wall_color, roof_color, number, height = 100, width = 80, ) -> None:
        self.number = number 
        self.wall_color = wall_color
        self.roof_color = roof_color
        self.height = height
        self.width = width
        self.roof = None
        self.wall = None

    def build_house(self, x, y):
        self.y_roof = y - (2.5)*self.height/13 

        self.wall = canvas.create_rectangle(x - self.width/2 + 10, self.y_roof , x + self.width/2 - 10, y + self.height/2, fill= self.wall_color, outline='black')
        self.roof = canvas.create_polygon(x - self.width/2, self.y_roof, x, y - self.height/2, x+self.width/2, self.y_roof, fill= self.roof_color, outline='black')

    def info(self):
        print('Номер дома:', self.number)
        print('Цвет стен', self.wall_color)
        print('Цвет крыши', self.roof_color)

house1 = House('green', 'brown', 1)
house2 = House('pink', 'lavender', 2)

house1.build_house(50, 50)


house1.info()
house2.wall_color = 'red'
house2.build_house(200, 50)
house2.info()

window.mainloop()
