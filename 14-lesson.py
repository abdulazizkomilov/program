from datetime import datetime 
from tkinter import *

oyna = Tk()
oyna.title('Dasturcha :) ')
oyna.geometry('300x300')

natija = Label(text="Natija", bg="pink")
natija.place(x=90, y=135, width=120, height=40)

yil = Entry()
yil.place(x=75, y=50, width=150, height=30)

def farq():
	bugun = datetime.today()
	natija.config(text=bugun.year - int(yil.get()))

tugma = Button(text='Hisoblash', command=farq)
tugma.place(x=90, y=90, width=120, height=40)


oyna.mainloop()