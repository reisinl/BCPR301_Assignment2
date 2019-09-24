from TurtleDrawer import TurtleDrawer
import tkinter
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import Parser
import sys
from TkDrawer import TkDrawer
from Drawer import Drawer
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
        file_menu = tkinter.Menu(menu, tearoff=0)

        file_menu.add_command(label="Open", command=self.openFile)
        file_menu.add_command(label="Save", command=self.saveFile)
        file_menu.add_command(label="Exit", command=self.root.quit)

        self.canvas = tkinter.Canvas(master=self.root, cnf={"width": 500, "height": 200, "bg": "white"})
        self.canvas.pack(side=tkinter.TOP)
        self.text = scrolledtext.ScrolledText(master=self.root, cnf={"width": 80, "height": 10})
        self.text.pack(side=tkinter.BOTTOM)

        self._handleArguments()

        print("self.text")
        print(self.text)
        run_menu = tkinter.Menu(menu, tearoff=0)
        run_menu.add_command(label="Turtle", command=self.drawTurtle)
        run_menu.add_command(label="Tkinter", command=self.drawTkinter)
        # runMenu.add_command(label="Turtle", command=self.draw, variable=turtle_drawer)
        # runMenu.add_command(label="Tkinter", command=self.draw, variable=tkinter_drawer)

        help_menu = tkinter.Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.showAbout)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Run", menu=run_menu)
        menu.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menu)

        # self.canvas = tkinter.Canvas(master=self.root, cnf={"width": 500, "height": 200, "bg": "white"})
        # self.canvas.pack(side=tkinter.TOP)
        # self.text = scrolledtext.ScrolledText(master=self.root, cnf={"width": 80, "height": 10})
        # self.text.pack(side=tkinter.BOTTOM)
        #
        # self._handleArguments()

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
        opened_file = filedialog.askopenfile(mode="r", filetypes=[("Hog Files", "*.hog")])
        if (opened_file is not None):
            file_data = opened_file.read()
            self._setText(file_data)

    def saveFile(self):
        saved_file = filedialog.asksaveasfile(mode="w", filetypes=[("Hog Files", "*.hog")])
        if (saved_file is not None):
            saved_file.write(self._getText())
            saved_file.close()

    def draw(self, drawer: Drawer):
        # self._clearCanvas()
        # drawer = TurtleDrawer.TurtleDrawer(self.canvas)
        parser = Parser.Parser(drawer)
        commands = self._getText().splitlines()
        print(commands)
        parser.parse(commands)

    def drawTurtle(self):
        self._clearCanvas()
        self.draw(TurtleDrawer(self.canvas))
        # parser = Parser.Parser(drawer)
        # commands = self._getText().splitlines()
        # print("drawTurtle")
        # print(commands)
        # parser.parse(commands)

    def drawTkinter(self):
        self._clearCanvas()
        self.draw(TkDrawer(self.canvas))
        # parser = Parser.Parser(drawer)
        # commands = self._getText().splitlines()
        # print("drawTkinter")
        # print(commands)
        # parser.parse(commands)

    def showAbout(self):
        messagebox.showinfo(title="Hogzilla", message="TIGr Frontend \nBy Umang & Chris")

    def _handleArguments(self):
        if (len(sys.argv) > 1):
            try:
                opened_file = file(sys.argv[1])
                fileData = opened_file.read()
                self._setText(fileData)
            except IOError:
                print("File not found")


f = FrontEnd()
