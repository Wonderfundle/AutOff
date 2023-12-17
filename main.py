import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Button
butonOrta=Button(10)
GPIO.setwarnings(False)
#GPIO modu seçme
GPIO.setmode(GPIO.BCM)
#GPIO pinlerinin yerini belirleme
redPin = 12
greenPin = 19
bluePin = 13
buzzer=23
pin=17
#Çıkış için pin seçme
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

def turnOff():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def white():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def red():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def green():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def blue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def yellow():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def purple():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
    
def lightBlue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
def eglence():
    turnOff()
    sleep(1) #1second
    white()
    sleep(1)
    red()
    sleep(1)
    green()
    sleep(1)
    blue()
    sleep(1)
    yellow()
    sleep(1)
    blue()
    sleep(1)
    purple()
    sleep(1)
    green()
    sleep(1)
    lightBlue()
    sleep(1)
    purple()
    sleep(1)
    turnOff()

while True:
    if butonOrta.is_pressed:
        print("bzz")
        GPIO.output(buzzer,GPIO.HIGH)
        sleep(0.3)
        GPIO.output(buzzer,GPIO.LOW)
        eglence()
        GPIO.output(pin,GPIO.HIGH)
        sleep(10)
        GPIO.output(pin,GPIO.LOW)
    '''
x=input("?:")
if x=="a":
	print("bzz")
	GPIO.output(buzzer,GPIO.HIGH)
	sleep(0.3)
	GPIO.output(buzzer,GPIO.LOW)
	eglence()
	GPIO.output(pin,GPIO.HIGH)
	sleep(15)
	GPIO.output(pin,GPIO.LOW) 
elif x=="s":
	print("bzz2")
	GPIO.output(buzzer,GPIO.HIGH)
	sleep(0.3)
	GPIO.output(buzzer,GPIO.LOW)
	eglence()
	GPIO.output(pin,GPIO.HIGH)
	sleep(45)
	GPIO.output(pin,GPIO.LOW) 
elif x=="d":
	print("bzz3")drd
	GPIO.output(buzzer,GPIO.HIGH)
	sleep(0.3)
	GPIO.output(buzzer,GPIO.LOW)
	eglence()
	GPIO.output(pin,GPIO.HIGH)
	sleep(60)
	GPIO.output(pin,GPIO.LOW)
'''
