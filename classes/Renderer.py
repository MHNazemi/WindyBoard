
from interfaces.IRenderer import IRenderer
import uuid
import time
import turtle
import math


class WinyPathRenderer(IRenderer):
    def __init__(self, cellCounts, numbers, screenX, screenY):
        self.s_ = turtle.Screen()
        self.s_.setup(screenX, screenY)

        self.t_ = turtle.Turtle()
        # self.t_.shape("circle")
        self.t_.speed(0)

        self.cellCounts = cellCounts
        self.numbers = numbers

        self.lenght = 600
        self.objects = dict()

    def draw_board(self):

        STEP = self.lenght // self.cellCounts
        self.step = STEP
        j = 0
        for i in range(0, self.lenght+1, STEP):

            self.t_.penup()
            self.t_.setpos(-self.lenght/2, self.lenght/2 - i)
            self.t_.pendown()
            self.t_.setpos(self.lenght/2, self.lenght/2 - i)
            self.t_.penup()
            self.t_.setpos(-self.lenght/2 + i, self.lenght/2)
            self.t_.pendown()
            self.t_.setpos(-self.lenght/2 + i, -self.lenght/2)

            self.t_.penup()
            self.t_.setpos(-self.lenght/2 + STEP//2 +
                           i, -self.lenght/2 + STEP//2)
            if j < len(self.numbers):
                self.t_.write(self.numbers[j])
            j += 1

        self.t_.penup()
        self.t_.setpos(0, 0)

    def clear_screen(self):
        self.t_.clear()

    def draw_frame(self):
        for o_ in self.objects.values():
            if o_.isUpdated:
                self.t_.penup()
                self.t_.color(o_.color)
                self.t_.setpos(o_.oldX*self.step + self.step//2,
                               o_.oldY*self.step + self.step//2)
                self.t_.pendown()
                self.t_.setpos(o_.x*self.step + self.step//2,
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

                self.t_.setheading(angel)
                o_.updateOld()
                o_.clearNewStatus()

    def addObject(self, obj):
        objId = uuid.uuid4()
        self.objects[objId] = obj
        return objId.int

    def removeObject(self, objId):
        if objId in self.objects:
            del self.objects[objId]
