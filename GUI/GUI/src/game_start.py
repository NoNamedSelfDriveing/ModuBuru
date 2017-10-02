import sys
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
        lblPlayerNum.setFont(QtGui.QFont('SansSerif', 40, QtGui.QFont.Bold))
        lblPlayerNum.resize(lblPlayerNum.sizeHint())
        lblPlayerNum.move(400, 220)

        # 플레이어 선택checkBox

        cmbPlayerNum = QtGui.QComboBox(self)
        cmbPlayerNum.addItem('2명')
        cmbPlayerNum.addItem('3명')
        cmbPlayerNum.addItem('4명')
        cmbPlayerNum.resize(200, 80)
        cmbPlayerNum.move(430, 400)
        cmbPlayerNum.activated[str].connect(self.player_num_choice)

        # 플레이어 인원 결정 버튼
        btnPlayerNum = QtGui.QPushButton('OK', self)
        btnPlayerNum.clicked.connect(self.player_num_decide)
        btnPlayerNum.resize(100, 80)
        btnPlayerNum.move(700, 400)

        self.show()

    # background 설정 method
    def setBackground(self):
        self.theboard = Board(self)
        self.setCentralWidget(self.theboard)    # 최종 설정

    # 플레이어 인원 선택 comboBox method
    def player_num_choice(self, player_num):
        self.playerNum = int(player_num[0])
        #print(self.playerNum)

    # 플레이어 인원 결정 PushButton method
    def player_num_decide(self):
        #print(self.playerNum)
        f = open('information.txt', 'w')
        f.write('player_num=%d\n' % self.playerNum)
        f.close()
        sys.exit()


# window background class
class Board(QtGui.QFrame):
    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.initBoard()

    # window background 변경 method
    def initBoard(self):
        self.setStyleSheet('background-image: url("../image/game_start_bg.jpg")')


def run():
    app = QtGui.QApplication([])
    GUI = GameStart()
    app.exec_()

run()
