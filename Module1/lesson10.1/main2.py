import fpdf
import os
fpdf.set_global('SYSTEM_TTFONNTS', os.path.join(os.path.dirname(__file__), 'fonts'))

pdf = fpdf.FPDF('P', 'cm', (10, 15))
pdf.add_font('arial', style='', fname='Arial.ttf', uni=True)
pdf.add_page()

pdf.set_font('arial', size=16)  # задать шрифт
pdf.set_text_color(0,225,0)     # задать цвет шрифта
pdf.set_fill_color(155,50,168)  # задать цвет заполнения
pdf.set_draw_color(0,0,255)     # задать цвет рамки
txt = 'I love python'

pdf.cell(10, 5, txt= txt, align='C', border = 1, fill = True)

# pdf.image('path.jpg', g=0, w=10, x=0, y=5)  # поместить картинку
pdf.output('text_fpdf.pdf')     # создать пдф