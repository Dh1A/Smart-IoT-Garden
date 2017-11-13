import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import dronev1
#import RPi.GPIO as GPIO
#from lib_nrf24 import NRF24
import time





class MainG (QtGui.QMainWindow ,dronev1.Ui_MainWindow):

    def __init__(self, parent = None ):

        super(MainG,self).__init__(parent)
        self.setupUi(self)








a =QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()
