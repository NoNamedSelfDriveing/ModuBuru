import sys
from PyQt4.QtGui import *

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		# 시작 위치, width, height 설정
		self.setGeometry(50, 50, 500, 300)
		# 윈도우 제목 설정 
		self.setWindowTitle("PyQt tuts!")
		# 윈도우 아이콘 설정
		self.setWindowIcon(QIcon('./image/python_logo.png'))
		self.show()

app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())

