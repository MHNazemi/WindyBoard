from interfaces import IEngine
import time
from classes import Physics, Renderer, Controller, Player


class WindyPathEngine(IEngine.IEngine):
    def __init__(self, values: dict, player: Player, goal, wait=0.016):

        self.physic = Physics.Wind(values, (player,), (-5, 4), (-5, 4))

        self.renderer = Renderer.WinyPathRenderer(
            len(values.keys()), list(values.values()), 700, 700)
        self.renderer.addObject(player)
        # if AI == None:
        #     self.AI = AI.WinyPathRenderer()
        # else:
        #     self.AI = AI

        self.controller = Controller.WinyPathController(player)

        self.wait = wait

    def run(self):
        self.renderer.draw_board()
        while True:
            self.renderer.draw_frame()
            self.controller.getKeyboardInput()
            self.physic.apply()
            # self.AI.apply()
            # time.sleep(self.wait)

    def resetGame(self):
        pass
