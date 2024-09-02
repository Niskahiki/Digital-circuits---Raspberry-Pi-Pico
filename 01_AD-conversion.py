from machine import Pin, ADC
import time

adc = ADC(Pin(27))
led = Pin("LED", Pin.OUT)
max_adc_value = 65535

while True:
    adc_value = adc.read_u16()
    delay = int((adc_value / max_adc_value) * 1000)
    led.on()
    time.sleep_ms(delay)
    led.off()
    time.sleep_ms(delay)