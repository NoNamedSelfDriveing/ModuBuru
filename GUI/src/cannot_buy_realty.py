import sys
import os
from PyQt4 import QtGui, QtTest

class CannotBuyRealty(QtGui.QMainWindow):
    def __init__(self):
        super(CannotBuyRealty, self).__init__()
        self.setGeometry(150, 100, 1000, 600)
        self.setWindowTitle('Cannot Buy Realty!')

        self.lblCannotBuyTxt = QtGui.QLabel('자산이 부족하여 구매할 수 없습니다.', self)
        self.lblCannotBuyTxt.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        self.lblCannotBuyTxt.resize(self.lblCannotBuyTxt.sizeHint())
        self.lblCannotBuyTxt.move(50, 100)

        self.lblChargePrice = QtGui.QLabel(self)
        self.lblChargePrice.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        self.lblChargePrice.resize(800, 200)
        self.lblChargePrice.move(100, 200)
        self.lblChargePrice.setText('청구 금액 : ￦ 50,000')

        self.lblNowCash = QtGui.QLabel(self)
        self.lblNowCash.setFont(QtGui.QFont('SansSerif', 50, QtGui.QFont.Bold))
        self.lblNowCash.resize(800, 200)
        self.lblNowCash.move(100, 400)
        self.lblNowCash.setText('보유 금액 : ￦ 50,000')

        self.setPriceCashLabel()

        self.show()

        QtTest.QTest.qWait(3000)
        sys.exit()

    def setPriceCashLabel(self):
        chargePrice = sys.argv[1]
        nowCash = sys.argv[2]

        self.lblChargePrice.setText('청구 금액 : ￦ %s' % chargePrice)
        self.lblNowCash.setText('보유 금액 : ￦ %s' % nowCash)


def run():
    app = QtGui.QApplication([])
    window = CannotBuyRealty()
    app.exec_()

run()
