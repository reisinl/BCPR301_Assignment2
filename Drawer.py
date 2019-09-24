class Drawer(object):
    """ Responsible for defining an interface for drawing """

    def __init__(self, canvas):
        self.pencilBox = ["black", "red", "green", "blue"]
        self.canvas = canvas
        # self.selectPen(0)
        # self.penUp()

    def selectPen(self,penNum):
        print("Selected pen " + str(penNum))

    def penDown(self):
        print("pen down")

    def penUp(self):
        print("pen up")

    def drawLine(self, direction, distance):
        print("drawing line of length " + str(distance) + " at " + str(direction))

    def drawCircle(self, radius):
        print("drawing circle of radius " + str(radius))
