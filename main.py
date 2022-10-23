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


command = "mode 75,50" # Fenstergrösse einstellen

os.system(command) # Fenstergrösse ausführen
os.system('color 02') # Farbe konfigurieren
numLines = shutil.get_terminal_size().lines # anzahl Zeilen auslesen
numCols = shutil.get_terminal_size().columns # anzahl Kollonen auslesen

Field = np.arange(numCols*numLines).reshape(numLines,numCols) #2D Array mit Zeilen und Kollonen erstellen


def Printer(): # Gibt Spielfeld aus nachdem Array Werte mit zugehörigem Zeichen ersetzt wurden
    print(str(Field).replace(", ", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").replace("0",
    " ").replace("2", "A").replace("4","V").replace("6","I")+"Score: "+str(score)+"  Lives: "+str(lives))


np.set_printoptions(threshold=sys.maxsize) # Array Ausgabe einrichten


np.place(Field,Field>=0,0) # Füllt Array mit 0
# Gibt Leeres Feld zum Start aus
print(str(Field).replace(", ","").replace("[","").replace("]","").replace("\n","").replace(" ","").replace("0", " "))
X = 0 # Koordinaten Variablen setzen
y = 0 #
i = 0 # Zähl variable setzen
enemies = [] # Liste für gegner objekte erstellen
projectiles = [] # Liste für Projektile erstellen
player = GameEntities.Player(49,30,Field) # Spieler erstellen
enemyMov = 0 # Zählvariable gegner erstellen
score = 0 # score Variable erstellen
lives = 5 # Variable für Leben erstellen
cd = 0 # Schuss Cooldown Variable erstellen
spwn = 10 # Gegner Spawn Cooldown Variable einstellen
while lives > 0: # Loop solange man noch Leben hat
    if spwn >= 20: # Alle 20 Ticks
        spwn = 0
        u = random.randint(0, numCols - 1)
        enemies.append(GameEntities.Enemy(0, u, 4, Field)) # Gegner an Zufälliger Position erstellen
    else:
        spwn +=1
    if enemyMov == 5:
        enemyMov=0
        for it in enemies:
            rück = it.tick()
            if rück ==1:
                score +=1
                enemies.remove(it)
            elif rück ==2:
                enemies.remove(it)
                lives +=-1
    else:
        enemyMov += 1




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





