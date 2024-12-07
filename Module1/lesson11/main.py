import datetime 
from fpdf import FPDF 

pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()

pdf.image('photo.png', h=297,w=210, x=0, y=0)

pdf.add_font('comic', '', 'c:\Windows\Fonts\TIMES.TTF', uni=True)
pdf.set_font('comic', size = 37)
pdf.set_text_color(0,0,0)

friend_name = input('Введите имя человека, которому предназначена открытка\n')

pdf.cell(0, 95, ln=1)
pdf.cell(0, 20, 'Дорогой, ' + friend_name + '!', align='C', ln=1)

pdf.set_font('comic', size=18)
pdf.set_text_color(0,0,0)
message = input('Введите текст поздравления\n')
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.multi_cell(0, 20, txt = message, align='C')

today = datetime.datetime.today().strftime('%d.%m.%Y')

pdf.set_text_color(124,89,147)
pdf.cell(0, 10, txt = today, align = 'R', ln=1)

author_name = input('Введите ваше имя:\n')
pdf.cell(0,10, txt=author_name, align='R', ln=1)

pdf.output('bday_card.pdf')
