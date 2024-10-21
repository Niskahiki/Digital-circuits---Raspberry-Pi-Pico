from machine import Pin
import time

'''Implement an ASM chart in Python

The state machine controls lights with a push button. When the button is pressed the light
switches on immediately. The button has to be released before lamp can be switched off.
Then when the button is pressed again the light switches off. The following ASM-chart
specifies the state machine operation. Implement the state machine in MicroPython. Use
SW2 (Pin id: 7) for button and LED3 (Pin id: 20) for lamp. Clock frequency of the state
machine is 20 Hz (50 ms period)'''

class Light:
    def __init__(self, delay, button, led):
        self.delay = delay
        self.button = Pin(button, Pin.IN, Pin.PULL_UP)
        self.led = Pin(led, Pin.OUT)
        self.state = self.off # initial state
        
    def execute(self):
        self.state()
        
    def off(self):
        self.led.off()
        time.sleep(self.delay)
        
        if self.button():
            while self.button():
                pass
                
            self.state = self.on
            
    def on(self):
        self.led.on()
        time.sleep(self.delay)
        
        if self.button():
            while self.button():
                pass
                
            self.state = self.off
                    
                    
def main():
    asm = Light(0.050, 7, 20)
    
    while True:
        asm.execute()
    
 
if __name__ == "__main__":
    main()
    