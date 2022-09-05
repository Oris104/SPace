# This is a sample Python script.
import os
import shutil
import numpy as np
import array
import sys
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.







command = "mode 75,150"
os.system(command)
numLines =shutil.get_terminal_size().lines
numCols =shutil.get_terminal_size().columns

Field =  np.arange(numCols*numLines).reshape(numLines,numCols)



def Printer():
    print(str(Field).replace(", ", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").replace("0",
    " ").replace("2", "A"))



np.set_printoptions(threshold=sys.maxsize)



np.place(Field,Field>=0,0)
print(str(Field).replace(", ","").replace("[","").replace("]","").replace("\n","").replace(" ","").replace("0", " "))
X=0
y=0

class Chara():
    def __init__(self,x,y,val):
        self.x=x
        self.y=y
        self.val=val
        self.createAt()


    def createAt(self):
        Field[self.x][self.y]=self.val
    def moveDown(self):
        Field[self.x+1][self.y]= Field[self.x][self.y]
        Field[self.x][self.y]=0
        self.x+=1
    def moveUp(self):
        Field[self.x - 1][self.y] = Field[self.x][self.y]
        Field[self.x][self.y] = 0
        self.x -= 1
    def moveRight(self):
        Field[self.x][self.y+1] = Field[self.x][self.y]
        Field[self.x][self.y] = 0
        self.y += 1
    def moveLeft(self):
        Field[self.x][self.y-1] = Field[self.x][self.y]
        Field[self.x][self.y] = 0
        self.y -= 1
i=0
obj = Chara(20,20,2)
while 1:

    if i < 10:
        obj.moveDown()
    elif i< 20:
        obj.moveRight()
    elif i< 30:
        obj.moveUp()
    elif i< 40:
        obj.moveLeft()
    else:
        i=0
    i+=1
    Printer()
    time.sleep(0.5)






