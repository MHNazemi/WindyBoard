from interfaces.IRenderer import IRenderer
from interfaces.IPhysic import IPhysic


class IEngine:
    def run(self):
        raise NotImplementedError()

    def resetGame(self):
        raise NotImplementedError()
