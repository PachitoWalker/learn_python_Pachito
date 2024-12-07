import tkinter 
import random 

window = tkinter.Tk(className= 'Random')
window.geometry('1600x900')

def check():
    but.place(x=random.randint(1, 1600), y=random.randint(1, 900))

but = tkinter.Button(text='НАЖМИ', font=('Times New Roman', 24), fg='white', bg='black', command= check)
but.place(x=800, y= 450)




window.mainloop()