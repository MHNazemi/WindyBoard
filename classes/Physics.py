from interfaces import IPhysic


class Wind(IPhysic):
    def __init__(self, values, objects):
        self.values = values
        self.objects = objects

    def apply(self):
        for o_ in objects:
            x = o_.getCurrentPos()
            o_.moveY(self.values[x])
