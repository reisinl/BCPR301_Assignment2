import TurtleDrawer
import tkinter
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import Parser
import sys
import TkDrawer
from tkinter import BOTH, END, LEFT

class FrontEnd(object):
    def __init__(self):
        self._initGUI()

    def _initGUI(self):
        # Tkinter root
        self.root = tkinter.Tk()
        self.root.title("Learn To Draw A Hog")
        try:
            self.root.iconbitmap("thatpigicon.ico")
        except:
            pass
        self.root.resizable(width=False, height=False)

        menu = tkinter.Menu(master=self.root)
        fileMenu = tkinter.Menu(menu, tearoff=0)

        fileMenu.add_command(label="Open", command=self.openFile)
        fileMenu.add_command(label="Save", command=self.saveFile)
        fileMenu.add_command(label="Exit", command=self.root.quit)

        runMenu = tkinter.Menu(menu, tearoff=0)
        runMenu.add_command(label="Turtle", command=self.drawTurtle)
        runMenu.add_command(label="Tkinter", command=self.drawTkinter)

        helpMenu = tkinter.Menu(menu, tearoff=0)
        helpMenu.add_command(label="About", command=self.showAbout)

        menu.add_cascade(label="File", menu=fileMenu)
        menu.add_cascade(label="Run", menu=runMenu)
        menu.add_cascade(label="Help", menu=helpMenu)
        self.root.config(menu=menu)

        self.canvas = tkinter.Canvas(master=self.root, cnf={"width": 500, "height": 200, "bg": "white"})
        self.canvas.pack(side=tkinter.TOP)

        self.text = scrolledtext.ScrolledText(master=self.root, cnf={"width": 80, "height": 10})
        self.text.pack(side=tkinter.BOTTOM)

        self._handleArguments()

        self.root.mainloop()

    def _getText(self):
        return self.text.get(index1="1.0", index2=END)

    def _setText(self, text):
        self.text.delete(index1="1.0", index2=END)
        self.text.insert(index="1.0", chars=text)

    def _clearCanvas(self):
        self.canvas.addtag_all("zipzap")
        self.canvas.delete("zipzap")

    def openFile(self):
        openedFile = filedialog.askopenfile(mode="r", filetypes=[("Hog Files", "*.hog")])
        if (openedFile is not None):
            fileData = openedFile.read()
            self._setText(fileData)

    def saveFile(self):
        savedFile = filedialog.asksaveasfile(mode="w", filetypes=[("Hog Files", "*.hog")])
        if (savedFile is not None):
            savedFile.write(self._getText())
            savedFile.close()

    def drawTurtle(self):
        self._clearCanvas()
        drawer = TurtleDrawer.TurtleDrawer(self.canvas)
        parser = Parser.Parser(drawer)
        commands = self._getText().splitlines()
        parser.parse(commands)

    def drawTkinter(self):
        self._clearCanvas()
        drawer = TkDrawer.TkDrawer(self.canvas)
        parser = Parser.Parser(drawer)
        commands = self._getText().splitlines()
        parser.parse(commands)

    def showAbout(self):
        messagebox.showinfo(title="Hogzilla", message="TIGr Frontend \nBy Umang & Chris")

    def _handleArguments(self):
        if (len(sys.argv) > 1):
            try:
                openedFile = file(sys.argv[1])
                fileData = openedFile.read()
                self._setText(fileData)
            except IOError:
                print("File not found")


f = FrontEnd()

