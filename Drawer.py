class Drawer(object):
    """ Responsible for defining an interface for drawing """

    def __init__(self, canvas):
        self.pencilBox = ["black", "red", "green", "blue"]
        self.canvas = canvas
