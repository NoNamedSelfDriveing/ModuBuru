import sys
from PyQt4 import QtGui, QtCore

class Bankrupt(QtGui.QMainWindow):
    def __init__(self):
        super(Bankrupt, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.set_background()

        # '부동산 리스트' 텍스트 표시할 Label
        lblRealtyListTxt = QtGui.QLabel('부동산 리스트', self)
        lblRealtyListTxt.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
        lblRealtyListTxt.resize(lblRealtyListTxt.sizeHint())
        lblRealtyListTxt.move(300, 30)

        # 부동산 리스트 표시할 ScrollArea 생성
        self.realtyScrollArea = QtGui.QScrollArea(self)
        self.realtyScrollArea.setWidgetResizable(True)
        self.realtyScrollArea.setFixedWidth(800)
        self.realtyScrollArea.setFixedHeight(500)
        self.realtyScrollArea.move(50, 100)
        self.realtyScrollAreaWidgetContents = QtGui.QWidget(self.realtyScrollArea)
        self.realtyScrollArea.setWidget(self.realtyScrollAreaWidgetContents)

        self.verticalLayoutScroll = QtGui.QVBoxLayout(self.realtyScrollAreaWidgetContents)

        '''for i in range(0, 10):
            pushButton = QtGui.QPushButton('Hello', self)
            pushButton.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
            pushButton.resize(100, 100)
            self.verticalLayoutScroll.addWidget(pushButton)
        '''

        realtyList = ['서울', '타이페이', '시드니', '퀸엘리자베스호']
        for i in realtyList:
            pushButton = QtGui.QPushButton(i, self)
            pushButton.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
            pushButton.resize(100, 100)
            if i == '서울' or i == '시드니':
                #pushButton.setIcon(QtGui.QIcon('../image/green.png'))
                #pushButton.setIconSize(QtCore.QSize(100, 100))
                pushButton.setStyleSheet('background-image: url("../image/green.png")')
            self.verticalLayoutScroll.addWidget(pushButton)


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
        self.lblFine.setText('￦ 2,000,000')

        # '합계' 텍스트 표시 Label
        lblTotalTxt = QtGui.QLabel('합계', self)
        lblTotalTxt.setFont(QtGui.QFont('SansSerif', 30, QtGui.QFont.Bold))
        lblTotalTxt.resize(lblTotalTxt.sizeHint())
        lblTotalTxt.move(50, 620)

        # 선택한 건물 가치 총액 표시할 Label
        self.lblTotalPrice = QtGui.QLabel(self)
        self.lblTotalPrice.setFont(QtGui.QFont('SansSerif', 30))
        self.lblTotalPrice.resize(400, 50)
        self.lblTotalPrice.move(200, 620)
        self.lblTotalPrice.setText('￦ 1,500,000')

        # 파산 신청 PushButton
        self.btnBankrupt = QtGui.QPushButton('파산\n신청', self)
        self.btnBankrupt.clicked.connect(self.go_bankrupt)
        self.btnBankrupt.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        self.btnBankrupt.resize(200, 200)
        self.btnBankrupt.move(1000, 200)

        # 보유 부동산 판매 완료 PushButton
        self.btnOK = QtGui.QPushButton('OK', self)
        self.btnOK.clicked.connect(self.sell_realty)
        self.btnOK.setEnabled(False)
        self.btnOK.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        self.btnOK.resize(200, 200)
        self.btnOK.move(1000, 450)

        self.show()

    # 배경 설정 method
    def set_background(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # 납부금(벌금) 표시 method
    def show_fine(self):
    # self.lblFine.setText(fine)
        pass

    # 부동산 리스트 ScrollArea에 들어갈 부동산 리스트 생성 및 채워넣는 method
    def show_realty_list(self):
    # while(condition):
    # self.verticalLayoutScroll.addWidget(QWidgt)
        pass

    # 부동산 리스트 목록 PushButton 클릭 이벤트
    def select_realty(self):
    # self.lblTotalPrice.setText(currentPrice)
    # if currentPrice >= fine:
    # self.btnOK.setEnabled(True)
        pass

    # 부동산 판매 버튼(OK) 클릭 이벤트
    def sell_realty(self):
    # 현재 플레이어 부동산 내역에서 선택된 내용 삭제
    # sys.exit()
        pass

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
        self.setStyleSheet('background-image: url("../image/blue_marble.jpg")')

def run():
    app = QtGui.QApplication([])
    window = Bankrupt()
    app.exec_()

run()
