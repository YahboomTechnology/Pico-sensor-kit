from machine import Pin, ADC
import utime

# Human detection sensor pin
human = Pin(11, Pin.IN)


# Initialize the photosensitive sensor pin to GP28 (ADC function)
light = ADC(28)

red = Pin(1, Pin.OUT)
green = Pin(2, Pin.OUT)
blue = Pin(3, Pin.OUT)

led = Pin(25, Pin.OUT)

# Turn off the RGB light
def rgb_off():
    red.value(0)
    green.value(0)
    blue.value(0)

# Turn on the RGB light, white
def rgb_on():
    red.value(1)
    green.value(1)
    blue.value(1)
    
# Open on board LED
def led_on():
    led.value(1)

# Close on board LED
def led_off():
    led.value(0)

# Read the current analog value of the photosensitive sensor, range [0, 100]
# The stronger the light intensity, the smaller the value.
def get_value():
    return int(light.read_u16() * 101 / 65536)


def detect_someone():
    if human.value() == 1:
        return True
    return False


abc = 0

while True:
    val = get_value()
#     print('val=', val)

    if val >= 50:
        led_on()
        if detect_someone() == True:
            abc += 1
            rgb_on()
            print("value=", abc)
            utime.sleep(1)
        else:
            if abc != 0:
                abc = 0
                rgb_off()
    else:
        led_off()
        rgb_off()

    utime.sleep(.1)
