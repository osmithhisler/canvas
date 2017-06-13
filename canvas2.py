#draw four squares, randomly color each square, produce sound when red is generated, use keyboard to change color of random squares, write last color and datetime to .db file 
import os, sys
import random
import time
import winsound
from Tkinter import *
master = Tk()

def fgreen(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "green")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("green " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()

def fred(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "red")
    #play tone if keyboard is used to create a red square
    winsound.Beep(275, 1000)
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("red " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()
    
def forange(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "orange")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("orange " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()

def fyellow(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "yellow")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("yellow " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()

def fblue(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "blue")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("blue " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()

def fviolet(event):
    s1 = [0,0,100,100]
    s2 = [100,0,200,100]
    s3 = [0,100,100,200]
    s4 = [100,100,200,200]
    s = [s1, s2, s3, s4]
    w.create_rectangle(random.choice(s), fill = "violet")
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas2.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    file = open(filename, 'w')
    file.write("violet " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    file.close()

def mouseclick(event):
    w.focus_set()

w = Canvas(master, width = 200, height = 200)

#click in canvas and then use keyboard to color the fourth square
w.bind("<Button-1>", mouseclick)
w.bind("<g>", fgreen)
w.bind("<r>", fred)
w.bind("<o>", forange)
w.bind("<y>", fyellow)
w.bind("<b>", fblue)
w.bind("<v>", fviolet)
w.pack()

#choose random colors from color list 
color = ["red", "orange", "yellow", "green", "blue", "violet"]
c1 = random.choice(color)
c2 = random.choice(color)
c3 = random.choice(color)
c4 = random.choice(color)

#draw three more squares
w.create_rectangle(0,0,100,100, fill = c1)
w.create_rectangle(100,0,200,100, fill = c2)
w.create_rectangle(0,100,100,200, fill = c3)
w.create_rectangle(100,100,200,200, fill = c4)

#add text
w.create_text(150,125,text = "Click on canvas.")
w.create_text(150,150,text = "and use keyboard")
w.create_text(150,175,text = "to choose color.")

#play tone when a red square is generated
if c1 == "red" or c2 == "red" or c3 == "red" or c4 == "red":
    winsound.Beep(275, 1000)
    
master.mainloop()
