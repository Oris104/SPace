import keyboard


class Chara():  # Grundklasse Charakter
    def __init__(self, x, y, val, Field):  # Basis initialisierung
        self.x = x
        self.y = y
        self.val = val
        self.Field = Field
        self.createAt()  # Schreibt eigenen wer an Position in Array

    def createAt(self):
        self.Field[self.x][self.y] = self.val

    def moveDown(self):  # Schreibt Wert ein Feld nach unten

        self.Field[self.x + 1][self.y] = self.Field[self.x][self.y]
        self.Field[self.x][self.y] = 0
        self.x += 1

    def moveUp(self):  # Schreibt Wert ein Feld nach oben
        self.Field[self.x - 1][self.y] = self.Field[self.x][self.y]
        self.Field[self.x][self.y] = 0
        self.x -= 1

    def moveRight(self):  # Schreibt Wert ein Feld nach rechts
        if self.y + 1 <= 73:
            self.Field[self.x][self.y + 1] = self.Field[self.x][self.y]
            self.Field[self.x][self.y] = 0
            self.y += 1

    def moveLeft(self):  # Schreibt Wert ein Feld nach links
        if self.y > 1:
            self.Field[self.x][self.y - 1] = self.Field[self.x][self.y]
            self.Field[self.x][self.y] = 0
            self.y -= 1


class Player(Chara):  # Spielercharakter
    def __init__(self, x, y, Field):  # Schreibt sich selbst in festes Felf
        super().__init__(x, y, 2, Field)
        self.val = 2

    def tick(self):
        self.createAt()
        if keyboard.is_pressed("left"):
            self.moveLeft()
        if keyboard.is_pressed("right"):
            self.moveRight()


class Projectile(Chara):
    def suicide(self):
        self.Field[self.x][self.y] = 0
        del (self)

    def tick(self):
        if not self.x > 0:
            self.suicide()
        else:
            self.moveUp()


class Enemy(Chara):
    def suicide(self):
        self.Field[self.x][self.y] = 0

    def tick(self):
        if self.x >= 49:
            self.suicide()
            return 2
        elif not self.Field[self.x][self.y] == self.val:
            self.suicide()
            return 1
        else:
            self.moveDown()
            return 0
