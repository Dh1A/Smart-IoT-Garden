import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)


GPIO.output(14, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
sleep(2)
GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
sleep(2)
GPIO.output(18, GPIO.HIGH)
sleep(2)
GPIO.output(18, GPIO.LOW)
sleep(2)
GPIO.output(23, GPIO.HIGH)
sleep(2)
GPIO.output(23, GPIO.LOW)
sleep(2)
GPIO.output(24, GPIO.HIGH)
GPIO.output(25, GPIO.LOW)
sleep(2)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.HIGH)
sleep(2)