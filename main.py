import os
import random
import shutil
import numpy as np
import sys
import time
import GameEntities
import keyboard

command = "mode 75,50"  # Fenstergrösse einstellen

os.system(command)  # Fenstergröße ausführen
os.system('color 02')  # Farbe konfigurieren
numLines = shutil.get_terminal_size().lines  # anzahl Zeilen auslesen
numCols = shutil.get_terminal_size().columns  # anzahl Kolonen auslesen

Field = np.arange(numCols * numLines).reshape(numLines, numCols)  # 2D Array mit Zeilen und Kolonen erstellen


def Printer():  # Gibt Spielfeld aus, nachdem Array Werte mit zugehörigem Zeichen ersetzt wurden
    print(str(Field).replace(", ", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").replace("0",
                                                                                                                    " ")
          .replace("2", "A").replace("4", "V").replace("6", "I") + "Score: " + str(score) + "  Lives: " + str(lives))


np.set_printoptions(threshold=sys.maxsize)  # Array Ausgabe einrichten

np.place(Field, Field >= 0, 0)  # Füllt Array mit 0
# Gibt leeres Feld zum Start aus
print(
    str(Field).replace(", ", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").replace("0", " "))
X = 0  # Koordinaten Variablen setzen
y = 0  #
i = 0  # Zähl variable setzen
enemies = []  # Liste für gegner objekte erstellen
projectiles = []  # Liste für Projektile erstellen
player = GameEntities.Player(49, 30, Field)  # Spieler erstellen
enemyMov = 0  # Zählvariable gegner erstellen
score = 0  # score Variable erstellen
lives = 5  # Variable für Leben erstellen
cd = 0  # Schuss Cooldown Variable erstellen
spwn = 10  # Gegner Spawn Cooldown Variable einstellen
while lives > 0:  # Loop solange man noch Leben hat
    if spwn >= 20:  # Alle 20 Ticks
        spwn = 0
        u = random.randint(0, numCols - 1)
        enemies.append(GameEntities.Enemy(0, u, 4, Field))  # Gegner an Zufälliger Position erstellen
    else:
        spwn += 1
    if enemyMov == 5:  # Alle 5 Ticks
        enemyMov = 0
        for it in enemies:  # Bei allen Gengner Objekten tick() aufrufen
            rueck = it.tick()  # Tick Rückgabe abfangen
            if rueck == 1:  # bei 1 gegner durch Projektil tod
                score += 1  # Score erhöhen
                enemies.remove(it)  # gegner entfernen
            elif rueck == 2:  # bei 2 gegner unten angekommen
                enemies.remove(it)  # gegner entfernen
                lives += - 1  # Leben abziehen
    else:
        enemyMov += 1

    if keyboard.is_pressed("space"):  # wenn lehrtaste gedrückt
        if cd == 0:  # wenn Cooldown 0 ist
            projectiles.append(GameEntities.Projectile(48, player.y, 6, Field))  #
            projectiles.append(GameEntities.Projectile(48, player.y + 1, 6, Field))  # Projektile vor spieler erstellen
            projectiles.append(GameEntities.Projectile(48, player.y - 1, 6, Field))  #
            cd = 5  # 5 Ticks cooldown
    if cd > 0:  # wenn CD grösser als 0 um 1 verkleinern
        cd += -1

    player.tick()  # Spieler Tick aufrufen

    Printer()  # Spielfeld Ausgeben
    for it in projectiles:  # bei allen Projektilen
        if it.x <= 1:  # wenn auserhalb spielfeld
            projectiles.remove(it)  # Projektil entfernen
        else:
            it.tick()  # sonst Projektil Tick aufrufen

    time.sleep(0.05)  # alle 50mS ein Tick
print("game over")  # bei Tod Gamer Over ausgeben
input()  # auf Input warten
