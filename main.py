from classes.Renderer import WinyPathRenderer
from classes.Player import Player
from classes import Engine

windPower = {-5: 0, -4: 0, -3: 0, -2: 0, -
             1: 1, 0: 1, 1: 2, 2: 1, 3: 1, 4: 1}


p = Player(x=-5, y=0)
e = Engine.WindyPathEngine(windPower, p)
e.run()

input("End")
