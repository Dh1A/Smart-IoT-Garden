import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)



GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def heating() :

    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)

    GPIO.output(23, GPIO.HIGH)

    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

def cooling ():

    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)

    GPIO.output(23, GPIO.LOW)

    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)

    sleep(20)

    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)

def stop() :

    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)

    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)

    GPIO.output(23, GPIO.HIGH)