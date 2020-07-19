from interfaces.IRenderer import IRenderer


class IEngine:
    def run(self):
        raise NotImplementedError()

    def apply_init(self):
        raise NotImplementedError()

    def apply_renderer(self):
        raise NotImplementedError()

    def apply_logic(self):
        raise NotImplementedError()

    def apply_controller(self):
        raise NotImplementedError()

    def apply_physics(self):
        raise NotImplementedError()

    def apply_AI(self):
        raise NotImplementedError()

    def resetGame(self):
        raise NotImplementedError()
