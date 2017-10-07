import sys
from PyQt4 import QtGui, QtCore
from functools import partial

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
        self.chkVilla1 = QtGui.QCheckBox('별장 1', self)
        self.chkVilla1.stateChanged.connect(partial(self.show_selected, self.chkVilla1.text()))
        self.chkVilla1.setFont(Building.boldFont)
        self.chkVilla1.resize(400, 150)
        self.chkVilla1.move(50, 220)

        # '별장 2' 선택 CheckBox
        self.chkVilla2 = QtGui.QCheckBox('별장 2', self)
        self.chkVilla2.stateChanged.connect(partial(self.show_selected, self.chkVilla2.text()))
        self.chkVilla2.setFont(Building.boldFont)
        self.chkVilla2.resize(400, 150)
        self.chkVilla2.move(50, 470)

        # '빌딩' 선택 CheckBox
        self.chkBuilding = QtGui.QCheckBox('빌딩', self)
        self.chkBuilding.stateChanged.connect(partial(self.show_selected, self.chkBuilding.text()))
        self.chkBuilding.setFont(Building.boldFont)
        self.chkBuilding.resize(400, 150)
        self.chkBuilding.move(450, 220)

        # '호텔' 선택 CheckBox
        self.chkHotel = QtGui.QCheckBox('호텔', self)
        self.chkHotel.stateChanged.connect(partial(self.show_selected, self.chkHotel.text()))
        self.chkHotel.setFont(Building.boldFont)
        self.chkHotel.resize(400, 150)
        self.chkHotel.move(450, 470)

        # '선택한 건물' 텍스트 띄울 Label
        lblSelectedTxt = QtGui.QLabel('선택한 건물', self)
        lblSelectedTxt.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        lblSelectedTxt.resize(lblSelectedTxt.sizeHint())
        lblSelectedTxt.move(840, 20)

        # 선택한 건물 표시할 Label
        self.lblSelected = QtGui.QLabel(self)
        self.lblSelected.setFont(QtGui.QFont('SansSerif', 50))
        self.lblSelected.resize(200, 80)
        self.lblSelected.move(930, 140)
        #lblSelected.setText('별장 1')

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
        btnOK.clicked.connect(self.close_window)
        btnOK.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        btnOK.resize(200, 200)
        btnOK.move(920, 470)

        self.show()

    # 배경 설정 method
    def setBackground(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # 선택한 건물 표시 method
    def show_selected(self, text, state):
        checkBoxList = [self.chkVilla1, self.chkVilla2, self.chkBuilding, self.chkHotel]
        if state == QtCore.Qt.Checked:
            for checkBox in checkBoxList:
                if checkBox.text() != text:
                    checkBox.setEnabled(False)

            self.lblSelected.setText(text)
        else:
            for checkBox in checkBoxList:
                checkBox.setEnabled(True)
            self.lblSelected.setText('')

    # 현재 window 닫는 method
    def close_window(self):
        sys.exit()

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
