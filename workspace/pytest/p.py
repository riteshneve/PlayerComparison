import Tkinter
import tkMessageBox
import subprocess
import os
import pyautogui
import time
from Tkconstants import LEFT, BOTTOM, INSERT
import tkFileDialog
from Tkinter import Tk
from tkFileDialog import askopenfilename
from Tkinter import *

def runCodeCallBack():
    os.system('sec.py')

def openFileCallBack():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
    text.insert(INSERT, "OPEN File \"" + filename + "\"\n")
    secFile = open('sec.py', 'a')
    secFile.write(  "import subprocess\nimport os\nimport time\nimport pyautogui\n" +
                    "try:" + "\n" +
                    "\tp = subprocess.Popen(['notepad.exe', \"" + filename + "\"])" + "\n" +
                    "except Exception:" + "\n" +
                    "\tpass" + "\n")
    secFile.close()
    #os.system('sec.py')

def writesubmitKeys():
    text.insert(INSERT, "Enter Keystrokes \"" + data + "\"\n")
    secFile = open('sec.py', 'a')
    secFile.write(  "try:" + "\n" +
                    "\tpyautogui.typewrite('" + data + "', 0.25)" + "\n" +
                    "\tpyautogui.hotkey('ctrl', 's')" + "\n" +
                    "except Exception:" + "\n" +
                    "\tpass" + "\n")
    secFile.close()

def submitKeys(keystrokes, enterKeyWindow):
    global data
    data = keystrokes.get("1.0",'end-1c')
    enterKeyWindow.destroy()
    print data
    writesubmitKeys()

def enterKeyCallBack():
    global data
    enterKeyWindow = Toplevel()
    keystrokes = Text(enterKeyWindow)
    keystrokes.pack()
    keySubmitbutton = Button(enterKeyWindow,text="Submit", command=lambda: submitKeys(keystrokes, enterKeyWindow))
    keySubmitbutton.pack()

def enterDelayCallBack():
    text.insert(INSERT, "Enter Delay \"" + "5sec" + "\"\n")
    secFile = open('sec.py', 'a')
    secFile.write(  "time.sleep(5)" + "\n")
    secFile.close()

def launchWebsiteCallBack():
    text.insert(INSERT, "Launch Website \"" + "file:///C:/Users/R!TE$H/workspace/pytest/docs/sample.html" + "\"\n")
    secFile = open('sec.py', 'a')
    secFile.write(  "import webbrowser\n" +
                    "webbrowser.open('file:///C:/Users/R!TE$H/workspace/pytest/docs/sample.html')" + "\n")
    secFile.close()
    
data = "val"
#clear seconday file
open('sec.py', 'w').close()
#start the gui
print "***STARTING GUI***"
top = Tk()
#add frame
frame = Frame(top)
frame.pack(side = LEFT)
#add button
runCodeButton = Button(frame, text ="Run Code", command = runCodeCallBack)
runCodeButton.pack()
openFileButton = Button(frame, text ="Open File", command = openFileCallBack)
openFileButton.pack()
enterKeyButton = Button(frame, text ="Enter Keystrokes", command = enterKeyCallBack)
enterKeyButton.pack()
enterDelayButton = Button(frame, text ="Enter Delay", command = enterDelayCallBack)
enterDelayButton.pack()
launchWebsiteButton = Button(frame, text ="Launch Website", command = launchWebsiteCallBack)
launchWebsiteButton.pack()
#add text field
text = Text(top)
text.pack(side = LEFT)
print "***GUI LOADED***"
top.mainloop()