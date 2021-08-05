import utime
from ultrasonic import ultrasonic
from dht11 import DHT11
from machine import Pin, I2C
i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)

#Initialize temperature and humidity pins
pin = Pin(22, Pin.OUT)
#Initialize the temperature and humidity library
dht11 = DHT11(pin)

#Initialize ultrasonic
Echo = Pin(13, Pin.IN)
Trig = Pin(14, Pin.OUT)
ultrasonic = ultrasonic(Trig, Echo)


while True:
    distance = ultrasonic.Distance_accurate() # Update the data detected by ultrasonic
    temperature = dht11.temperature # Update temperature value
    humdity = dht11.humidity        # Update humidity value

    #Print data
    print("distance=%dcm, temperature=%dC, humdity=%d%%"%(distance, temperature, humdity))

    #Format data into string format
    str_distance = "dis=%dcm"%(distance)
    str_temperature = "tem=%dC"%(temperature)
    str_humdity = "hum=%d%%"%(humdity)

    #oled display data
    oled.fill(0x0)
    oled.text(str_distance, 0, 0)
    oled.text(str_temperature, 0, 10)
    oled.text(str_humdity, 0, 20)
    oled.show()

    utime.sleep(.5)
