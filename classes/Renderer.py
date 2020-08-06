
from interfaces.IRenderer import IRenderer
import uuid
import time
import turtle
import math


class WinyPathRenderer(IRenderer):
    def __init__(self, initPos, goalPos, cellCounts, numbers, screenX, screenY):
        self.s_ = turtle.Screen()
        self.s_.setup(screenX, screenY)

        self.boardPen = turtle.Turtle()
        self.playerPen = turtle.Turtle()
        # self.boardPen.shape("circle")
        self.boardPen.speed(0)
        self.boardPen.hideturtle()
        self.playerPen.speed(0)

        self.initPos = initPos
        self.goalPos = goalPos

        self.cellCounts = cellCounts
        self.numbers = numbers

        self.lenght = 600
        self.objects = dict()

    def draw_board(self, color="black"):
        self.boardPen.color(color)
        STEP = self.lenght // self.cellCounts
        self.step = STEP
        j = 0
        for i in range(0, self.lenght+1, STEP):

            self.boardPen.penup()
            self.boardPen.setpos(-self.lenght/2, self.lenght/2 - i)
            self.boardPen.pendown()
            self.boardPen.setpos(self.lenght/2, self.lenght/2 - i)
            self.boardPen.penup()
            self.boardPen.setpos(-self.lenght/2 + i, self.lenght/2)
            self.boardPen.pendown()
            self.boardPen.setpos(-self.lenght/2 + i, -self.lenght/2)

            self.boardPen.penup()
            self.boardPen.setpos(-self.lenght/2 + STEP//2 +
                                 i, -self.lenght/2 + STEP//2)
            if j < len(self.numbers):
                self.boardPen.write(self.numbers[j])
            j += 1

        self.boardPen.penup()
        self.boardPen.setpos(self.goalPos[0]*STEP + STEP //
                             2, self.goalPos[1]*STEP + STEP//2)
        self.boardPen.pendown()
        self.boardPen.write("X")

        self.boardPen.penup()
        self.boardPen.setpos(self.initPos[0], self.initPos[1])

    def clear_screen(self):
        self.boardPen.clear()

    def clear_player(self):
        self.playerPen.clear()

    def draw_frame(self):
        for o_ in self.objects.values():
            if o_.isUpdated():
                self.playerPen.penup()
                self.playerPen.setpos(o_.oldX*self.step + self.step//2,
                                      o_.oldY*self.step + self.step//2)
                self.playerPen.color(o_.color)
                self.playerPen.pendown()
                self.playerPen.setpos(o_.x*self.step + self.step//2,
                                      o_.y*self.step + self.step//2)

                difX = o_.x - o_.oldX
                difY = o_.y - o_.oldY

                if difX != 0:
                    if difY != 0:
                        angel = math.degrees(math.tanh(abs(difY) / abs(difX)))
                        if difX > 0 and difY < 0:
                            angel = 360-angel
                        elif difX < 0 and difY > 0:
                            angel = 90+angel
                        elif difX < 0 and difY < 0:
                            angel = 180+angel
                    else:
                        if difX > 0:
                            angel = 0
                        else:
                            angel = 180
                else:
                    if difY > 0:
                        angel = 90
                    else:
                        angel = 270

                self.playerPen.setheading(angel)
                o_.updateOld()
                o_.clearNewStatus()

    def draw_result(self, result):

        self.playerPen.hideturtle()
        self.playerPen.color("green")
        for x in range(len(result)):
            for y in range(len(result[0])):
                self.playerPen.penup()
                self.playerPen.setpos((x-self.cellCounts//2)*self.step + self.step//2,
                                      (y-self.cellCounts//2)*self.step + self.step//2)
                self.playerPen.pendown()
                self.playerPen.write(result[x][y])
        self.playerPen.showturtle()

    def addObject(self, obj):
        objId = uuid.uuid4()
        self.objects[objId] = obj
        return objId.int

    def removeObject(self, objId):
        if objId in self.objects:
            del self.objects[objId]
