from PyQt4 import QtCore

class OtherClass(QtCore.QObject):
    valueUpdated = QtCore.pyqtSignal(int)

    def method(self):
       i = 100
        for i in range(100):
            print i
            self.valueUpdated.emit(i)
            for j in range(100500):
                pass