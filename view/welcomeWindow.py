from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import Qt

class welcomeWindow:  # 欢迎登录界面
    def __init__(self,teacherInfoWindow):
        self.teacherInfoWindow=teacherInfoWindow
        qfile_stats = QFile("resources/ui/welcome.ui")
        self.ui = QUiLoader().load(qfile_stats)
        # self.ui.getintoButton.clicked.connect(self.getNext)
        self.ui.close()

    def getNext(self):  #到达下一个页面，即功能页面
        self.ui.hide()
        self.teacherInfoWindow.ui.show()