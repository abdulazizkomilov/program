from tkinter import *
oyna = Tk()
oyna.title('Calculator')
oyna.geometry('500x300')

son1 = Entry(bg='lightblue')
son1.place(x=148, y=30, width=200, height=40)

son = Button(text="+", bg='yellow')
son.place(x=148, y=80, width=25, height=25)

son3 = Button(text="/", bg='yellow')
son3.place(x=323, y=80, width=25, height=25)

son4 = Button(text="-", bg='yellow')
son4.place(x=208, y=80, width=25, height=25)

son5 = Button(text="*", bg='yellow')
son5.place(x=268, y=80, width=25, height=25)

son2 = Entry(bg='lightblue')
son2.place(x=148, y=130, width=200, height=40)

def farq():
	sona = son or son4 or son5 or son3
	natija.config(int(10000) - int(son2.get()))

tugma = Button(text="=", command=farq, bg='lightpink')
tugma.place(x=200, y=180, width=100, height=30)

natija = Label(text='Natija', bg='lightgreen')
natija.place(x=180, y=240, width=140, height=40)

sona = son or son4 or son5 or son3

oyna.mainloop()

