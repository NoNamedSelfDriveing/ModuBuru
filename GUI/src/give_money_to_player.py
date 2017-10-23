import sys
import os
from PyQt4 import QtGui, QtCore

class GiveMoneyToPlayer(QtGui.QMainWindow):
    def __init__(self):
        super(GiveMoneyToPlayer, self).__init__()
        self.setGeometry(200, 100, 900, 500)
        self.setWindowTitle('Give Money to Player')
        self.setBackground()

        self.lblGiveToPlayerTxt = QtGui.QLabel(self)
        self.lblGiveToPlayerTxt.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
        self.lblGiveToPlayerTxt.resize(800, 100)
        self.lblGiveToPlayerTxt.move(70, 50)
        self.lblGiveToPlayerTxt.setText('Player A에게 아래 금액을 지급하십시오')


        self.lblPrice = QtGui.QLabel(self)
        self.lblPrice.setFont(QtGui.QFont('SansSerif', 70, QtGui.QFont.Bold))
        self.lblPrice.resize(550, 100)
        self.lblPrice.move(30, 250)
        self.lblPrice.setText('￦ 50,000')

        self.btnOK = QtGui.QPushButton('지급\n완료', self)
        self.btnOK.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        self.btnOK.clicked.connect(self.closeApplication)
        self.btnOK.resize(250, 250)
        self.btnOK.move(620, 200)

        self.showPrice()
        self.show()

    def setBackground(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    def showPrice(self):
        playerName = sys.argv[1]
        price = sys.argv[2]
        self.lblGiveToPlayerTxt.setText('%s에게 아래 금액을 지급하시오' % playerName)
        self.lblPrice.setText('￦ %s' % price)
        
    def closeApplication(self):
        sys.exit()

class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()

    def initBoard(self):
        self.setStyleSheet('background-image: url("../image/green.png")')

def run():
    app = QtGui.QApplication([])
    window = GiveMoneyToPlayer()
    app.exec_()

run()
