import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import interface


class lab4(QtWidgets.QMainWindow,interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myfunc)

    def myfunc(self):
        with open('1.txt','r') as first, open('2.txt','w') as second:
            data = first.read()
            second.write(data)

        with open('2.txt','r') as second_print:
            data2 = second_print.read()


        self.textBrowser.setText(data)
        self.textBrowser_2.setText(data2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = lab4()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()