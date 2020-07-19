from interfaces import IEngine
import time
from classes import Physics, Renderer, Controller, Player


class WindyPathEngine(IEngine.IEngine):
    def __init__(self, values: dict, player: Player, goal, wait=0.016):

        self.physics = Physics.WindPhysics(values, (player,), (-5, 4), (-5, 4))

        self.renderer = Renderer.WinyPathRenderer(
            len(values.keys()), list(values.values()), 700, 700)
        self.renderer.addObject(player)
        # if AI == None:
        #     self.AI = AI.WinyPathRenderer()
        # else:
        #     self.AI = AI

        self.controller = Controller.WinyPathController(player)

        self.wait = wait
        self.goal = goal

    def run(self):
        self.apply_init()
        while True:
            self.apply_renderer()
            self.apply_logic()
            self.apply_controller()
            self.apply_physics()

    def apply_init(self):
        self.renderer.draw_board()

    def apply_renderer(self):
        self.renderer.draw_frame()

    def apply_logic(self):
        pass

    def apply_controller(self):
        self.controller.getKeyboardInput()

    def apply_physics(self):
        self.physics.apply()

    def apply_AI(self):
        pass

    def resetGame(self):
        pass
