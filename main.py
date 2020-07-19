from classes.Renderer import WinyPathRenderer
from classes.Player import Player

windPower = (0, 0, 0, -1, -1, -2, -1, -1, -1, -1)

r = WinyPathRenderer(10, windPower, 700, 700)
r.draw_board()
p = Player(x=-5, y=0)


r.addObject(p)
p.moveX(1)
r.draw_frame()
p.moveX(1)
r.draw_frame()
p.moveX(1)
r.draw_frame()
input()
