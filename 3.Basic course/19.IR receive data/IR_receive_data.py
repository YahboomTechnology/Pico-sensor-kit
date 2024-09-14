from machine import Pin
import time
from ir import IRReceiver

pin = Pin(5, Pin.IN, Pin.PULL_UP)
ir_receiver = IRReceiver(pin)

while True:
    value = ir_receiver.Getir()
    if value is not None:
        print(f"Received value: {value}")
        time.sleep(0.1)

