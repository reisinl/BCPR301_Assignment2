
class Drawer(object):
    """ Responsible for defining an interface for drawing """
    def __init__(self):
        pass
    def selectPen(self,penNum):
        print("Selected pen " + str(penNum))

    def penDown(self):
        print("pen down")

    def penUp(self):
        print("pen up")

    def drawLine(self, direction, distance):
        print("drawing line of length " + str(distance) + " at " + str(direction))


class Parser(object):

    def __init__(self):
        self.drawer = Drawer()
        self.source = []
        self.command = ""
        self.data = 0

    def parse(self, rawSource):
        self.source = rawSource
        for line in self.source:
            self.command = line[0]
            try:
                self.data=int(line[2])
            except:
                self.data = 0
            if self.command == "P":
                self.drawer.selectPen(self.data)
            if self.command == "D":
                self.drawer.penDown()
            if self.command == "N":
                self.drawer.drawLine(0,self.data)
            if self.command == "E":
                self.drawer.drawLine(90,self.data)
            if self.command == "S":
                self.drawer.drawLine(180,self.data)
            if self.command == "W":
                self.drawer.drawLine(270,self.data)
            if self.command == "U":
                self.drawer.penUp()


class SourceReader(object):
    """ responsibe for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards """
    def __init__(self):
        self.parser = Parser()
        self.source = []

    def go(self):
        self.source.append("P 2 # select pen 2")
        self.source.append("D	# pen down")
        self.source.append("W 2	# draw west 2cm")
        self.source.append("N 1	# then north 1")
        self.source.append("E 2	# then east 2")
        self.source.append("S 1")
        self.source.append("U	# pen up")
        self.parser.parse(self.source)


if __name__ == "__main__":
        s = SourceReader()
        s.go()
