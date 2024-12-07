import tkinter
import os

window = tkinter.Tk()
window.geometry('1600x900')
window.resizable(width=False, height=False)
window.config(bg='black')

text = tkinter.Label(text='Ваш Компьютер ЗАРАЖЕН', font=('Courier New', 38), fg='red', bg='black')
text.place(x=100, y=100)

cont_text = tkinter.Label(text='6', font=('Courier New', 18), fg='red', bg='black')

def count_start():
    cont_text.place(x=800, y=25)
    if int(cont_text['text']) > 0:
        cont_text['text'] = int(cont_text['text']) - 1
    else:
        cont_text['text'] = 0 
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry (str(width) + 'x' + str(height))
        img_dir = os.path.join(os.path.dirname(__file__), 'skrimer1.png')
        print(img_dir)
        photo = tkinter.PhotoImage(file=img_dir)
        potoPlc = tkinter.Label(image=photo, bg='black')
        potoPlc.image = photo
        potoPlc.place(x=0,y=0, width=width, height=height)
    window.after(1000, count_start)

def on_close():
    print("Closing")
    count_start()


window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
