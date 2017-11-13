import DHT212
import os
import RPi.GPIO as gpio
import time
import datetime
import glob
import MySQLdb
from time import strftime
import urllib

def TempVal():
    temperature = probe_temp(w1tempfile)
    url = 'http://192.168.0.100/write-to-database.py?temp=' + str(temperature)
    result = urllib.urlopen(url)
    time.sleep(2)
    print
    "\nRecorded Temperature is ", (temperature)
    time.sleep(2)
    print
    "\nWriting to Database..."
    time.sleep(2)
    print
    "\nProcess Finished.\n"
    print
    "\nProcess Initialized Again.\nWaiting for Interrupt..."
    return DHT212.readDHT22temp()

