from machine import Pin, PWM, ADC
import utime

#Initialize the potentiometer pin
rp = ADC(28)

#PWM output initialization, motor pin
pwm1 = PWM(Pin(13))
pwm1.freq(1000) #Set frequency

#Numerical conversion parameters
conver_100 = 101 / (65536)

#Numerical remapping
def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


#Set speed of fan, speed=[0, 100]
def pwm_motor(speed):
    if speed > 100 or speed < 0:
        print('Please enter a limited speed value of 0-100')
        return
    pulse = my_map(speed, 0, 100, 0, 65535)
    print(pulse)
    pwm1.duty_u16(pulse)

while True:
    # Convert the read potentiometer value into [0, 100]
    val_rp = int(rp.read_u16() * conver_100)
    utime.sleep(.1)
    # print(val_rp)
    pwm_motor(val_rp)
