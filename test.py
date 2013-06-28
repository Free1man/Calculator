from Tkinter import *

import tkMessageBox

import datetime

import ttk

def writeEventToFile(event):


    data = open("data2.txt", "a")
    data.write(date.get()+" ")
    data.write(eventName.get()+" ")
    data.write(reminder.get()+"\n")
    data.close()

    text = 'Your event ' + eventName.get() + ' ' + ' will start at ' + date.get() + ' you will be reminded %s day(s) before' % reminder.get()

    tkMessageBox.showinfo('Reminder', text)

def readEventFromFile(event):
    data = open("data2.txt", "r")
    text = data.read()
    text = text.split()
    datefromfile = 0
    reminder = 2
    while datefromfile < len(text):


        x = text[datefromfile]
        y = text[reminder]
        checkEvent(x, int(y))
        datefromfile = datefromfile + 3
        reminder = reminder + 3
    data.close()

    data = open("data1.txt", "r")
    text = data.read()
    if len(text) < 1:
        tkMessageBox.showinfo('Reminder', "No reminders")
    elif len(text) > 1:
        tkMessageBox.showinfo('Reminder', text)

    open('data1.txt', 'w').close()

def checkEvent(datefromfile, reminder):

    currentDate = datetime.datetime.now()
    currentDate = currentDate.replace(hour=0, minute=0, second=0, microsecond=0)
    eventDate = datetime.datetime.strptime(datefromfile, "%Y-%m-%d")
    reminderDate = eventDate - datetime.timedelta(days=reminder)

    if currentDate > eventDate:
        print 'missed'
        print currentDate
        print eventDate
        print reminderDate
        print reminder
        print 'missed'
    elif currentDate >= reminderDate:
        data = open("data1.txt", "a")
        data.write('You will have upcoming event on '+str(datefromfile)+'\n')
        data.close()
        print 'event'
        print currentDate
        print eventDate
        print reminderDate
        print reminder
        print 'event'


if __name__ == '__main__'

root = Tk()
root.geometry("250x200")

dateLabel = Label(root, text="Date YYYY-MM-DD")
dateLabel.pack(side=TOP)
date = Entry(bd=2)
date.pack()

eventNameLabel = Label(root, text="Event Name")
eventNameLabel.pack(side=TOP)
eventName = Entry(bd=2)
eventName.pack()

reminderLabel = Label(root, text="Remind days before")
reminderLabel.pack( side=TOP)
reminder = Entry(bd=2)
reminder.pack()

root.wm_title("Reminder")
Read = ttk.Button(root, text="Read", width=30)
Read.bind("<Button-1>", readEventFromFile)
Write = ttk.Button(root, text="Write", width=30)
Write.bind("<Button-1>", writeEventToFile)
Write.pack()
Read.pack()


root.mainloop()
