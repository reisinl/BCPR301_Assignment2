from appJar import gui

app=gui()

app.startTabbedFrame("TabbedFrame")
app.startTab("Python")
app.addLabel("L1", "Python is awsome")
app.stopTab()

app.startTab("C#")
app.addLabel("l1", "c# is good")
app.stopTab()

app.startTab("Java")
app.addLabel("l3", "Java is very Complex")
app.stopTab()
app.stopTabbedFrame()

app.go()
