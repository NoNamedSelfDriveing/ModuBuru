import sys
from PyQt4 import QtGui 

app = QtGui.QApplication([])
window = QtGui.QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle("PyQt Tuts!")

window.show()
app.exec_()

