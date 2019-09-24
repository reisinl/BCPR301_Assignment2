import sys
import tkinter
from TurtleDrawer import TurtleDrawer
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from TkDrawer import TkDrawer
from Drawer import Drawer
from tkinter import END
from Parser import Parser


class FrontEnd(object):
    def __init__(self):
        # Tkinter root
        self.root = tkinter.Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("Learn To Draw A Hog")
        self.canvas = tkinter.Canvas(master=self.root, cnf={
            "width": 500, "height": 200, "bg": "white"
        })
        self.canvas.pack(side=tkinter.TOP)
        self.text = scrolledtext.ScrolledText(master=self.root, cnf={
            "width": 80, "height": 10
        })
        self.text.pack(side=tkinter.BOTTOM)
        self._handleArguments()
        self.menu = tkinter.Menu(master=self.root)
        self._initGUI()

    def _initGUI(self):
        self.menu.add_cascade(label="File", menu=self._make_file_menu())
        self.menu.add_cascade(label="Run", menu=self._make_run_menu())
        self.menu.add_cascade(label="Help", menu=self._make_help_menu())
        self.root.config(menu=self.menu)
        self.root.mainloop()

    def _make_help_menu(self):
        help_menu = tkinter.Menu(self.menu, tearoff=0)
        help_menu.add_command(label="About", command=self.showAbout)
        return help_menu

    def _make_file_menu(self):
        file_menu = tkinter.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.openFile)
        file_menu.add_command(label="Save", command=self.saveFile)
        file_menu.add_command(label="Exit", command=self.root.quit)
        return file_menu

    def _make_run_menu(self):
        run_menu = tkinter.Menu(self.menu, tearoff=0)
        run_menu.add_command(label="Turtle", command=self.drawTurtle)
        run_menu.add_command(label="Tkinter", command=self.drawTkinter)
        return run_menu

    def _getText(self):
        return self.text.get(index1="1.0", index2=END)

    def _setText(self, text):
        self.text.delete(index1="1.0", index2=END)
        self.text.insert(index="1.0", chars=text)

    def _clearCanvas(self):
        self.canvas.addtag_all("zipzap")
        self.canvas.delete("zipzap")

    def openFile(self):
        opened_file = filedialog.askopenfile(
            mode="r", filetypes=[("Hog Files", "*.hog")]
        )
        if opened_file is not None:
            file_data = opened_file.read()
            self._setText(file_data)

    def saveFile(self):
        saved_file = filedialog.asksaveasfile(
            mode="w", filetypes=[("Hog Files", "*.hog")]
        )
        if saved_file is not None:
            saved_file.write(self._getText())
            saved_file.close()

    def draw(self, drawer: Drawer):
        parser = Parser(drawer)
        commands = self._getText().splitlines()
        print(commands)
        parser.parse(commands)

    def drawTurtle(self):
        self._clearCanvas()
        self.draw(TurtleDrawer(self.canvas))

    def drawTkinter(self):
        self._clearCanvas()
        self.draw(TkDrawer(self.canvas))

    def showAbout(self):
        messagebox.showinfo(
            title="Hogzilla", message="TIGr Frontend \nBy Umang & Chris"
        )

    def _handleArguments(self):
        if len(sys.argv) > 1:
            try:
                opened_file = open(sys.argv[1])
                read_value = opened_file.read()
                self._setText(read_value)
            except IOError:
                print("File not found")

f = FrontEnd()
