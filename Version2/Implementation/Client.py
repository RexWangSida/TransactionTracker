#!/usr/bin/python
from tkinter import *
from tkinter import messagebox
from product import *
from inventory import inventory
import datetime


def start():
    window = Tk()
    window.title("Sneakers Tradings Tracker")
    window.geometry("1000x1000")
    #above is structure, code starts here
    background_image = PhotoImage(file="image.png")
    background_label = Label(window,image=background_image)
    background_label.place(relwidth=1,relheight=1)
    #------------file read
    def READ():
        f = open("inventory.txt","r")
        lines = f.readlines()
        if lines == None:
            data = inventory([])  

        else:
            l = []
            for i in range(len(lines)//5):
                name = str(lines[i*5].strip())
                sell = float(lines[i*5+1].strip())
                buy = float(lines[i*5+2].strip())
                date = str(lines[i*5+3].strip())
                number = int(lines[i*5+4].strip())
                new_product= product(sell,buy,name,number,date)
                l.append(new_product)

            data = inventory(l)
        f.close()
        return data

    #------------file read ends

    #------------file write

    def WRITE(data):
        f = open("inventory.txt","w")
        seq = data.toSeq()
        for i in seq:
            f.write(str(i.get_name())+"\n")
            f.write(str(i.get_sell_price())+"\n")
            f.write(str(i.get_buy_price())+"\n")
            f.write(str(i.get_date())+"\n")
            f.write(str(i.get_number())+"\n")
        f.close()

    #------------file write ends


    def warning():
        msg = messagebox.showinfo("Warning", "This right of this program belongs to Sida Wang for personal use only!")

    def CLOSE():
        window.destroy()
        start()

    def ADD():
        data = READ()
        name = str(entry1.get())
        sell = float(entry2.get())
        buy = float(entry3.get())
        number = int(entry4.get())
        date = datetime.datetime.now()
        data.add_trade(sell,buy,name,number,date)
        WRITE(data)
        DISPLAY()
        
    def DELETE():
        data = READ()
        name = str(entry5.get())
        data.delete_trade(name)
        WRITE(data)
        DISPLAY()

    def DISPLAY():
        data = READ()
        seq = data.toSeq()
        display = Text(frame)
        display.grid(column = 0, row = 15)

        for i in seq :
            display.insert(INSERT,"Name:" + i.get_name()+"\n")
            display.insert(INSERT,"Sell-out price:" + str(i.get_sell_price())+"\n")
            display.insert(INSERT,"Buy-in price:" + str(i.get_buy_price()) +"\n")
            display.insert(INSERT,"Date of trade:" + str(i.get_date()) +"\n")
            display.insert(INSERT,"Number of pairs:" + str(i.get_number()) +"\n")
            display.insert(INSERT,"Profit:" + str(i.profit()) +"\n\n\n")

    def PROFIT():
        data = READ()
        display = Text(frame)
        display.grid(column = 0, row = 15)
        display.insert(INSERT,"Net-Profit is  " + str(data.net_profit())) 




    B1 = Button(window, text = "Click me before you start", command = warning)
    B1.grid(column = 0 , row = 0)

    label0 = Label(text="Please add trade here:")
    label0.grid(column = 0 , row = 1)
    label1 = Label(text="Name:")
    label1.grid(column = 0 , row = 2)
    label2 = Label(text="Sell-out price:")
    label2.grid(column = 0 , row = 3)
    label3 = Label(text="Buy-in price:")
    label3.grid(column = 0 , row = 4)
    label4 = Label(text="Number of pairs:")
    label4.grid(column = 0 , row = 5)
    label4 = Label(text="Please delete trade here:")
    label4.grid(column = 0 , row = 10)
    label5 = Label(text="Name:")
    label5.grid(column = 0 , row = 11)

    entry1 = Entry()
    entry1.grid(column =1, row = 2)
    entry2 = Entry()
    entry2.grid(column =1, row = 3)
    entry3 = Entry()
    entry3.grid(column =1, row = 4)
    entry4 = Entry()
    entry4.grid(column =1, row = 5)
    entry5 = Entry()
    entry5.grid(column =1, row = 11)

    B2 = Button(window, text = "ADD", command = ADD)
    B2.grid(column = 1 , row = 6)
    B3 = Button(window, text = "DELETE", command = DELETE)
    B3.grid(column = 1 , row = 12)
    B3 = Button(window, text = "VIEW ALL", command = DISPLAY)
    B3.grid(column = 0 , row = 13)
    B4 = Button(window, text = "CLOSE", command = CLOSE)
    B4.grid(column = 1 , row = 13)
    B5 = Button(window, text = "NET PROFIT", command = PROFIT)
    B5.grid(column = 0 , row = 14)
    frame = Frame(window)
    frame.grid(column = 0, row = 15)

    #below is structure, code ends here
    window.mainloop()

start()

