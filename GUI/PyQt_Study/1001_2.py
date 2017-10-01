import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Test!")
        self.setWindowIcon(QtGui.QIcon('/usr/share/pixel-wallpaper/road.jpg'))

        # 액션object 생성 및  네임 설정
        extractAction = QtGui.QAction("&exit", self)
        # 단축키 설정
        extractAction.setShortcut("Alt+F3")
        # 마우스를 위에 올려둘 때 설명 텍스트 설정
        extractAction.setStatusTip("Leave The App")
        # 해당 액션 클릭 이벤트 설정
        extractAction.triggered.connect(self.close_application)

        # 제목 수정 액션 Object 생성
        titleAction = QtGui.QAction("&Modify Title", self)
        titleAction.setShortcut("Ctrl+A")
        titleAction.setStatusTip("Modify Current Window Title")
        titleAction.triggered.connect(self.modify_title)

        # 상태 바 추가 
        self.statusBar()

        # 메인 메뉴 object 생성
        mainMenu = self.menuBar()
        # fileMenu object 생성 및 File 메뉴 메인 메뉴에 추가
        fileMenu = mainMenu.addMenu('&File')
        # fileMenu에 extractAction, titleAction 액션 추가
        fileMenu.addAction(extractAction)
        fileMenu.addAction(titleAction)

        self.home()

    def home(self):
        # quit button
        btn  = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        #btn.resize(btn.sizeHint())
        btn.move(100, 100)

        # tool bar 생성
        extractAction = QtGui.QAction(QtGui.QIcon('/usr/share/pixel-wallpaper/road.jpg'), 'a', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        # check box
        checkBox = QtGui.QCheckBox('서울', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        # prograss bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.btn = QtGui.QPushButton('Down\nload', self)
        self.btn.resize(btn.sizeHint())
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel('Windows', self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)
        self.show()

    # check box action method
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))   #window 스타일 변경

    # progress bar action method
    def download(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    # check box action method
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    # 현재 창 닫을 시 팝업 메시지 띄우기
    def closeEvent(self, event):
        event.ignore()
        self.close_application()

    def close_application(self):
        # Pop Up Message
        choice = QtGui.QMessageBox.question(self, "Extract!", 'Get into to chopper?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Now!")
            sys.exit()
        else:
            pass

        #self.setWindowTitle("Fuck you!")

    def modify_title(self):
        self.setWindowTitle("Fuck you Man!")


def run():
    app = QtGui.QApplication([])
    GUI = Window()
    app.exec_()

run()
