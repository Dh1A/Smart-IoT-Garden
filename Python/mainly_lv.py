import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import lastv
from time import sleep
import RPi.GPIO as GPIO
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
import TempC
import tempR
import humR
import lumR
import humSR

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)




UserT = 0

class MainG (QtGui.QMainWindow ,lastv.Ui_MainWindow):

    def __init__(self, parent = None ):
        
        global UserT
        super(MainG,self).__init__(parent)
        self.setupUi(self)

        self.threadclass = ThreadClass()
        self.refresh = Refresh ()
        self.threadclass.start()

        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)

        self.connect(self.threadclass,QtCore.SIGNAL('Temp'),self.Updatetemp)
        self.connect(self.threadclass,QtCore.SIGNAL('Hum'), self.Updatehum )
        self.connect(self.threadclass, QtCore.SIGNAL('Lum'), self.Updatelum)
        self.connect(self.threadclass, QtCore.SIGNAL('Hums'), self.UpdatehumS)
        self.connect(self.dial_lum,QtCore.SIGNAL("valueChanged(int)"),self.SSRout)
        self.UP.clicked.connect(self.UP.run)
        self.DOWN.clicked.connect(self.DOWN.run)

        self.HumRef.clicked.connect( self.refresh.run)
        self.connect(self.dial_Temp, QtCore.SIGNAL("valueChanged(int)"), self.tempG)



    def tempG(self,temp):

        global UserT

        UserT = temp

        print (UserT)



    def Updatetemp(self,temp):

        global UserT

        self.temp_val.display(temp)
        self.ActualTemp.display(temp)
        if temp > UserT :
            TempC.cooling()
            print("cooling")
        elif temp < UserT :
            TempC.heating()
            print("heating")
        else:
            TempC.stop()
            print("stop")



    def Updatehum(self,hum):

        self.HumidityVal.display(hum)
        self.ActualHum.display(hum)


    def Updatelum(self,lum):

        self.LumVal.display(lum)
        self.ActualLum.display(lum)

    def UpdatehumS(self, humso):
        self.HumidityVal_S.display(humso)


    def Updateirrig(self,irrig):

        self.IrrigVal.display(irrig)
        self.ActualIrrig.display(irrig)









class ThreadClass(QtCore.QThread) :
    def __init__(self, parent= None):
        super(ThreadClass, self).__init__(parent)

    def run(self):

       while 1:

           temp = tempR.TempVal()
           hum = humR.HumVal()
           lum = lumR.LumVal()
           hums = humSR.Humsval()

           self.emit(QtCore.SIGNAL('Temp'), temp)
           self.emit(QtCore.SIGNAL('Hum'), hum)
           self.emit(QtCore.SIGNAL('Lum'), lum)
           self.emit(QtCore.SIGNAL('Hums'), hums)

           self.sleep(1)

class Refresh(QtCore.QThread) :
    def __init__(self, parent= None):
        super(Refresh, self).__init__(parent)

    def run (self) :
        GPIO.output(23, GPIO.LOW)
        sleep(30)
        GPIO.output(23, GPIO.HIGH)
        self.terminate ()


class UP(QtCore.QThread) :
    def __init__(self, parent= None):
        super(UP, self).__init__(parent)

    def run (self) :

        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)


class DOWN(QtCore.QThread):
    def __init__(self, parent=None):
        super(DOWN, self).__init__(parent)

    def run(self):
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)

a =QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()

