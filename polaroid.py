#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP) # shutter button
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP) # shutdown button
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # verde
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # rojo
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # azul


os.system("stty -F /dev/serial0 9600")



def redLight(on):
	print("LEN ON") 
	if on:
		GPIO.output(16,GPIO.HIGH)
	else:	
	    GPIO.output(16,GPIO.LOW)
	print("LEN OFF") 

def blueLight(on):
	print("LEN ON") 
	if on:
		GPIO.output(12,GPIO.HIGH)
	else:	
	    GPIO.output(12,GPIO.LOW)
	print("LEN OFF") 
	
def greenLight(on):
	print("LEN ON") 
	if on:
		GPIO.output(24,GPIO.HIGH)
	else:	
	    GPIO.output(24,GPIO.LOW)
	print("LEN OFF") 

def printPicture(channel):
	os.system("lp -o fit-to-page test1.jpg")
	
def takePicture(channel):
	print("entro")
	os.system("libcamera-still -o test1.jpg --vflip --hflip")	
	
def pressShutterButton(channel):
	greenLight(False)
	redLight(True)
	takePicture(channel)
	redLight(False)
	blueLight(True)
	printPicture(channel)
	time.sleep(30)
	blueLight(False)
	greenLight(True)	
	time.sleep(5)
	
def pressShutdownButton(channel):	
	redLight(False)
	blueLight(False)
	greenLight(False)
	os.system("shutdown -h now")	
		
greenLight(True)

GPIO.add_event_detect(18, GPIO.FALLING, callback = pressShutterButton, bouncetime = 1000)
GPIO.add_event_detect(3, GPIO.FALLING, callback = pressShutdownButton, bouncetime = 1000)

while 1:
	time.sleep(1)
