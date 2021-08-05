import ws2812b
import utime
from machine import Pin, I2C
from color import color

# i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)
i2c=I2C(1, scl=Pin(19),sda=Pin(18), freq=100000)

# Initialize the color recognition sensor
Color = color(i2c)

ring_pin = 17 
numpix   = 8  
strip = ws2812b.ws2812b(numpix, 0, ring_pin)


strip.fill(0,0,0)
strip.show()

utime.sleep(.1)

while True:
    Colors = Color.GetColor() #Get the data of the color recognition sensor
    r = Colors[0]
    g = Colors[1]
    b = Colors[2]
    strip.fill(r, g, b)       #Set color
    strip.show()
    utime.sleep(0.2)
