import sys
import os
import time
from PyQt4 import QtGui, QtTest

class GiveInitialMoney(QtGui.QMainWindow):
    def __init__(self):
        super(GiveInitialMoney, self).__init__()
        self.setGeometry(240, 150, 800, 500)
        self.setWindowTitle('Give Initial Money')
        self.set_background()

        # 텍스트 표시 메인 Label
        self.lblMain = QtGui.QLabel(self)
        self.lblMain.setFont(QtGui.QFont('SansSerif', 33))
        self.lblMain.resize(750, 100)
        self.lblMain.move(50, 100)

        # '인출 시작' PushButton
        self.btnStart = QtGui.QPushButton('인출\n시작', self)
        self.btnStart.clicked.connect(self.give_money)
        self.btnStart.setFont(QtGui.QFont('SansSerif', 50))
        self.btnStart.resize(200, 200)
        self.btnStart.move(450, 250)

        self.show()

    # 배경 화면 설정 method
    def set_background(self):
        pass
        #self.background = Background(self)
        #self.setCentralWidget(self.background)

    # 인출 시작 PushButton 클릭 이벤트 method, 돈 출력 시작
    def give_money(self):
        playerNum = int(sys.argv[1])
        playerOrder = {'1' : '첫', '2' : '두','3' : '세', '4' : '네'}
        initialCashList = ['4560000', '3680000', '2900000'] # 플레이어 수에 따른 초기 현금 지급액 리스트(각각 2명, 3명, 4명)
        personalInitialCash = initialCashList[playerNum-2]    # 개인에게 지급되는 현금 (2~4명이므로 index는 0~2)

        # 루틴 돌며 각각 플레이어 현급 출력
        for i in range(1, int(playerNum)+1):
            self.lblMain.setText('%s 번째 플레이어 현금 인출 중...' % playerOrder.get(str(i)))

            '''
                하드웨어 측에서 인출 작업 수행
            '''

            QtTest.QTest.qWait(2000)    # 2sec 대기

        self.lblMain.setText('인출이 완료되었습니다.')
        QtTest.QTest.qWait(2000)

        # home.py 실행, 플레이어 수 인자로 넘기기
        os.system('python3 home.py %s' % str(playerNum))
        sys.exit()

# 배경 화면 설정 클래스
class Background(QtGui.QFrame):
    def __init__(self, parent):
        super(Background, self).__init__(parent)
        self.init_background()

    def init_background(self):
        self.setStyleSheet('background-image: url("../image/.png")')

def run():
    app = QtGui.QApplication([])
    window = GiveInitialMoney()
    app.exec_()

run()
