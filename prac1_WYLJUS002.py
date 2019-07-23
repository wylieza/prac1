#!/usr/bin/python3
"""
Names: Justin Wylie
Student Number: WYLJUS002
Prac: 1
Date: <21/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time

#SETUP

#globals
count = 0

#pins
GPIO.setmode(GPIO.BOARD)

led2 = 11
led1 = 13
led0 = 15
btn0 = 16
btn1 = 18

GPIO.setup(led0, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn0, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#methods
def callback_method_btn0(channel): #incremet
    global count
    if(count >= 7):
        count = 0
    else:
        count += 1


def callback_method_btn1(channel): #decrement
    global count
    if(count <= 0):
        count = 7
    else:
        count -= 1


#interrupts
#GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
GPIO.add_event_detect(btn0, GPIO.FALLING, callback=callback_method_btn0,bouncetime=250)
GPIO.add_event_detect(btn1, GPIO.FALLING, callback=callback_method_btn1,bouncetime=250)

# Logic that you write
def main():
    print("Display Update")
    temp = count

    if temp >= 4:
        GPIO.output(led2, GPIO.HIGH)
        temp -= 4
    else:
        GPIO.output(led2, GPIO.LOW)

    if temp >= 2:
        GPIO.output(led1, GPIO.HIGH)
        temp -= 2
    else:
        GPIO.output(led1, GPIO.LOW)

    if temp >= 1:
        GPIO.output(led0, GPIO.HIGH)
        temp -= 1
    else:
        GPIO.output(led0, GPIO.LOW)




# Only run the functions if 
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
