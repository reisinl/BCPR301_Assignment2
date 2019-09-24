import turtle
import Drawer


class TurtleDrawer(Drawer.Drawer):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.my_turtle = turtle.RawPen(self.canvas)
        self.my_turtle.degrees()
        self.selectPen(0)
        self.penUp()

    def selectPen(self, penNum):
        try:
            self.my_turtle.color(self.pencilBox[penNum])
        except:
            self.my_turtle.color(self.pencilBox[0])

    def penDown(self):
        self.my_turtle.down()

    def penUp(self):
        self.my_turtle.up()

    def drawLine(self, direction, distance):
        self.my_turtle.setheading(direction)
        self.my_turtle.forward(distance)

    def drawCircle(self, radius):
        south = 270
        north = 90
        east = 0
        old_state = self.my_turtle.drawing
        old_direction = self.my_turtle.heading()
        self.my_turtle.up()
        self.my_turtle.setheading(south)
        self.my_turtle.forward(radius)
        self.my_turtle.setheading(east)
        self.my_turtle._drawing = old_state
        self.my_turtle.circle(radius)

        self.my_turtle.up()
        self.my_turtle.setheading(north)
        self.my_turtle.forward(radius)
        self.my_turtle.setheading(old_direction)
        self.my_turtle._drawing = old_state
