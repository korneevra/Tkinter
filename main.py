from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    # lbl.configure(text='I asked you!', font=('Times new roman', 50))
    res = f'Hi {txt.get()} + {combo.get()}'
    lbl.configure(text=res)


win = Tk()
win.title("Hi Tkinter")
win.geometry('500x400')
lbl = Label(win, text='Label text!', font=('Arial Bold', 20))
lbl.grid(column=0, row=0)
txt = Entry(win, width=10, state='disabled')
txt.grid(column=1, row=0)
txt.focus()
btn = Button(win, text='Do not touch', bg='red', fg='blue', command=clicked)
btn.grid(column=1, row=1)
combo = Combobox(win)
combo['values'] = (1, 2, 3, 4, 5, 'text')
combo.current(2)
combo.grid(column=3, row=0)

win.mainloop()
