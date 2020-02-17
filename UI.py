import tkinter
from tkinter import *
import main

MON_X_POSITION = 100
ONEDAY_PERIOD_PIXEL = 100
TIME_PIXEL_BEFORE_MON = 60

start_time = 8


HALFHOUR_PERIOD_PIXEL = 14

TERMONE_Y_POSITION = 50
TERMTWO_PIXEL_AFTER_ONE = 330
DAYS_PIXEL_BEFORE_ONE = 30


window = tkinter.Tk()

window.title("Time Table Generator")
window.geometry("900x750")


timetableCanvas = Canvas(window, width=999999, height=999999) 
timetableCanvas.pack()


#horizontal lines
timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - DAYS_PIXEL_BEFORE_ONE, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - DAYS_PIXEL_BEFORE_ONE, fill='green')

timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - 2, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - 2, fill='green')
for i in range(11):
    timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - 1 + i * 2 * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - 1 + i * 2 * HALFHOUR_PERIOD_PIXEL, fill='green')
    tkinter.Label(window, text=f"{8 + i}: 00", font=('Arial', 5)).place(x=MON_X_POSITION - TIME_PIXEL_BEFORE_MON + 1,y=TERMONE_Y_POSITION + i * 2 * HALFHOUR_PERIOD_PIXEL)

for i in range(11):
    timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - 1 + (i * 2 + 1) * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - 1 + (i * 2 + 1) * HALFHOUR_PERIOD_PIXEL, fill='light green')
timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL, fill='green')
timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL + 1, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL + 1, fill='green')


timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 2, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 2, fill='green')
for i in range(11):
    timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + i * 2 * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + i * 2 * HALFHOUR_PERIOD_PIXEL, fill='green')
    tkinter.Label(window, text=f"{8 + i}: 00", font=('Arial', 5)).place(x=MON_X_POSITION - TIME_PIXEL_BEFORE_MON + 1,y=TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE + i * 2 * HALFHOUR_PERIOD_PIXEL)

for i in range(11):
    timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + (i * 2 + 1) * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + (i * 2 + 1) * HALFHOUR_PERIOD_PIXEL, fill='light green')
timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL, MON_X_POSITION + 5 * ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE - 1 + 11 * 2 * HALFHOUR_PERIOD_PIXEL, fill='green')




#vertical lines
timetableCanvas.create_line(MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION - DAYS_PIXEL_BEFORE_ONE, MON_X_POSITION - TIME_PIXEL_BEFORE_MON, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE + 22*HALFHOUR_PERIOD_PIXEL, fill='green')
timetableCanvas.create_line(MON_X_POSITION - 2, TERMONE_Y_POSITION - DAYS_PIXEL_BEFORE_ONE, MON_X_POSITION - 2, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE + 22*HALFHOUR_PERIOD_PIXEL, fill='green')
for i in range(6):
    timetableCanvas.create_line(MON_X_POSITION - 1 + i*ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION - DAYS_PIXEL_BEFORE_ONE, MON_X_POSITION - 1 + i*ONEDAY_PERIOD_PIXEL, TERMONE_Y_POSITION + TERMTWO_PIXEL_AFTER_ONE + 22*HALFHOUR_PERIOD_PIXEL, fill='green')



sectionNameList = []
sectionBoxList = []

timetableNum = 0


def generate(timetableNum):
    if(timetableNum < len(main.timetable) and timetableNum >= 0):
        tkinter.Label(window, text=f"({timetableNum+1}/{len(main.timetable)})", font=('Arial', 10)).place(x=600,y=100)

        for sn in sectionNameList:
            sn.place_forget()
        for sb in sectionBoxList:
            timetableCanvas.delete(sb)
            
        for t in main.timetable[timetableNum]:
            for p in t[1]["Reformate"]:
                sectionBox = timetableCanvas.create_rectangle(MON_X_POSITION + (p[1]-1)*ONEDAY_PERIOD_PIXEL - 1, 
                ((p[2]-start_time)*2*HALFHOUR_PERIOD_PIXEL+TERMONE_Y_POSITION)+(p[0]-1)*TERMTWO_PIXEL_AFTER_ONE - 1, 
                MON_X_POSITION + p[1]*ONEDAY_PERIOD_PIXEL - 1 , 
                ((p[3]-start_time)*2*HALFHOUR_PERIOD_PIXEL+TERMONE_Y_POSITION)+(p[0]-1)*TERMTWO_PIXEL_AFTER_ONE - 1, 
                fill='light green')
                sectionBoxList.append(sectionBox)
                sectionName = tkinter.Label(window, text=t[1]["Section"], font=('Arial', 10), bg = 'light green')
                sectionName.place(x=MON_X_POSITION + (p[1]-1)*ONEDAY_PERIOD_PIXEL,y=((p[2]-start_time)*2*HALFHOUR_PERIOD_PIXEL+TERMONE_Y_POSITION)+(p[0]-1)*TERMTWO_PIXEL_AFTER_ONE)
                sectionNameList.append(sectionName)

def next():
    global timetableNum
    if timetableNum < len(main.timetable) - 1:
       timetableNum = timetableNum + 1
    print(timetableNum)
    generate(timetableNum)

def before():
    global timetableNum
    if timetableNum > 0:
        timetableNum = timetableNum - 1
    print(timetableNum)
    generate(timetableNum)


generate(0)

b = tkinter.Button(window, text='next', font=('Arial', 12), width=10, height=1, command=next).place(x=600, y=200)
b = tkinter.Button(window, text='before', font=('Arial', 12), width=10, height=1, command=before).place(x=600, y=400)



window.mainloop()