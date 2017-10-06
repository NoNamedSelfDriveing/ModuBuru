import sys
from PyQt4 import QtGui

class Building(QtGui.QMainWindow):
    boldFont = QtGui.QFont('SansSerif', 20, QtGui.QFont.Bold)
    noBoldFont = QtGui.QFont('SansSerif', 20)

    def __init__(self):
        super(Building, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Buying Building')
        self.setBackground()

        # '주택' 텍스트 표시 Label
        lblHome = QtGui.QLabel('주택', self)
        lblHome.setFont(Building.boldFont)
        lblHome.resize(lblHome.sizeHint())
        lblHome.move(200, 100)

        # 주택 수 선택 CheckBox
        cmbHomeNum = QtGui.QComboBox(self)
        cmbHomeNum.setFont(Building.boldFont)
        #cmbHomeNum.addItem('2')
        #cmbHomeNum.ad
        for i in range(0, 4):
            cmbHomeNum.addItem(str(i+1))
        cmbHomeNum.resize(200, 80)
        cmbHomeNum.move(200, 200)
        self.show()

    def setBackground(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()
    def initBoard(self):
        self.setStyleSheet('background-image: url("../image/game_start_bg.jpg")')

def run():
    app = QtGui.QApplication([])
    window = Building()
    app.exec_()

run()
