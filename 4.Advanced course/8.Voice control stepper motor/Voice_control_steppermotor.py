from machine import Pin
import utime
import _thread

# Onboard LED light initialization
led = Pin(25, Pin.OUT)

# Sound sensor module pin initialization
sound = Pin(10, Pin.IN)

# Pin initialization
in1 = Pin(16, Pin.OUT)
in2 = Pin(15, Pin.OUT)
in3 = Pin(14, Pin.OUT)
in4 = Pin(13, Pin.OUT)

# Relay pin initialization
relay = Pin(4, Pin.OUT)

delay = 1

# The number of revolutions required for a lap
ROUND_VALUE = 509

# The sequence value of a four-phase eight-beat stepper motor.
STEP_VALUE = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]

# Open on board LED
def led_on():
    led.value(1)

# Close on board LED
def led_off():
    led.value(0)

# Read the state of the sound module, return True if the sound exceeds the threshold, and return False if it does not exceed the threshold
def sound_state():
    if sound.value() == 0:
        return True
    return False

# Pin output low level
def reset():
    in1(0)
    in2(0)
    in3(0)
    in4(0)

def step_run(count):
    direction = -1     # Clockwise
    if count < 0:
        direction = 1  # Counterclockwise
        count = -count
    for x in range(count):
        for bit in STEP_VALUE[::direction]:
            in1(bit[0])
            in2(bit[1])
            in3(bit[2])
            in4(bit[3])
            utime.sleep_ms(delay)
    reset()

#If a positive integer is clockwise, negative integer is counterclockwise
def step_angle(a):
    step_run(int(ROUND_VALUE * a / 360))

# The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.
def relay_on():
    relay(1)

# The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.
def relay_off():
    relay(0)

# Run stepper motor
def task_1():
    while True:
        step_run(1)
        


def main():
    _thread.start_new_thread(task_1, ())
    time_point = utime.ticks_ms()

    motor_state = False
    # Loop, detect sound module
    while True:
        if sound_state() == True:
            # Sound filtering for 300 milliseconds to avoid repeated detection
            if utime.ticks_ms() - time_point >= 300:
                print("get sound")
                time_point = utime.ticks_ms()
                motor_state = not motor_state

        if motor_state:
            # Open the relay switch
            relay_on()
            led_on()
        else:
            # Close the relay switch
            relay_off()
            led_off()

try:
    main()
except KeyboardInterrupt:
    _thread.exit()
