from interfaces import IController


class WinyPathController(IController.I2DController):
    def __init__(self, obj):
        self.obj = obj

    def getKeyboardInput(self):
        i = input()
        while True:
            if i.lower() == "w":
                self.obj.moveY(1)
                break
            elif i.lower() == "d":
                self.obj.moveX(1)
                break
            elif i.lower() == "s":
                self.obj.moveY(-1)
                break
            elif i.lower() == "a":
                self.obj.moveX(-1)
                break
            print("Invalid Input! Try again")
            i = input()
