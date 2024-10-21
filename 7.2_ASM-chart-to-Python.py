from machine import Pin
import time

'''Design and implement a state machine

An alarm system has two inputs: alarm signal and a button. Alarm signal goes high when
there is an alarm. Button can be pressed to acknowledge the alarm. There are two outputs:
red light and siren.

The alarm system works so that initially both light and siren are off.
  • When alarm is activated both lamp and siren go on.
  
  • When the button is pressed the alarm acknowledged. If the alarm is still active when
    it is acknowledged the siren is switched off and the red light starts to blink. The red
    light keeps on blinking until the alarm is deactivated.
    
  • If the alarm is deactivated before button has been pressed the siren is switched off
    and red light stays on until user presses button.'''

class Alarm_System:
    def __init__(self, delay, button, alarm, red_lamp, siren):
        self.delay = delay
        self.button = Pin(button, Pin.IN, Pin.PULL_UP)
        self.alarm = Pin(alarm, Pin.IN, Pin.PULL_UP)
        self.red_lamp = Pin(red_lamp, Pin.OUT)
        self.siren = Pin(siren, Pin.OUT)
        self.state = self.off # initial state
        
    def execute(self):
        self.state()
        
    def off(self):
        self.red_lamp.off()
        self.siren.off()
        time.sleep(self.delay)
        
        if self.alarm.value() == 0:
            while self.alarm.value() == 0:
                pass
            
            self.state = self.start_alarm
    
    def start_alarm(self):
        self.red_lamp.on()
        self.siren.on()
        time.sleep(self.delay)
        
        if self.alarm.value() == 0:
            while self.alarm.value() == 0:
                pass
            
            self.state = self.alarm_switched_off
            
        elif self.button.value() == 0:
            while self.button.value() == 0:
                pass
            
            self.state = self.alarm_acknowledged
        
    def alarm_switched_off(self):
        self.red_lamp.on()
        self.siren.off()
        time.sleep(self.delay)
        
        if self.button.value() == 0:
            while self.button.value() == 0:
                pass
            
            self.state = self.off
        
    def alarm_acknowledged(self):
        self.red_lamp.off()
        self.siren.off()
        time.sleep(self.delay)
        
        self.red_lamp.on()
        time.sleep(self.delay)
        
        if self.button.value() == 0:
            while self.button.value() == 0:
                pass
            
            self.state = self.off
    
            
def main():
    asm = Alarm_System(0.050, 7, 9, 22, 20)
    
    while True:
        asm.execute()
        

if __name__ == "__main__":
    main()
        