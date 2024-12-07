import tkinter

current_question = 0
score = 0

window = tkinter.Tk()
window.geometry("1920x1080")

label_title = tkinter.Label(text='TEST', font=('Times New Roman', 24), fg='white', bg='black')
label_title.place(x=0,y=0, width=1920, height=50)

def check():
    global score, current_question
    answer  = var.get()
    if facts[current_question]['right'] == answer:
        score += 1
    if current_question < len(facts)-1:
        current_question += 1
        fact['text']=facts[current_question]['text']
    else:
        points_label = tkinter.Label(text = 'SCORE: ' + str(score), font= ('Times New Roman', 40), fg= 'red', bg='white')
        points_label.place(x=0, y=0, width=700, height=250)
    scores = tkinter.Label(text=score, font=('Times New Roman', 12), fg = 'white', bg ='red')
    scores.place(x=1800, y= 10)



facts = [
    {'text':'Земля плоская?', 'right':0},
    {'text':'У котов 1 хвост', 'right':1},
    {'text':'На руке человека 5 пальцев?', 'right':1},
    {'text':'2*2 = 4?', 'right':1},
    {'text':'Меркурий ближе всего к солнцу?', 'right':1},
]

fact = tkinter.Message(text= facts[current_question]['text'], font=('Times New Roman', 22), fg= 'white', bg = 'black', width=600, borderwidth=0 )
fact.place(x=10, y=100)



var = tkinter.IntVar()
rb_true = tkinter.Radiobutton(text='True', value=1, variable= var)
rb_false = tkinter.Radiobutton(text='False', value=0, variable= var)

rb_true.place(x=10, y= 220)
rb_false.place(x=10, y=270)

btn_check = tkinter.Button(text='Ответить', font=('Times New Roman', 24), fg = 'white', bg = 'black',command=check)
btn_check.place(x=800, y=700)

window.mainloop()