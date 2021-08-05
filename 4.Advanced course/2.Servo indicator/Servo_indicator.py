import utime
import ws2812b
import random
from machine import Pin


ring_pin = 17 # RGB halo pin
numpix   = 8  # Number of RGB lights
strip = ws2812b.ws2812b(numpix, 0, ring_pin)

# Close all lights
strip.fill(0,0,0)
strip.show()

rp = machine.ADC(28)

conver_180 = 181 / (65535)
servo = machine.PWM(machine.Pin(7))
servo.freq(50)

def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def servo_control(value):
    duty = my_map(value, 0, 180, 500000, 2500000)
#     print(duty)
    servo.duty_ns(duty)

utime.sleep(.1)

while True:
    # Convert the read potentiometer value into [0, 180]
    val_rp = int(rp.read_u16() * conver_180)
    utime.sleep(.01)
    print(val_rp)
    servo_control(val_rp)
    if val_rp < 180/3:
        strip.fill(val_rp, 0, 0)
    elif val_rp < 180/3*2:
        strip.fill(0, val_rp, 0)
    else:
        strip.fill(0, 0, val_rp)
    strip.show()
