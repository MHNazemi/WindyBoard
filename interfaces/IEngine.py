from interfaces.IRenderer import IRenderer
from interfaces.IPhysic import IPhysic


class IEngine:
    def run(self):
        raise NotImplementedError()

    def addPhysics(self, physic: IPhysic):
        raise NotImplementedError()

    def addRenderer(self, renderer: IRenderer):
        raise NotImplementedError()

    def addAI(self, AI):
        raise NotImplementedError()

    def resetGame(self):
        raise NotImplementedError()
