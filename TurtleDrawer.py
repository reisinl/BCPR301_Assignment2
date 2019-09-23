import turtle
import Drawer


class TurtleDrawer(Drawer.Drawer):
    def __init__(self, canvas):
        self.pencilBox = ["black", "red", "green", "blue"]
        self.canvas = canvas
        self.yurtle = turtle.RawPen(self.canvas)
        self.yurtle.degrees()
        self.selectPen(0)
        self.penUp()
        
    def selectPen(self, penNum):
        try:
            self.yurtle.color(self.pencilBox[penNum])
        except:
            self.yurtle.color(self.pencilBox[0])
        
    def penDown(self):
        self.yurtle.down()
        
    def penUp(self):
        self.yurtle.up()
        
    def drawLine(self, direction, distance):
        self.yurtle.setheading(direction)
        self.yurtle.forward(distance)

    def drawCircle(self, radius):
        south = 270
        north = 90
        east = 0
        oldState = self.yurtle._drawing
        oldDirection = self.yurtle.heading()
        self.yurtle.up()
        self.yurtle.setheading(south)
        self.yurtle.forward(radius)
        self.yurtle.setheading(east)
        self.yurtle._drawing = oldState
        self.yurtle.circle(radius)
        self.yurtle.up()
        self.yurtle.setheading(north)
        self.yurtle.forward(radius)
        self.yurtle.setheading(oldDirection)
        self.yurtle._drawing = oldState