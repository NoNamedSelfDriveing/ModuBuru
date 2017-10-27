import sys
import os
import csv
import pickle
from PyQt4 import QtGui, QtCore
from functools import partial

class BuyRealtyWithBuilding(QtGui.QMainWindow):
    boldFont = QtGui.QFont('SansSerif', 80, QtGui.QFont.Bold)
    noBoldFont = QtGui.QFont('SansSerif', 20)

    def __init__(self):
        super(BuyRealtyWithBuilding, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Buy Realty With Building')
        self.setBackground()

        # '건물을 선택하세요' 텍스트 띄울 Label
        lblSelect = QtGui.QLabel('건물을 선택하세요', self)
        lblSelect.setFont(QtGui.QFont('SansSerif', 50))
        lblSelect.resize(lblSelect.sizeHint())
        lblSelect.move(160, 30)

        # '땅' 선택 checkBox
        self.chkLand = QtGui.QCheckBox('땅', self)
        self.chkLand.stateChanged.connect(partial(self.show_selected, self.chkLand.text()))
        self.chkLand.setFont(BuyRealtyWithBuilding.boldFont)
        self.chkLand.resize(400, 150)
        self.chkLand.move(320, 150)

        # '별장 1' 선택 CheckBox
        self.chkVilla1 = QtGui.QCheckBox('별장 1', self)
        self.chkVilla1.stateChanged.connect(partial(self.show_selected, self.chkVilla1.text()))
        self.chkVilla1.setFont(BuyRealtyWithBuilding.boldFont)
        self.chkVilla1.resize(400, 150)
        self.chkVilla1.move(50, 320)

        # '별장 2' 선택 CheckBox
        self.chkVilla2 = QtGui.QCheckBox('별장 2', self)
        self.chkVilla2.stateChanged.connect(partial(self.show_selected, self.chkVilla2.text()))
        self.chkVilla2.setFont(BuyRealtyWithBuilding.boldFont)
        self.chkVilla2.resize(400, 150)
        self.chkVilla2.move(50, 530)

        # '빌딩' 선택 CheckBox
        self.chkBuilding = QtGui.QCheckBox('빌딩', self)
        self.chkBuilding.stateChanged.connect(partial(self.show_selected, self.chkBuilding.text()))
        self.chkBuilding.setFont(BuyRealtyWithBuilding.boldFont)
        self.chkBuilding.resize(400, 150)
        self.chkBuilding.move(500, 320)

        # '호텔' 선택 CheckBox
        self.chkHotel = QtGui.QCheckBox('호텔', self)
        self.chkHotel.stateChanged.connect(partial(self.show_selected, self.chkHotel.text()))
        self.chkHotel.setFont(BuyRealtyWithBuilding.boldFont)
        self.chkHotel.resize(400, 150)
        self.chkHotel.move(500, 530)

        # '선택한 건물' 텍스트 띄울 Label
        lblSelectedTxt = QtGui.QLabel('선택한 건물', self)
        lblSelectedTxt.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        lblSelectedTxt.resize(lblSelectedTxt.sizeHint())
        lblSelectedTxt.move(840, 20)

        # 선택한 건물 표시할 Label
        self.lblSelected = QtGui.QLabel(self)
        self.lblSelected.setFont(QtGui.QFont('SansSerif', 30))
        self.lblSelected.resize(200, 80)
        self.lblSelected.move(930, 140)

        # '금액' 텍스트 띄울 Label
        lblPriceTxt = QtGui.QLabel('금액', self)
        lblPriceTxt.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        lblPriceTxt.resize(lblPriceTxt.sizeHint())
        lblPriceTxt.move(950, 270)

        # 선택한 건물 금액 표시할 Label
        self.lblPrice = QtGui.QLabel('￦ 0', self)
        self.lblPrice.setFont(QtGui.QFont('SansSerif', 30))
        self.lblPrice.resize(300, 80)
        self.lblPrice.move(900, 380)
        #self.lblPrice.setText('W 0000')

        # 구매 완료할 PushButton
        btnOK = QtGui.QPushButton('완료', self)
        btnOK.clicked.connect(self.pay_money)
        btnOK.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        btnOK.resize(200, 200)
        btnOK.move(920, 470)

        self.checkbox_enable_initial_set();    # 초기 체크박스 enable/disable 설정
        self.get_each_building_price();  # 본 토지의 건물별 가격 구하기
        self.show()

    # 배경 설정 method
    def setBackground(self):
        self.theBoard = Board(self)
        self.setCentralWidget(self.theBoard)

    # 일부 checkbox만 enable 세팅하기(땅을 안샀다면 빌딩, 호텔은 disable 시켜야 함)
    def checkbox_enable_initial_set(self):
        # 현재 토지에 세워진 건물 개수 가져오기
        f = open('selected_num_of_building.dat', 'rb')
        self.landNowBuildingNum = pickle.load(f)
        f.close()

        # 땅 유무에 따른 처리
        if self.landNowBuildingNum.get('land') == 0:
            self.chkVilla1.setEnabled(False)
            self.chkVilla2.setEnabled(False)
            self.chkBuilding.setEnabled(False)
            self.chkHotel.setEnabled(False)

        elif self.landNowBuildingNum.get('land') == 1:
            self.chkLand.setEnabled(False)

        # 별장 개수에 따른 처리
        if self.landNowBuildingNum.get('villa') == 0:
            self.chkBuilding.setEnabled(False)
            self.chkHotel.setEnabled(False)

        elif self.landNowBuildingNum.get('villa') == 1:
            self.chkVilla2.setEnabled(False)
            self.chkBuilding.setEnabled(False)
            self.chkHotel.setEnabled(False)

        elif self.landNowBuildingNum.get('villa') == 2:
            self.chkVilla1.setEnabled(False)
            self.chkVilla2.setEnabled(False)

        # 빌딩 유무에 따른 처리
        if self.landNowBuildingNum.get('building') == 1:
            self.chkBuilding.setEnabled(False)

        elif self.landNowBuildingNum.get('building') == 0:
            self.chkHotel.setEnabled(False)

        # 호텔 유무에 따른 처리
        if self.landNowBuildingNum.get('hotel') == 1:
            self.chkHotel.setEnabled(False)

    # 본 토지의 건물별 가격 가져오기
    def get_each_building_price(self):
        landNameColumn = 2
        checkBoxList = [self.chkLand, self.chkVilla1, self.chkVilla2, self.chkBuilding, self.chkHotel]
        # 건물 가격 적힌 column 값
        priceColumn = {self.chkLand.text() : 5, self.chkVilla1.text() : 6, self.chkVilla2.text() : 7, self.chkBuilding.text() : 8, self.chkHotel.text() : 9}
        # 본 토지의 건물 가격 저장 dictionary
        self.buildingPrice = {self.chkLand.text() : '', self.chkVilla1.text() : '', self.chkVilla2.text() : '', self.chkBuilding.text() : '', self.chkHotel.text() : ''}

        # 건물별 가격 저장
        f = open('./realty_info.csv', 'r')
        csvReader = csv.reader(f)
        for row in csvReader:
            if row[landNameColumn] == sys.argv[1]:
                # 건물별 가격 저장
                for targetCheckBox in checkBoxList:
                    self.buildingPrice[targetCheckBox.text()] = row[priceColumn[targetCheckBox.text()]]
        f.close()

    # 선택한 건물 표시 method
    def show_selected(self, text, state):
        # 체크된 건물 확인 후 건물 이름 표시 및 가격 표시
        if state == QtCore.Qt.Checked:
            self.lblSelected.setText(text)
            #for checkBox in checkBoxList:
                # 해당 토지의 건물 가격 표시
            #    if checkBox.text() == text:
            self.lblPrice.setText('￦ %s' % self.buildingPrice[text])

                # 해당 사항 없는 체크박스 disabled
                #else:
            # 만약 땅 선택 되어 있을 시 별장1, 별장2 enable
            if self.chkLand.isChecked():
                self.chkVilla1.setEnabled(True)
                self.chkVilla2.setEnabled(True)
            # 만약 '별장 1' 선택 되어있을 시 '별장 2' disable
            if self.chkVilla1.isChecked():
                self.chkVilla2.setEnabled(False)
                # '땅' 선택되어 있을 시 가격 첨가, 텍스트 첨가(땅 + 별장 1)
                if self.chkLand.isChecked():
                    self.lblSelected.setText(self.chkLand.text() + ',  ' + self.chkVilla1.text())
                    self.lblPrice.setText('￦ %s' % str(int(self.buildingPrice.get(self.chkLand.text())) + int(self.buildingPrice.get(self.chkVilla1.text()))))
            # 만약 '별장 2' 선택 되어있을 시 '별장 1' disable
            if self.chkVilla2.isChecked():
                self.chkVilla1.setEnabled(False)
                # '땅' 선택되어 있을 시 가격 첨가, 텍스트 첨가(땅 + 별장 2)
                if self.chkLand.isChecked():
                    self.lblSelected.setText(self.chkLand.text() + ', ' + self.chkVilla2.text())
                    self.lblPrice.setText('￦ %s' % str(int(self.buildingPrice.get(self.chkLand.text())) + int(self.buildingPrice.get(self.chkVilla2.text()))))

        # 체크 박스 체크 해제 시
        else:
            self.lblSelected.setText('')
            self.lblPrice.setText('')

            # 땅 체크 해제하면 별장1, 별장 2 disable 
            if text == self.chkLand.text():
                self.chkVilla1.setEnabled(False)
                self.chkVilla2.setEnabled(False)

            # '별장 1' 체크 해제하면 '별장 2' enable
            if text == self.chkVilla1.text():
                self.chkVilla2.setEnabled(True)
                # 만약 '땅' 체크되어 있을 시 선택한 건물에 '땅' 표시
                if self.chkLand.isChecked():
                    self.lblSelected.setText(self.chkLand.text())
                    self.lblPrice.setText('￦ %s' % self.buildingPrice.get(self.chkLand.text()))
                # 이미 별장 1개만 구매했다면 별장 2 disable하기
                if self.landNowBuildingNum.get('villa') == 1:
                    self.chkVilla2.setEnabled(False)

            # '별장 2' 체크 해제하면 '별장 1' enable
            if text == self.chkVilla2.text():
                self.chkVilla1.setEnabled(True)
                # 만약 '땅' 체크되어 있을 시 선택한 건물에 '땅' 표시
                if self.chkLand.isChecked():
                    self.lblSelected.setText(self.chkLand.text())
                    self.lblPrice.setText('￦ %s' % self.buildingPrice.get(self.chkLand.text()))

    # 구매 버튼(OK) 버튼 클릭 이벤트 method
    def pay_money(self):
        nowCash = int(sys.argv[2])
        checkBoxList = [self.chkLand, self.chkVilla1, self.chkVilla2, self.chkBuilding, self.chkHotel]
        selectedNumOfBuilding = {'land' : 0, 'villa' : 0, 'building' : 0, 'hotel' : 0}
        totalPrice = self.lblPrice.text()[2:]
        buyFlag = 0

        if nowCash < int(totalPrice):
            os.system('python3 cannot_buy_realty.py %s %s' % (totalPrice, str(nowCash)))
            return

        # 토지 및 건물 구매했는지 안했는지 flag 설정하기
        for buildingType in list(selectedNumOfBuilding.keys()):
            if selectedNumOfBuilding[buildingType] != 0:
                buyFlag = 1

        # 선택 건물 개수 저장
        for checkBox in checkBoxList:
            if checkBox.isChecked():
                if checkBox.text() == '땅':
                    selectedNumOfBuilding['land'] = 1
                elif checkBox.text() == '별장 1':
                    selectedNumOfBuilding['villa'] = 1
                elif checkBox.text() == '별장 2':
                    selectedNumOfBuilding['villa'] = 2
                elif checkBox.text() == '빌딩':
                    selectedNumOfBuilding['building'] = 1
                elif checkBox.text() == '호텔':
                    selectedNumOfBuilding['hotel'] = 1

        # 토지 및 건물 구매했는지 안했는지 flag 설정하기
        for buildingType in list(selectedNumOfBuilding.keys()):
            if selectedNumOfBuilding[buildingType] != 0:
                buyFlag = 1

        f = open('selected_num_of_building.dat', 'wb')
        pickle.dump(selectedNumOfBuilding, f)
        pickle.dump(buyFlag, f)
        pickle.dump(totalPrice, f)
        f.close()

        # 선택한 건물 금액 인자로 pay_money.py(돈 납부하는 기능) 실행
        if buyFlag == 1:
            os.system('python3 pay_money.py %s' % totalPrice)     # '￦ '를 제외한 뒷 금액을  인자로
            sys.exit()

        # 아무것도 선택 안한 경우 그냥 close
        else:
            sys.exit()

# 배경 설정 Class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()
    def initBoard(self):
        self.setStyleSheet('background-image: url("../image/%s.png")' % sys.argv[1])

def run():
    app = QtGui.QApplication([])
    window = BuyRealtyWithBuilding()
    app.exec_()

if __name__ == "__main__":
    run()
