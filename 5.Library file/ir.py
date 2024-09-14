import time
from machine import Pin

class IRReceiver:
    def __init__(self, pin):
        self.Pin = pin
        self.ir_repeat_cnt = 0
        self.irdata = 0xfe

    def Getir(self):
        if self.Pin.value() == 0:
            self.ir_repeat_cnt = 0
            count = 0
            while self.Pin.value() == 0:
                count += 1
                time.sleep_us(30)  

            count = 0
            while self.Pin.value() == 1 and count < 160:
                count += 1
                time.sleep_us(30)
            print(" ")
            idx = 0
            cnt = 0
            data = [0, 0, 0, 0]
            for i in range(0, 32):
                count = 0
                while self.Pin.value() == 0 and count < 30:
                    count += 1
                    time.sleep_us(30)

                count = 0
                while self.Pin.value() == 1 and count < 80:
                    count += 1
                    time.sleep_us(30)

                if count > 35:
                    data[idx] |= 1 << cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1

            if data[0] + data[1] == 0xFF and data[2] + data[3] == 0xFF:
                self.irdata = data[2]
                print("Decoded data:", data)
        else:
            if self.ir_repeat_cnt > 110:
                self.ir_repeat_cnt = 0
                self.irdata = 0xfe
            else:
                time.sleep_us(1000)
                self.ir_repeat_cnt += 1
        if self.irdata != 254:
            result = self.irdata
            self.irdata = 254
            return result
        return None