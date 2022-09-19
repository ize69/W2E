from ast import Tuple
from multiprocessing.dummy import Array
from tkinter import tix
from tkinter.tix import *
from typing_extensions import final
import get_data
import check_local
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
dailyData=get_data.main()
print(dailyData[0])
setRaw = True
if setRaw:
    raw_data = tuple(dailyData)
    setRaw=False
window = tix.Tk()
window.title("where to eat @ RIT")
window.geometry('800x800')
window.grid_columnconfigure((0, 1, 2), weight=1)
def update_hours():
    print(raw_data[0])
    y = 0
    k = 0
    #draws the lables with the open locations 
    for i in range(len(dailyData)):
        if check_local.check_status(dailyData[i]):
            k+=1
            output = Button(window, text = dailyData[i][0], borderwidth=3,relief="groove", font="Ariel") 
            #creates the balloon for when hovering over the location to display the hours
            hours_of_oporation = Balloon(window)
            output.grid(row = k  + 4 - y%3, column = y % 3, pady = 3)
            temp = str(raw_data[i][check_local.check_meal((dailyData[i]))]) 
            temp += " to " 
            temp += str(raw_data[i][check_local.check_meal((dailyData[i]))+1])
            hours_of_oporation.bind_widget(output, balloonmsg = temp)
            y+=1       
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    output = Label(window, text = current_time, borderwidth=2, relief="groove") 
    #print(current_time)
    output.grid(row = 1 , column = 1 , pady = 5)

#creates title text
a = Label(window, text ='where to eat @ RIT', relief="groove",font = "50") 
#handel grid lay out of dinning locations 
a.config(font = ("Courier",18))
a.config(bg='#F76902')
a.config(fg='#FFFFFF')
a.config()
a.grid(row = 0, column = 1, pady = 5)
is_running = True
y = 0
k = 0

#draws the lables with the open locations 
for i in range(len(dailyData)):
    
    if check_local.check_status(dailyData[i]):
        k+=1
        output = Label(window, text = dailyData[i][0], borderwidth=3, relief="groove", font="Ariel") 
        output.grid(row = k  + 4 - y%3, column = y % 3, pady = 3)
        y+=1
now = datetime.now()
current_time = now.strftime("%I:%M %p")
output = Button(window, text = current_time, borderwidth=2, relief="groove") 
#print(current_time)
output.grid(row = 1 , column = 1 , pady = 5)
btn_R =Button(window,text = "refresh",borderwidth=2, relief="groove", command = update_hours)
btn_R.grid(row = 2 , column = 1 , pady = 5)
window.mainloop()


