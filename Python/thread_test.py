import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import lastv
from time import sleep

UserT = 0


class MainG (QtGui.QMainWindow ,lastv.Ui_MainWindow):

    def __init__(self, parent = None ):
        super(MainG,self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()



        self.connect(self.threadclass, QtCore.SIGNAL('Temp'), self.Updatetemp)
        self.connect(self.threadclass, QtCore.SIGNAL('Hum'), self.Updatehum)
        self.connect(self.threadclass, QtCore.SIGNAL('Lum'), self.Updatelum)
        self.connect(self.threadclass, QtCore.SIGNAL('Hums'), self.UpdatehumS)
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
            print("cooling")
        elif temp < UserT :
            print("heating")
        else:
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
        temp = 10

        while 1:


            hum = 10
            lum = 10
            hums = 10

            self.emit(QtCore.SIGNAL('Temp'), temp)
            self.emit(QtCore.SIGNAL('Hum'), hum)
            self.emit(QtCore.SIGNAL('Lum'), lum)
            self.emit(QtCore.SIGNAL('Hums'), hums)
            temp += 1

            self.sleep(1)













































a =QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()