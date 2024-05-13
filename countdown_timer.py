from tkinter import *
import datetime as dt
import time

root = Tk()
root.geometry('300x300')
btn1 = Button(root, text='Show window')
btn2 = Button(root, text='Close window')
hours = Entry(root)
min = Entry(root)
sec = Entry(root)

hours.pack()
min.pack()
sec.pack()

def show_timer():
    h = int(hours.get())
    m = int(min.get())
    s = int(sec.get())
    total = h*3600 + m*60 + s
    def set_time():
        nonlocal total
        if total > -5:
            timer = dt.timedelta(seconds=total)
            label.config(text=f'{timer}')
            total -= 1
            countdown_timer.after(1000, set_time)
        else:
            label.config(text='Tiempo terminado')
    btn1.pack_forget()
    btn2.pack()
    countdown_timer = Toplevel(root)
    countdown_timer.geometry('600x600')
    def hide_timer():
        btn2.pack_forget()
        btn1.pack()
        countdown_timer.destroy()
        countdown_timer.update()
    btn2.config(command=hide_timer)
    label = Label(countdown_timer)
    set_time()
    label.pack()
    #Label(countdown_timer, text='This will be the timer.').pack()

btn1.pack()
btn1.config(command=show_timer)

root.mainloop()