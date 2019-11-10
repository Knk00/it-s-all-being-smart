
##Code for ultrasonic sensor using raspberry pi -- for object coming close to you module

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
usecho=1
vcc=21
ust=12
lr=16
ll=20
GPIO.setup(lr,GPIO.OUT)
GPIO.setup(vcc,GPIO.OUT)
GPIO.setup(ll,GPIO.OUT)
GPIO.setup(usecho,GPIO.IN)
GPIO.setup(ust,GPIO.OUT)
GPIO.output(vcc,GPIO.HIGH)
GPIO.output(lr,GPIO.LOW)
GPIO.output(ust,GPIO.LOW)

GPIO.output(ll,GPIO.LOW)
#GPIO.output(ll,GPIO.HIGH)
def ultrasound():
    #GPIO.output(usecho,GPIO.LOW)
    GPIO.output(ust,GPIO.LOW)
    time.sleep(1)
    GPIO.output(ust,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(ust,GPIO.LOW)
    while(GPIO.input(usecho)==0):
        start_time=time.time()
    while(GPIO.input(usecho)==1):
        end_time=time.time()
    total_time = end_time - start_time
    distance=round(17150*total_time,2)
    print("Distance : " ,distance, "cm")
    return distance
destus=ultrasound()
print(destus)
GPIO.output(ll,GPIO.LOW)
GPIO.output(lr,GPIO.LOW)
