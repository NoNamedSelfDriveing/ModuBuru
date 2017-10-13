import sys
import os
import csv
#import buy_realty_with_building # 해당 모듈의 딕셔너리 키 값 읽어오기 실패
from PyQt4 import QtGui

playerList = []

# 부동산 관리 클래스
class RealtyInfo:
    realtyOwner = {}    # 각각 토지에 소유자 이름 저장
    realtyBuildingNum = {}  # 각각 토지에 각 건물(빌라, 빌딩, 호텔) 수 저장

    # 각각 토지에 소유자 이름 저장 딕셔너리, 각 건물 수 저장 딕셔너리 생성 및 초기화 method
    # @classmethod
    #def create_realty_dict(cls):
    landNameColumn = 2
    f = open('./realty_info.csv')
    csvReader = csv.reader(f)

    # 각각 토지 이름을 key 값으로 dictionary 생성 및 초기화 method
    for row in csvReader:
        realtyOwner[row[landNameColumn]] = ''
        realtyBuildingNum[row[landNameColumn]] = {'villa' : 0, 'building' : 0, 'hotel' : 0}  # 각각 빌라, 빌딩, 호텔 수
    f.close()

# Player 정보 관리 클래스
class Player:
    initialCash = ['4560000', '3680000', '2900000']
    playerCode = ['A', 'B', 'C', 'D']
    def __init__(self, totalNumOfPlayer, playerNum):
        self.nameCode = Player.playerCode[playerNum]   # 플레이어 이름 코드
        self.name = 'Player %s' % Player.playerCode[playerNum]  # 플레이어 이름
        self.cash = int(Player.initialCash[totalNumOfPlayer-2])  # 2~4명인데 배열은 0번부터이므로 -2
        self.realtyValue = 0  # 플레이어 소유 부동산 가치
        self.numOfBuilding = {'villa' : 0, 'building' : 0, 'hotel' : 0} # 플레이어가 가지고 있는 각 건물 수

    # 플레이어의 소유 건물 수, 해당 토지의 건물 수 증가 method
    def add_num_of_building(self, landName, buildingType, num):
        self.numOfBuilding[buildingType] += num
        RealtyInfo.realtyBuildingNum[landName][buildingType] += num
        #print(self.numOfBuilding[buildingType])
        #print(RealtyInfo.realtyBuildingNum[landName][buildingType])

    # 벌금 지급 능력 없을 시 선택 부동산 청산 method
    def remove_realty(self, realtyList):
        pass

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
        lblBarcodeInput.move(200, 550)

        # 바코드 정보 입력할 textbox
        self.edtBarcodeInfo = QtGui.QLineEdit(self)
        self.edtBarcodeInfo.setFont(QtGui.QFont('SansSerif', 30))
        self.edtBarcodeInfo.resize(300, 100)
        self.edtBarcodeInfo.move(600, 550)
        self.edtBarcodeInfo.setFocus()
        self.edtBarcodeInfo.returnPressed.connect(self.enter_pressed)

        # 플레이어 리스트 설정하기
        self.set_player_list()

        #playerList[0].add_num_of_building('cairo', 'villa', 2)

        self.show()

    # 배경 설정 method
    def set_background(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # 플레이어 리스트 설정 method
    def set_player_list(self):
        self.nowPlayerNum = 0    # 현재 플레이어가 몇 번째 플레이어인지 저장할 변수 

        # 플레이이 인원 수 구하기
        self.player_num = int(sys.argv[1])

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
        landBarcodeColumn = 1
        landNameColumn = 2
        landCodeColumn = 3
        barcodeValue = self.edtBarcodeInfo.text()

        f = open('./realty_info.csv', 'r')
        csvReader = csv.reader(f)
        for row in csvReader:
            if row[landBarcodeColumn] == barcodeValue:
                # 부가 건물이 있는 땅이면
                if row[landCodeColumn] == '1':
                    os.system('python3 buy_realty_with_building.py %s' % row[landNameColumn])   # 실행 인자 : 땅 이름
                # 부가 건물이 없는 땅이면
                elif row[landCodeColumn] == '0':
                    os.system('python3 buy_realty_without_building.py %s' % row[landNameColumn])
                break

        self.edtBarcodeInfo.setText('')
        print(buy_realty_with_building.numOfBuilding['villa'])  # 딕셔너리 key Error 발생

# window background class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.init_board()
    def init_board(self):
        self.setStyleSheet('background-image: url("../image/blue_marble.jpg")')

def run():
    app = QtGui.QApplication([])
    window = Home()
    app.exec_()

run()
