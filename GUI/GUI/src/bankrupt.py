import sys
from PyQt4 import QtGui

class Bankrupt(QtGui.QMainWindow):
    def __init__(self):
        super(Bankrupt, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.set_background()

        # '납부금' 텍스트 표시 Label
        lblFineTxt = QtGui.QLabel('납부금', self)
        lblFineTxt.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
        lblFineTxt.resize(lblFineTxt.sizeHint())
        lblFineTxt.move(1030, 30)

        # 납부금 금액 표시할 Label
        self.lblFine = QtGui.QLabel(self)
        self.lblFine.setFont(QtGui.QFont('SansSerif', 30))
        self.lblFine.resize(300, 50)
        self.lblFine.move(920, 100)
        self.lblFine.setText('￦ 00, 000')

        # '합계' 텍스트 표시 Label
        lblTotalTxt = QtGui.QLabel('합계', self)
        lblTotalTxt.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
        lblTotalTxt.resize(lblTotalTxt.sizeHint())
        lblTotalTxt.move(50, 600)

        # 선택한 건물 가치 총액 표시할 Label
        lblTotalPrice = QtGui.QLabel(self)
        lblTotalPrice.setFont(QtGui.QFont('SansSerif', 30))
        lblTotalPrice.resize(200, 50)
        lblTotalPrice.move(200, 600)
        lblTotalPrice.setText('￦ 00,000')

        # 파산 신청 PushButton
        btnBankrupt = QtGui.QPushButton('파산\n신청', self)
        btnBankrupt.clicked.connect(self.go_bankrupt)
        btnBankrupt.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        btnBankrupt.resize(200, 200)
        btnBankrupt.move(1000, 200)

        # 보유 부동산 판매 완료 PushButton
        btnOK = QtGui.QPushButton('OK', self)
        btnOK.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        btnOK.resize(200, 200)
        btnOK.move(1000, 450)

        self.show()

    # 배경 설정 method
    def set_background(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # '파산 신청' Button 클릭 이벤트
    def go_bankrupt(self):
        choice = QtGui.QMessageBox.question(self, '파산 신청', '정말로 파산하시겠습니까?(모든 재산이 사라집니다)', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()

# 배경 설정 class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.init_board()

    def init_board(self):
        self.setStyleSheet('background-image: url("../image/green.png")')

def run():
    app = QtGui.QApplication([])
    window = Bankrupt()
    app.exec_()

run()
