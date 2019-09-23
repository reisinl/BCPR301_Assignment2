import Drawer
import tkinter
import sys

class TkDrawer(Drawer.Drawer):
    def __init__(self, canvas):
        self._x = canvas.winfo_reqwidth() / 2
        self._y = canvas.winfo_reqheight() / 2
        
        self.pencilBox = ["black", "red", "green", "blue"]
        self.canvas = canvas
        self.selectPen(0)
        self.penUp()
        
    def selectPen(self, penNum):
        try:
            self.pencolour = self.pencilBox[penNum]
        except:
            self.pencolour = self.pencilBox[0]

    def penDown(self):
        self.isDrawing = True
        
    def penUp(self):
        self.isDrawing = False
        
    def _translate(self, angle, distance):
        north = 90
        south = 270
        east = 0
        west = 180
        
        if(angle == north):
            self._y = self._y - distance
        elif(angle == south):
            self._y = self._y + distance
        elif(angle == east):
            self._x = self._x + distance
        elif(angle == west):
            self._x = self._x - distance

    def drawLine(self, direction, distance):

        start = (self._x, self._y)
        self._translate(direction, distance)
        end = (self._x, self._y)

        if(self.isDrawing):
            self.canvas.create_line(start, end, fill=self.pencolour)

    def drawCircle(self, radius):
        topPoint = ((self._x - radius), (self._y - radius))
        bottomPoint = ((self._x + radius), (self._y + radius))
        self.canvas.create_oval(topPoint, bottomPoint, outline=self.pencolour)
