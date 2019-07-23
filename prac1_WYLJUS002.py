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

GPIO.setup(led0, GPIO.OUT)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

#interrupts
#GPIO.add_event_detect(BTN_B, GPIO.RISING, method_on_interrupt)
#GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_method(),bouncetime=300)

# Logic that you write
def main():
    print("write your logic here my dude")
    GPIO.output(led0, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led0,GPIO.LOW)
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
