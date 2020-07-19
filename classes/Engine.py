from interfaces import IEngine
import time
from classes import Physics, Renderer, Controller


class WindyPathEngine(IEngine):
    def __init__(self, physic=None, renderer=None, AI=None, controller=None, wait=0.016):

        if physic == None:
            self.physic = Physics.Wind()
        else:
            self.physic = physic

        if renderer == None:
            self.renderer = Renderer.WinyPathRenderer()
        else:
            self.renderer = renderer

        # if AI == None:
        #     self.AI = AI.WinyPathRenderer()
        # else:
        #     self.AI = AI

        if controller == None:
            self.controller = Controller.WinyPathController()
        else:
            self.controller = controller

        self.wait = wait

    def run(self):
        self.renderer.draw_board()
        while True:
            self.physic.apply()
            self.renderer.draw_frame()
            # self.AI.apply()
            time.sleep(self.wait)

    def addPhysics(self, physic: IPhysic):
        self.physic = physic

    def addRenderer(self, renderer: IRenderer):
        self.renderer = renderer

    def addAI(self, AI):
        self.AI = AI

    def resetGame(self):
        pass
