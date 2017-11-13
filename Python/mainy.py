import sys
from PyQt4 import QtGui
from Ui_MainWindow import Ui_MainWindow
from OtherClass import OtherClass

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myButtonSlot)
        self.otherclass = OtherClass(self)
        self.otherclass.valueUpdated.connect(self.handleValueUpdated)

    def myButtonSlot(self):
        self.otherclass.method()

    def handleValueUpdated(self, value):
        self.progressBar.setValue(value)
        QtGui.qApp.processEvents()

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()