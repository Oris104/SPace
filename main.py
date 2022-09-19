# This is a sample Python script.
import os
import random
import shutil
import numpy as np
import array
import sys
import time
import GameEntities
import math
import keyboard
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.







command = "mode 75,50"

os.system(command)
os.system('color 02')
numLines =shutil.get_terminal_size().lines
numCols =shutil.get_terminal_size().columns

Field =  np.arange(numCols*numLines).reshape(numLines,numCols)



def Printer():
    print(str(Field).replace(", ", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").replace("0",
    " ").replace("2", "A").replace("4","V").replace("6","I")+"Score: "+str(score)+"  Lives: "+str(lives))



np.set_printoptions(threshold=sys.maxsize)



np.place(Field,Field>=0,0)
print(str(Field).replace(", ","").replace("[","").replace("]","").replace("\n","").replace(" ","").replace("0", " "))
X=0
y=0


i=0
enemies=[]
projectiles=[]
player=GameEntities.Player(49,30,Field)
zc=0
score =0
lives = 5
cd=0
spwn =10
while lives > 0:
    if spwn >=20:
        spwn =0
        u = random.randint(0, numCols - 1)
        enemies.append(GameEntities.Enemy(0, u, 4, Field))
    else:
        spwn +=1
    if zc == 5:
        zc=0
        for it in enemies:
            neo = it.tick()
            if neo ==1:
                score +=1
                enemies.remove(it)
            elif neo ==2:
                enemies.remove(it)
                lives +=-1
    else:
        zc += 1




    if keyboard.is_pressed("space"):
        if cd ==0:
            projectiles.append(GameEntities.Projectile(48,player.y,6,Field))
            projectiles.append(GameEntities.Projectile(48, player.y+1, 6, Field))
            projectiles.append(GameEntities.Projectile(48, player.y-1, 6, Field))
            cd =5
    if cd>0:
        cd+=-1



    player.tick()

    Printer()
    for it in projectiles:
        if it.x <=1:
            projectiles.remove(it)
        else:
            it.tick()

    time.sleep(0.05)
print("game over")
input()





