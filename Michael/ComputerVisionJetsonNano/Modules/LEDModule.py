import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
class ledRBG():
    def __init__(self,R,B,G):
        self.R = R
        self.B = B
        self.G = G
        GPIO.setup(self.R, GPIO.OUT)
        GPIO.setup(self.B, GPIO.OUT)
        GPIO.setup(self.G, GPIO.OUT)

    def color(self, myColor):
    ## Active Low LEDs
        if myColor == 'red':    
            ## Red
            GPIO.setup(self.R, GPIO.LOW)
            GPIO.setup(self.B, GPIO.HIGH)
            GPIO.setup(self.G, GPIO.HIGH)
        elif myColor == 'blue':    
            ## Blue
            GPIO.setup(self.R, GPIO.HIGH)
            GPIO.setup(self.B, GPIO.LOW)
            GPIO.setup(self.G, GPIO.HIGH)
        elif myColor == 'green':    
            ## Green
            GPIO.setup(self.R, GPIO.HIGH)
            GPIO.setup(self.B, GPIO.HIGH)
            GPIO.setup(self.G, GPIO.LOW)
        elif myColor == 'off':    
            ## OFF
            GPIO.setup(self.R, GPIO.HIGH)
            GPIO.setup(self.B, GPIO.HIGH)
            GPIO.setup(self.G, GPIO.HIGH)
        elif myColor == 'white':    
            ## White
            GPIO.setup(self.R, GPIO.LOW)
            GPIO.setup(self.B, GPIO.LOW)
            GPIO.setup(self.G, GPIO.LOW)


def main():
    myLED = ledRBG(17, 27, 22)
    while True:
        myLED.color('red')
        sleep(1)
        myLED.color('green')
        sleep(1)
        myLED.color('off')
        sleep(1)
        
if __name__ == "__main__":
    main()