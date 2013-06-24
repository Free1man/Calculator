import datetime

def writeEventToFile():

    date = raw_input("Input date of Event:")
    eventName = raw_input("input name of event:")
    reminder = raw_input("Remind X days before:")

    print 'Your event ' + eventName + ' '+' will start at ' + date + ' you will be reminded %s day(s) before' % reminder

    data = open("data2.txt", "a")
    data.write(str(date+' '+eventName+' '+reminder+'\n'))
    data.close()


def readEventFromFile():
    data = open("data2.txt", "r")
    text = data.read()
    text = text.split()
    datefromfile = 0
    reminder = 2
    while datefromfile < len(text):


        x = text[datefromfile]
        y = text[reminder]
        checkEvent (x,int(y))
        datefromfile = datefromfile + 3
        reminder = reminder + 3
    data.close()


def checkEvent(datefromfile,reminder):


    currentDate = datetime.datetime.now()
    eventDate = datetime.datetime.strptime(datefromfile,"%Y-%m-%d")
    reminderDate = eventDate + datetime.timedelta(days=-reminder)

    if currentDate < reminderDate:
        print 'no events'
    elif currentDate >= reminderDate:
        print 'you have upcoming event'
        print currentDate
        print eventDate
        print datefromfile
        print reminderDate
        print reminder

now =  datetime.datetime.now()

print "Current time "+ now.strftime("%Y-%m-%d")
x = raw_input()

if x == '1':
    writeEventToFile()
elif x == '2':
    readEventFromFile()
