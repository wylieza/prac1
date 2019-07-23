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

#pins
GPIO.setmode(GPIO.BOARD)

led0 = 11
led1 = 13
led2 = 15
btn0 = 16
btn1 = 18

GPIO.setup(led0, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(btn0, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(btn1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#methods
def callback_method_btn0(channel):
    GPIO.output(led0, GPIO.HIGH)
    print("hello" + str(channel))

def callback_method_btn1(channel):
    GPIO.output(led0, GPIO.LOW)
    print("there")


#interrupts
#GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
GPIO.add_event_detect(btn0, GPIO.FALLING, callback=callback_method_btn0,bouncetime=300)
GPIO.add_event_detect(btn1, GPIO.FALLING, callback=callback_method_btn1,bouncetime=300)

# Logic that you write
def main():
    print("write your logic here my dude")
    #if GPIO.input(btn0) == GPIO.HIGH:
     #   GPIO.output(led0, GPIO.HIGH)

    #GPIO.output(led0,GPIO.LOW)
    time.sleep(1)



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
