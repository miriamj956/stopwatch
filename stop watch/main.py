from tkinter import *
import time
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("stopwatch")

hour = StringVar()
hour.set("00")

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

hourEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=second)
secondEntry.place(x=180, y=20)

def settime():
    try:
        temp = (int(hour.get())*3600) + (int(minute.get())*60) + (int(second.get())) #converts into seconds
    except: 
        print("Please enter a number")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins, 60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time countdown", "Time's up")

        temp -=1


button1= Button(root, text="set time", command=settime)
button1.place(x=130, y=70)


root.mainloop()
