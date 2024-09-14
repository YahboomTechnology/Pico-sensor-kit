from machine import Pin, PWM
import utime
from ir import IRReceiver

# Initialize the buzzer pin to PWM function
buzzer = PWM(Pin(15))
buzzer.freq(262)
buzzer.duty_u16(0)

# The frequency of playing the middle tone 1-7
freq = [262, 294, 330, 350, 393, 441, 495]


#Configure infrared receiving pin
pin = Pin(5, Pin.IN, Pin.PULL_UP)
#Configure infrared receiving library
Ir = IRReceiver(pin)

# Infrared remote control keyboard corresponding code value
POWER = 69
MENU = 71
TEST = 68
PLUS = 64
RECALL = 67
BACKWARD = 7
PLAY = 21
FORWARD = 9
NUM_0 = 22
REDUCE = 25
CLEAR = 13
NUM_1 = 12
NUM_2 = 24
NUM_3 = 94
NUM_4 = 8
NUM_5 = 28
NUM_6 = 90
NUM_7 = 66
NUM_8 = 82
NUM_9 = 74


# Set the buzzer to emit different tones.
# index=[0-7], where 0 is off, and 1-7 represent middle C, middle D, middle E, middle F, middle G, middle A, and middle B respectively.
# time represents the function delay time (positive integer), in milliseconds.
# auto_off indicates whether the buzzer is automatically turned off after the delay time.
def tone(index, time=0, auto_off=False):
    if index == 0:
        buzzer.duty_u16(0)
        utime.sleep_ms(time)
    elif index >= 1 and index <= 7:
        tone_freq = freq[int(index - 1)]
        buzzer.freq(tone_freq)
        buzzer.duty_u16(32768)
        utime.sleep_ms(time)
        if auto_off == True:
            buzzer.duty_u16(0)
        # print("----freq:", index, tone_freq)
    else:
        print("Tones must be 0-7")


delay = 0

tone(1, 100, True)

while True:
   #Read remote control data
    value = Ir.Getir()
#     if value != None:
#         print(int(value))

# Determine whether there is a key that meets the requirements
    if value == NUM_1:
        tone(1, delay)
        print("NUM_1")
    elif value == NUM_2:
        tone(2, delay)
        print("NUM_2")
    elif value == NUM_3:
        tone(3, delay)
        print("NUM_3")
    elif value == NUM_4:
        tone(4, delay)
        print("NUM_4")
    elif value == NUM_5:
        tone(5, delay)
        print("NUM_5")
    elif value == NUM_6:
        tone(6, delay)
        print("NUM_6")
    elif value == NUM_7:
        tone(7, delay)
        print("NUM_7")
    else:
        tone(0)
