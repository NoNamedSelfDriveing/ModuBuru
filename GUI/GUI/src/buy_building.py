import sys
from PyQt4 import QtGui

class Building(QtGui.QMainWindow):
    boldFont = QtGui.QFont('SansSerif', 80, QtGui.QFont.Bold)
    noBoldFont = QtGui.QFont('SansSerif', 20)

    def __init__(self):
        super(Building, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Buying Building')
        self.setBackground()

        # '건물을 선택하세요' 텍스트 띄울 Label
        lblSelect = QtGui.QLabel('건물을 선택하세요', self)
        lblSelect.setFont(QtGui.QFont('SansSerif', 50))
        lblSelect.resize(lblSelect.sizeHint())
        lblSelect.move(90, 70)

        # '별장 1' 선택 CheckBox
        chkVilla1 = QtGui.QCheckBox('별장 1', self)
        chkVilla1.setFont(Building.boldFont)
        chkVilla1.resize(400, 150)
        chkVilla1.move(50, 220)

        # '별장 2' 선택 CheckBox
        chkVilla2 = QtGui.QCheckBox('별장 2', self)
        chkVilla2.setFont(Building.boldFont)
        chkVilla2.resize(400, 150)
        chkVilla2.move(50, 470)

        # '빌딩' 선택 CheckBox
        chkBuilding = QtGui.QCheckBox('빌딩', self)
        chkBuilding.setFont(Building.boldFont)
        chkBuilding.resize(400, 150)
        chkBuilding.move(450, 220)

        # '호텔' 선택 CheckBox
        chkHotel = QtGui.QCheckBox('호텔', self)
        chkHotel.setFont(Building.boldFont)
        chkHotel.resize(400, 150)
        chkHotel.move(450, 470)

        # '선택한 건물' 텍스트 띄울 Label
        lblSelectedTxt = QtGui.QLabel('선택한 건물', self)
        lblSelectedTxt.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        lblSelectedTxt.resize(lblSelectedTxt.sizeHint())
        lblSelectedTxt.move(840, 20)

        # 선택한 건물 표시할 Label
        lblSelected = QtGui.QLabel(self)
        lblSelected.setFont(QtGui.QFont('SansSerif', 50))
        lblSelected.resize(200, 80)
        lblSelected.move(930, 140)
        lblSelected.setText('별장 1')

        # '금액' 텍스트 띄울 Label
        lblPriceTxt = QtGui.QLabel('금액', self)
        lblPriceTxt.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        lblPriceTxt.resize(lblPriceTxt.sizeHint())
        lblPriceTxt.move(950, 270)

        # 선택한 건물 금액 표시할 Label
        lblPrice = QtGui.QLabel(self)
        lblPrice.setFont(QtGui.QFont('SansSerif', 30))
        lblPrice.resize(300, 80)
        lblPrice.move(900, 380)
        lblPrice.setText('W 0000')

        # 구매 완료할 PushButton
        btnOK = QtGui.QPushButton('완료', self)
        btnOK.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        btnOK.resize(200, 200)
        btnOK.move(920, 470)

        self.show()

    # 배경 설정 method
    def setBackground(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

# 배경 설정 Class
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
