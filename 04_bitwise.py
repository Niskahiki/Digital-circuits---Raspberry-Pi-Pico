from machine import Pin
import time

'''
Your task is to write a program that waits for user to press a button on the proto board.
When user presses the button, a variable is incremented by one. If the value is over seven
then variable is set to zero. By pressing the button repeatedly, you can cycle the variable
through numbers 0 – 7.
In addition to incrementing the variable that program displays the number in binary using
the proto board’s LEDs. 
'''


def set_leds_off(LEDs):
    for led in LEDs:
        led.off()

def set_leds_on(LEDs, number):
    for i in range(3):
        if number & (1 << i):
            LEDs[i].on()
        else:
            LEDs[i].off()

def main():
    sw = Pin(12, mode = Pin.IN, pull = Pin.PULL_UP)
    LEDs = [
        Pin(22, Pin.OUT),
        Pin(21, Pin.OUT),
        Pin(20, Pin.OUT)]
    decimal_number = 0
    
    set_leds_off(LEDs)
    
    while True:
        if not sw.value():
            time.sleep_ms(250)
            
            decimal_number += 1
            
            if decimal_number > 7:
                decimal_number = 0
                
            set_leds_on(LEDs, decimal_number)
    
    
if __name__ == "__main__":
    main()
    