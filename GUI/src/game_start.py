import sys
import os
from PyQt4 import QtGui, QtCore

class GameStart(QtGui.QMainWindow):
    def __init__(self):
        super(GameStart, self).__init__()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Game Start!')
        self.setBackground()

        self.playerNum = 2  # 플레이어 인원 기본 2명으로 초기화

        # 플레이어 선택 label 
        lblPlayerNum = QtGui.QLabel('인원을 선택해주세요', self)
        lblPlayerNum.setFont(QtGui.QFont('SansSerif', 80, QtGui.QFont.Bold))
        lblPlayerNum.resize(lblPlayerNum.sizeHint())
        lblPlayerNum.move(150, 150)

        # 플레이어 선택comboBox
        cmbPlayerNum = QtGui.QComboBox(self)
        cmbPlayerNum.setFont(QtGui.QFont('SansSerif', 70, QtGui.QFont.Bold))
        cmbPlayerNum.addItem('2명')
        cmbPlayerNum.addItem('3명')
        cmbPlayerNum.addItem('4명')
        cmbPlayerNum.resize(250, 150)
        cmbPlayerNum.move(300, 400)
        cmbPlayerNum.activated[str].connect(self.player_num_choice)

        # 플레이어 인원 결정 버튼
        btnPlayerNum = QtGui.QPushButton('OK', self)
        btnPlayerNum.setFont(QtGui.QFont('SansSerif', 70, QtGui.QFont.Bold))
        btnPlayerNum.resize(200, 150)
        btnPlayerNum.move(700, 400)
        btnPlayerNum.clicked.connect(self.player_num_decide)

        self.show()

    # background 설정 method
    def setBackground(self):
        self.theboard = Board(self)
        self.setCentralWidget(self.theboard)    # 최종 설정

    # 플레이어 인원 선택 comboBox method
    def player_num_choice(self, player_num):
        self.playerNum = player_num[0]

    # 플레이어 인원 결정 PushButton method
    def player_num_decide(self):
        # 플레이어 인원 수 인자로 넘기기
        os.system('python3 give_initial_money.py %s' % self.playerNum)    # 메인 screen인 home.py 실행
        sys.exit()


# window background class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.init_board()

    # window background 변경 method
    def init_board(self):
        self.setStyleSheet('background-image: url("../image/blue_marble.jpg")')


def run():
    app = QtGui.QApplication([])
    window = GameStart()
    app.exec_()

run()
