from Tkinter import *
from getPlayerDetails import *
from Tkconstants import LEFT
import tkFont

def insertDataInGrid(stats, listPlayer):
    gotTestBat = False
    for stat in stats:
        stat = stat.getText()
        if "Tests" in stat:
            stat = re.sub('Tests\n', '', stat)
            if gotTestBat == False:
                testBatData = stat.split('\n')
                gotTestBat = True
            else:
                testBowlData = stat.split('\n')
    
    print testBatData[7]
        
    listPlayer.pack(side = LEFT)
    listPlayer.insert(1, "")
    listPlayer.insert(2, "")
    listPlayer.insert(3, testBatData[1])
    listPlayer.insert(4, testBatData[4])
    listPlayer.insert(5, testBatData[5])
    listPlayer.insert(6, testBatData[6])
    listPlayer.insert(7, testBatData[9])
    listPlayer.insert(8, testBatData[10])
    listPlayer.insert(9, "")
    listPlayer.insert(10, testBowlData[5])
    listPlayer.insert(11, testBowlData[8])
    listPlayer.insert(12, testBowlData[9])

def valueGET(val1, val2, listPlayer1, listPlayer2):
    print val1 + "  " + val2
    statsPlayer1 = getPlayerDetails(val1)
    statsPlayer2 = getPlayerDetails(val2)
    
    if statsPlayer1 == "":
        print "no data"
    else:
        insertDataInGrid(statsPlayer1, listPlayer1)
    if statsPlayer2 == "":
        print "no data"
    else:
        insertDataInGrid(statsPlayer2, listPlayer2)    

def insertStatDetails(listStats):
    listStats.insert(1, "")
    listStats.insert(2, "Batting")
    listStats.insert(3, "Mat")
    listStats.insert(4, "Runs")
    listStats.insert(5, "HS")
    listStats.insert(6, "Ave")
    listStats.insert(7, "100s")
    listStats.insert(8, "50s")
    listStats.insert(9, "Bowling")
    listStats.insert(10, "Wkts")
    listStats.insert(11, "Ave")
    listStats.insert(12, "Econ")

class ContentUI():
    def showLogin(self, frame, playerDataFrame):

        self.contentUI = ContentUI()    

        playerLabel1 = Label(frame, text="Player 1")
        playerLabel1.pack(side = LEFT)
        playerLabel1.grid(row=0, column=0)
        
        playerLabel2 = Label(frame, text="Player 2")
        playerLabel2.pack(side = LEFT)
        playerLabel2.grid(row=0, column=1)
        
        playerInput1 = Entry(frame, bd =5)
        playerInput1.pack(side = LEFT)
        playerInput1.grid(row=1, column=0)

        playerInput2 = Entry(frame, bd =5)
        playerInput2.pack(side = LEFT)
        playerInput2.grid(row=1, column=1)

        submit = Button(frame, text="Enter", width=15, command=lambda: valueGET(playerInput1.get(), playerInput2.get(), listPlayer1, listPlayer2))
        submit.grid(row=2, column=0, columnspan=2)
        
        listStats = Listbox(playerDataFrame, width=20, height=14)
        listStats.pack(side = LEFT)
        insertStatDetails(listStats)
        listPlayer1 = Listbox(playerDataFrame, width=10, height=14)
        listPlayer2 = Listbox(playerDataFrame, width=10, height=14)

class UIDisplay():
    def play(self):
        root = Tk()
        
        root.title("title")
        root.geometry("640x480")

        app = Frame(root)
        playerDataFrame = Frame(root)
        contentUI = ContentUI()
        contentUI.showLogin(app, playerDataFrame)

        app.grid()
        playerDataFrame.grid()
        root.mainloop()

adkooPlay = UIDisplay()
adkooPlay.play()