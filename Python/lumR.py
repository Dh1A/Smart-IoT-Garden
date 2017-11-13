from pyfirmata import Arduino, util
board = Arduino('/dev/ttyUSB0')

def Lumval() :
 int lum
 it = util.Iterator(board)
 it.start()
 board.analog[0].enable_reporting()
 lum = board.analog[0].read()
 it.start()
 return (lum)

