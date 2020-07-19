from interfaces import IController


class WinyPathController(IController.I2DController):
    def __init__(self, obj):
        self.obj = obj

    def getKeyboardInput(self):

        getch = _Getch()
        i = getch().decode()
        while True:
            if i.lower() == "w":
                self.obj.moveY(1)
                break
            elif i.lower() == "d":
                self.obj.moveX(1)
                break
            elif i.lower() == "s":
                self.obj.moveY(-1)
                break
            elif i.lower() == "a":
                self.obj.moveX(-1)
                break
            print("Invalid Input! Try again")
            i = getch().decode()


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
