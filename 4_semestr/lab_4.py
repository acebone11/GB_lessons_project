import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import interface


class lab4(QtWidgets.QMainWindow,interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myfunc)

    def myfunc(self):
        text ='это нужно вывести на дисплей \n'

        self.textBrowser.setText(text)
        self.textBrowser_2.setText(text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = lab4()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()