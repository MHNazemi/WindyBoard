from interfaces import IEngine
import time
from classes import Physics, Renderer, Controller, Player, AI


class WindyPathEngine(IEngine.IEngine):
    def __init__(self, values: dict, player: Player, initPos, goal, wait=0.016):

        self.physics = Physics.WindPhysics(values, (player,), (-5, 4), (-5, 4))

        self.renderer = Renderer.WinyPathRenderer(initPos, goal,
                                                  len(values.keys()), list(values.values()), 700, 700)
        self.renderer.addObject(player)
        self.player = player

        self.player.updatePosition(initPos[0], initPos[1])
        self.initPos = initPos
        self.AI = AI.MC(player, 100, ("w", "d", "s", "a"))

        self.controller = Controller.WinyPathController(player)

        self.wait = wait
        self.goal = goal

    def run(self):
        self.apply_init()
        finished, reward = self.apply_logic()
        reward = None
        while True:
            self.apply_renderer()
            if finished:
                input("finished!")
                self.resetGame(reward)
                finished = False
                reward = None
                self.apply_init()
                continue
            action = self.apply_AI(reward)
            self.apply_controller(action)
            self.apply_physics()
            finished, reward = self.apply_logic()

    def apply_init(self):
        self.renderer.draw_board()

    def apply_renderer(self):
        self.renderer.draw_frame()

    def apply_logic(self):
        x, y = self.player.getCurrentPos()
        if x == self.goal[0] and y == self.goal[1]:
            return True, 0
        else:
            return False, -1

    def apply_controller(self, action=None):
        if action == None:
            self.controller.getKeyboardInput()
        else:
            self.controller.getAutomatedController(action)

    def apply_physics(self):
        self.physics.apply()

    def apply_AI(self, reward):
        return self.AI.apply(reward)

    def resetGame(self, reward):
        self.player.updatePosition(self.initPos[0], self.initPos[1])
        self.renderer.clear_screen()
        self.AI.endEpisode(reward)
        self.player.updatePosition(self.initPos[0], self.initPos[1])
        self.player.clearNewStatus()
