import get_data
import check_local
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from datetime import datetime
dailyData=get_data.main(5)
def main():
    #get_data.main(5)
    #creates window
    window = tk.Tk()
    window.title("where to eat @ RIT")
    window.geometry('800x800')
    window.grid_columnconfigure((0, 1, 2), weight=1)
    #creates title text
    a = Label(window, text ='where to eat @ RIT', font = "50") 
    #handel grid lay out of dinning locations 
    a.config(font = ("Courier",18))
    a.grid(row = 0, column = 1, pady = 5)
    y = 0
    k = 0
    for i in range(len(dailyData)):

        if check_local.check_status(dailyData[i]):
            k+=1
            output = Label(window, text = dailyData[i][0], borderwidth=3, relief="groove", font="Ariel") 
            output.grid(row = k  + 4 - y%3, column = y % 3, pady = 3)
            y+=1
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    output = Label(window, text = current_time, borderwidth=2, relief="groove") 
    print(current_time)
    output.grid(row = 1 , column = 1 , pady = 5)
    window.mainloop()
if __name__ == '__main__':
    main()