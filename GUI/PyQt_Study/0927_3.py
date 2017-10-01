import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		# 시작 위치, width, height 설정
		self.setGeometry(50, 50, 500, 300)
		# 윈도우 제목 설정 
		self.setWindowTitle("PyQt tuts!")
		# 윈도우 아이콘 설정
		self.setWindowIcon(QtGui.QIcon('./image/python_logo.png'))
		self.home()

	def home(self):
		# 버튼 생성
		btn = QtGui.QPushButton("Quit", self)
		# 클릭 이벤트 시 현재 창 닫기 설정
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		# 버튼 크기 설정
		btn.resize(100,100)
		# 버튼 위치 설정
		btn.move(100, 100)
		self.show()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()

