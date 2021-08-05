from machine import Pin
import utime

shake = Pin(27, Pin.OUT)
key = Pin(28, Pin.IN, Pin.PULL_UP)
buzzer = Pin(15, Pin.OUT)


while True:
    if key.value() == 0:
        shake.value(1)
        for i in range(10):
            buzzer.value(1)
            utime.sleep(0.0001)
            buzzer.value(0)
            utime.sleep(0.0001)
        utime.sleep(.001)
    shake.value(0)
