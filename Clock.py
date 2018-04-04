# Digital Clock Displaying Current UTC time.
# 
from tkinter import *
import time
from datetime import datetime, date, time

root = Tk()
time1 = ''
clock = Label(root, font=('times', 40, 'bold'), bg='black', fg='green yellow', bd='10', relief='raised')
clock2 = Label(root, font=('times', 40, 'bold'), bg='black', fg='green yellow', bd='10', relief='raised')
clock.pack(fill=BOTH, expand=1)
clock2.pack(fill=BOTH, expand=1)
def tick():
    global time1
    # get the current local time from the PC
    time2 = datetime.utcnow().strftime('%H:%M:%S')
    time3 = datetime.now().strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text="UTC Time(z):   " + time2)
        clock2.config(text="Local Time(q): " + time3)
    # calls itself every 200 milliseconds
    clock.after(200, tick)
tick()
root.mainloop(  )
