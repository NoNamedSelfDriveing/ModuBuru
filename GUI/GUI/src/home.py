import sys
import os
import csv
from PyQt4 import QtGui

playerList = []

# Player 정보 관리 클래스
class Player:
    initialCash = ['4560000', '3680000', '2900000']
    playerCode = ['A', 'B', 'C', 'D']
    def __init__(self, totalNumOfPlayer, playerNum):
        self.name = 'Player %s' % Player.playerCode[playerNum]
        self.cash = Player.initialCash[totalNumOfPlayer-2]  # 2~4명인데 배열은 0번부터이므로 -2
        self.realtyValue = '0'
        self.realtyList = {}

class Home(QtGui.QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Home')
        self.set_background()

        # Font Object
        boldFont = QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold)
        noBoldFont = QtGui.QFont('SansSerif', 50)

        # 'Now Turn' 텍스트 표시 Label
        lblNowTurn = QtGui.QLabel('Now Turn', self)
        lblNowTurn.setFont(boldFont)
        lblNowTurn.resize(lblNowTurn.sizeHint())
        lblNowTurn.move(50, 50)

        # 현재 턴의 플레이어 이름 띄울 Label
        self.lblNowPlayerName = QtGui.QLabel('', self)
        self.lblNowPlayerName.setFont(noBoldFont)
        self.lblNowPlayerName.resize(self.lblNowPlayerName.sizeHint())
        self.lblNowPlayerName.move(450, 50)

        # 순서를 다음 턴으로 넘길 PushButton
        btnChangeTurn = QtGui.QPushButton('Next\nTurn', self)
        btnChangeTurn.setFont(boldFont)
        btnChangeTurn.clicked.connect(self.change_turn)
        btnChangeTurn.resize(250, 200)
        btnChangeTurn.move(1000, 270)

        # '현금 소유액' 텍스트 표시 Label
        lblNowCash = QtGui.QLabel('현금 소유액', self)
        lblNowCash.setFont(boldFont)
        lblNowCash.resize(lblNowCash.sizeHint())
        lblNowCash.move(50, 200)

        # 현재 턴의 플레이어 현금 소유액 띄울 Label
        self.lblNowPlayerCash = QtGui.QLabel('', self)
        self.lblNowPlayerCash.setFont(noBoldFont)
        self.lblNowPlayerCash.resize(self.lblNowPlayerCash.sizeHint())
        self.lblNowPlayerCash.move(450, 200)

        # '부동산 가치' 텍스트 띄울 Label
        lblRealtyValue = QtGui.QLabel('부동산 가치', self)
        lblRealtyValue.setFont(boldFont)
        lblRealtyValue.resize(lblRealtyValue.sizeHint())
        lblRealtyValue.move(50, 350)

        # 현재 턴의 플레이어 부동산 가치 띄울 Label
        self.lblNowPlayerRealtyValue = QtGui.QLabel('', self)
        self.lblNowPlayerRealtyValue.setFont(noBoldFont)
        self.lblNowPlayerRealtyValue.resize(self.lblNowPlayerRealtyValue.sizeHint())
        self.lblNowPlayerRealtyValue.move(450, 350)

        # '바코드 입력' 텍스트 띄울 Label
        lblBarcodeInput = QtGui.QLabel('바코드 입력', self)
        lblBarcodeInput.setFont(boldFont)
        lblBarcodeInput.resize(lblBarcodeInput.sizeHint())
        lblBarcodeInput.move(200, 500)

        # 바코드 정보 입력할 textbox
        self.edtBarcodeInfo = QtGui.QLineEdit(self)
        self.edtBarcodeInfo.setFont(QtGui.QFont('SansSerif', 30))
        self.edtBarcodeInfo.resize(400, 100)
        self.edtBarcodeInfo.move(600, 500)
        self.edtBarcodeInfo.setFocus()
        self.edtBarcodeInfo.returnPressed.connect(self.enter_pressed)

        # 플레이어 리스트 설정하기
        self.set_player_list()

        self.show()

    # 배경 설정 method
    def set_background(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # 플레이어 리스트 설정 method
    def set_player_list(self):
        self.nowPlayerNum = 0    # 현재 플레이어가 몇 번째 플레이어인지 저장할 변수 

        # information.txt 읽어서 플레이이 인원 수 구하기
        f = open('information.txt', 'r')
        line = f.readline()
        self.player_num = int(line[line.find('=')+1])  # 'player_num=' 다음 오는 인원 가져오기
        f.close()

        # 플레이어 리스트 설정하기
        # 플레이어 인원 수 만큼 Player 객체 배열로 생성
        for i in range(0, self.player_num):
            playerList.append(Player(self.player_num, i))

        # 첫번째 플레이어 정보로 초기 세팅
        self.lblNowPlayerName.setText( playerList[self.nowPlayerNum].name)
        self.lblNowPlayerCash.setText('￦ %s' % playerList[self.nowPlayerNum].cash)
        self.lblNowPlayerRealtyValue.setText('￦ %s' % playerList[self.nowPlayerNum].realtyValue)

        self.lblNowPlayerName.resize(self.lblNowPlayerName.sizeHint())
        self.lblNowPlayerCash.resize(self.lblNowPlayerCash.sizeHint())
        self.lblNowPlayerRealtyValue.resize(self.lblNowPlayerRealtyValue.sizeHint())

    # Next Turn 버튼 클릭 이벤트 method
    def change_turn(self):
        self.nowPlayerNum += 1
        if self.nowPlayerNum == self.player_num:    # 현재 플레이어가 마지막 순서의 플레이어면
            self.nowPlayerNum = 0                   # 처음 플레이어로 Back

        # 다음 플레이어 정보 표시
        self.lblNowPlayerName.setText(playerList[self.nowPlayerNum].name)
        self.lblNowPlayerCash.setText('￦ %s' % playerList[self.nowPlayerNum].cash)
        self.lblNowPlayerRealtyValue.setText('￦ %s' % playerList[self.nowPlayerNum].realtyValue)

        self.edtBarcodeInfo.setFocus()    #바코드 정보 입력 textbox로 포커스 이동

    # 바코드 입력 QLineEdit에 엔터 키 입력 이벤트 method
    def enter_pressed(self):
        landNameColumn = 2
        landCodeColumn = 3
        landName = self.edtBarcodeInfo.text()

        f = open('./realty_info.csv', 'r')
        csvReader = csv.reader(f)
        for col in csvReader:
            if col[landNameColumn] == landName:
                # 부가 건물이 있는 땅이면
                if col[landCodeColumn] == '1':
                    os.system('python3 buy_realty_with_building.py %s' % landName)
                # 부가 건물이 없는 땅이면
                elif col[landCodeColumn] == '0':
                    os.system('python3 buy_realty_without_building.py %s' % landName)
                break

        self.edtBarcodeInfo.setText('')

# window background class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.init_board()
    def init_board(self):
        self.setStyleSheet('background-image: url("../image/green.png")')

def run():
    app = QtGui.QApplication([])
    window = Home()
    app.exec_()

run()
