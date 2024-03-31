class Character:
    def __init__(self, N, X, Y):
        self.Name = N # String
        self.XPosition = X # Int
        self.YPosition = Y # Int

    def GetXPosition(self):
        return self.XPosition
    
    def GetYPosition(self):
        return self.YPosition
    
    def SetXPosition(self, X):
        if X >= 0 and X <= 10000:
            self.XPosition = X
        elif X < 0:
            self.XPosition = 0

    def SetYPosition(self, Y):
        if Y >= 0 and Y <= 10000:
            self.YPosition = Y
        elif Y < 0:
            self.YPosition = 0

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(self.GetYPosition() + 10)
        if Direction == "down":
            self.SetYPosition(self.GetYPosition() - 10)
        if Direction == "left":
            self.SetXPosition(self.GetXPosition() - 10)
        if Direction == "right":
            self.SetXPosition(self.GetXPosition() + 10)

class BikeCharacter(Character):
    def __init__(self, N, X, Y):
        Character.__init__(self, N, X, Y)

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(self.GetYPosition() + 20)
        if Direction == "down":
            self.SetYPosition(self.GetYPosition() - 20)
        if Direction == "left":
            self.SetXPosition(self.GetXPosition() - 20)
        if Direction == "right":
            self.SetXPosition(self.GetXPosition() + 20)

Jack = Character("Jack", 50, 50)

Karla = BikeCharacter("Karla", 100, 50)

Movement = input("Choose which player to move: ")
if Movement == "Jack":
    Direction = input("Which Direction? ")
    if Direction == "up" or Direction == "down" or Direction == "left" or Direction == "right":
        Jack.Move(Direction)
        print("Jack's new position is X = "+str(Jack.GetXPosition())+" Y = "+str(Jack.GetYPosition()))
    else:
        pass
elif Movement == "Karla":
    Direction = input("Which Direction? ")
    if Direction == "up" or Direction == "down" or Direction == "left" or Direction == "right":
        Karla.Move(Direction)
        print("Jack's new position is X = "+str(Karla.GetXPosition())+" Y = "+str(Karla.GetYPosition()))
    else:
        pass
