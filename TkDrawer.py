import Drawer
import tkinter
import sys

class TkDrawer(Drawer.Drawer):
    def __init__(self, canvas):
        self._x = canvas.winfo_reqwidth() / 4
        self._y = canvas.winfo_reqheight() / 6
        super().__init__(canvas)
        self.selectPen(0)
        self.penUp()

    def selectPen(self, penNum):
        try:
            self.pen_colour = self.pencilBox[penNum]
        except:
            self.pen_colour = self.pencilBox[0]

    def penDown(self):
        self.is_drawing = True

    def penUp(self):
        self.is_drawing = False

    def _translate(self, angle, distance):
        north = 90
        south = 270
        east = 0
        west = 180

        if angle == north:
            self._y = self._y - distance
        elif angle == south:
            self._y = self._y + distance
        elif angle == east:
            self._x = self._x + distance
        elif angle == west:
            self._x = self._x - distance

    def drawLine(self, direction, distance):

        start = (self._x, self._y)
        self._translate(direction, distance)
        end = (self._x, self._y)

        if self.is_drawing:
            self.canvas.create_line(start, end, fill=self.pen_colour)

    def drawCircle(self, radius):
        top_point = ((self._x - radius), (self._y - radius))
        bottom_point = ((self._x + radius), (self._y + radius))
        self.canvas.create_oval(top_point, bottom_point, outline=self.pen_colour)
