import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Date\qt_test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_login.clicked.connect(self.btn_loginFunction)
        self.btn_join.clicked.connect(self.btn_joinFunction)

    #btn_1이 눌리면 작동할 함수
    def btn_loginFunction(self) :
        self.stackedWidget.setCurrentIndex(1)

    #btn_2가 눌리면 작동할 함수
    def btn_joinFunction(self) :
        self.stackedWidget.setCurrentIndex(1)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()