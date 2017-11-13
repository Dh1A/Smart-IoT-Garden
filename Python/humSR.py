from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')

def Humsval() :

 it = util.Iterator(board)
 it.start()
 board.analog[1].enable_reporting()
 hums = board.analog[1].read()

 return (hums)