from interfaces import IPhysics


class WindPhysics(IPhysics.IPhysics):
    def __init__(self, values, objects, x_range, y_range):
        self.values = values
        self.objects = objects
        self.x_range = x_range
        self.y_range = y_range

    def apply(self):
        for o_ in self.objects:
            x, y = o_.getCurrentPos()
            if x in self.values:
                o_.moveY(self.values[x])
            self.barrier(o_)

    def barrier(self, o):
        x, y = o.getCurrentPos()
        if not self.x_range[0] <= x:
            x = self.x_range[0]
        elif not self.x_range[1] >= x:
            x = self.x_range[1]

        if not self.y_range[0] <= y:
            y = self.y_range[0]
        elif not self.y_range[1] >= y:
            y = self.y_range[1]

        o.updatePostion(x, y)
