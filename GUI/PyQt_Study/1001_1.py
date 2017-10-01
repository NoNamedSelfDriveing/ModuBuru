import sys
from PyQt4 import QtGui

app = QtGui.QApplication([])
window =QtGui.QWidget()

# 시작 위치, 크기 설정 
window.setGeometry(50, 100, 500, 300)

# 제목 설정
window.setWindowTitle("Test!")
window.show()

app.exec_()
