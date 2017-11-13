from pyfirmata import Arduino, util

board = Arduino('/dev/ttyACM0')


def SSRout(val):
    it = util.Iterator(board)
    it.start()
    board.digital[9].analogWrite(val)


