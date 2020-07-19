class Player:
    def __init__(self, x=0, y=0, color="black"):
        self.x = x
        self.y = y
        self.oldX = x
        self.oldY = y
        self.color = color
        self.updated = False

    def updatePostion(self, x, y):
        self.oldX = self.x
        self.oldY = self.y
        self.x = x
        self.y = y
        self.updated = True

    def moveX(self, x):
        self.oldX = self.x
        self.x += x
        self.updated = True

    def moveY(self, y):
        self.oldY = self.y
        self.y += y
        self.updated = True

    def isUpdated(self):
        self.updated = False

    def getOldPos(self):
        return self.oldX, self.oldY

    def getCurrentPos(self):
        return self.x, self.y

    def clearNewStatus(self):
        self.updated = False
