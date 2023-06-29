from tkinter import *
import tkinter as ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time, os, sys

root = Tk()
frm = ttk.Frame(root)
frm.grid()
ttk.Label(frm, text="Flowers for Friends").grid(column=0, row=0)

def myUI():
    myStatus = True

    while myStatus:
        makeRun = open("prng-service.txt", "w")
        makeRun.write("run")
        makeRun.close()
        time.sleep(10)

        readVal = open("prng-service.txt", "r")
        myNum = readVal.read()
        readVal.close()
        putNum = open("image-service.txt", "w")
        strNum = str(myNum)
        putNum.write(strNum)
        putNum.close()
        time.sleep(5)

        myFile = open("image-service.txt", "r")
        pathURL = myFile.read()
        myFile.close()
        print("Your image path URL from the current folder is:", pathURL)
        myImg = Image.open(pathURL)
        myImg.show()
        myStatus = False

ttk.Button(frm, text="Pick a new flower", command=myUI).grid(column=0, row=2)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=2)

root.mainloop()

