from tkinter import *

window = Tk()
window.geometry('1920x1080+0+0')    # axb - размер окна, + c + e - x и y размещения окна

label = Label(window, text='smth', font = ("Arial", 18), bg="#d899ff", fg = "gold")
label.place(x=100, y=100)

label["text"] = "какой-то текст"
count = 10

def func():
    global count
    count += 1
    btn["text"] = f"Клик {count}"

btn = Button(window, text="Click", font=("Arial", 16), bg="#d899ff", fg="gold", command=func)
btn.place(x=200, y=200)

window.mainloop()
