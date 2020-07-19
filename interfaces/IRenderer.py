import multiprocessing
import time


class IRenderer():

    def draw_frame(self):
        raise NotImplementedError()

    def addObject(self, obj):
        raise NotImplementedError()

    def removeObject(self, objId):
        raise NotImplementedError()
