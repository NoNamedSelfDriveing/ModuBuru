import sys
import csv

import Communicate_AVR as ComAVR
from PyQt4 import QtGui

class PayMoney(QtGui.QMainWindow):
    def __init__(self):
        super(PayMoney, self).__init__()
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Pay Money')
        self.set_background()

        self.cavr = ComAVR.ComAVR()

        # '넣은 돈' 텍스트 표시 Label
        lblInsertedMoneyTxt = QtGui.QLabel('넣은 돈', self)
        lblInsertedMoneyTxt.setFont(QtGui.QFont('SansSerif', 60, QtGui.QFont.Bold))
        lblInsertedMoneyTxt.resize(lblInsertedMoneyTxt.sizeHint())
        lblInsertedMoneyTxt.move(250, 20)

        # 넣은 금액 표시할 Label
        self.lblInsertedMoney = QtGui.QLabel(self)
        self.lblInsertedMoney.setText('￦ 0')
        self.lblInsertedMoney.setFont(QtGui.QFont('SansSerif', 60))
        self.lblInsertedMoney.resize(600, 100)
        self.lblInsertedMoney.move(200, 170)

        # '남은 금액' 텍스트 표시 Label
        lblRemainMoneyTxt = QtGui.QLabel('남은 금액', self)
        lblRemainMoneyTxt.setFont(QtGui.QFont('SansSerif', 60, QtGui.QFont.Bold))
        lblRemainMoneyTxt.resize(lblRemainMoneyTxt.sizeHint())
        lblRemainMoneyTxt.move(230, 300)

        # 남은 금액 표시 Label
        self.lblRemainMoney = QtGui.QLabel(self)
        self.lblRemainMoney.setFont(QtGui.QFont('SansSerif', 60))
        self.lblRemainMoney.resize(700, 100)
        self.lblRemainMoney.move(200, 450)

        self.show_initial_remain_money()

        self.show()

    # 배경 설정 기능 호출 method
    def set_background(self):
        self.background = BackGround(self)
        self.setCentralWidget(self.background)

    # 초기 잔여 금액 표시 method
    def show_initial_remain_money(self):
        '''landNameColumn = 2
        landPriceColumn = 5
        f = open('./realty_info.csv', 'r')
        csvReader = csv.reader(f)
        for col in csvReader:
            if col[landNameColumn] == sys.argv[1]:
                self.lblRemainMoney.setText('￦ %s' %col[landPriceColumn])
                break
        '''
        self.lblRemainMoney.setText('￦ %s' % sys.argv[1])

    

# 배경 설정 class
class BackGround(QtGui.QFrame):
    def __init__(self, parent):
        super(BackGround, self).__init__(parent)
        self.init_background()

    def init_background(self):
        self.setStyleSheet('background-image: url("../image/green.png")')

def run():
    app = QtGui.QApplication([])
    window = PayMoney()
    app.exec_()

run()

cavr = ComAVR.ComAVR()
cavr.get_banknote(100000)
#sys.exit()
