#!/usr/bin/python3
"""
Names: Justin Wylie
Student Number: WYLJUS002
Prac: 1
Date: <21/07/2019>
"""

#Librares
import RPi.GPIO as GPIO
import time

#SETUP

#globals
count = 0

#GPIO
#set board mode
GPIO.setmode(GPIO.BOARD)

#name pinouts
led2 = 11
led1 = 13
led0 = 15
btn0 = 16
btn1 = 18

#configure gpio pins
GPIO.setup(led0, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn0, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#methods
def callback_method_btn0(channel): #incremet counter
    global count
    if(count >= 7):
        count = 0
    else:
        count += 1


def callback_method_btn1(channel): #decrement counter
    global count
    if(count <= 0):
        count = 7
    else:
        count -= 1


#interrupts
GPIO.add_event_detect(btn0, GPIO.FALLING, callback=callback_method_btn0,bouncetime=250)
GPIO.add_event_detect(btn1, GPIO.FALLING, callback=callback_method_btn1,bouncetime=250)

#MAIN
def main():
    time.sleep(0.1)
    temp = count #Setup a tempory variable

    #Determine MSB
    if temp >= 4:
        GPIO.output(led2, GPIO.HIGH)
        temp -= 4
    else:
        GPIO.output(led2, GPIO.LOW)

    #Determine the next MSB
    if temp >= 2:
        GPIO.output(led1, GPIO.HIGH)
        temp -= 2
    else:
        GPIO.output(led1, GPIO.LOW)

    #Determine LSB
    if temp >= 1:
        GPIO.output(led0, GPIO.HIGH)
        temp -= 1
    else:
        GPIO.output(led0, GPIO.LOW)

#Check if running directly or imported
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
