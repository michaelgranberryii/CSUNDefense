import RPi.GPIO as GPIO
from time import sleep

pins = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

while True:
    ## Active Low LEDs
    
    ## Red
    GPIO.setup(pins[0], GPIO.LOW)
    GPIO.setup(pins[1], GPIO.HIGH)
    GPIO.setup(pins[2], GPIO.HIGH)
    sleep(1)

    ## Blue
    GPIO.setup(pins[0], GPIO.HIGH)
    GPIO.setup(pins[1], GPIO.LOW)
    GPIO.setup(pins[2], GPIO.HIGH)
    sleep(1)

    ## Green
    GPIO.setup(pins[0], GPIO.HIGH)
    GPIO.setup(pins[1], GPIO.HIGH)
    GPIO.setup(pins[2], GPIO.LOW)
    sleep(1)