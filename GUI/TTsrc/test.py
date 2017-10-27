import Adafruit_TCS34725 as TCS
import os
import time

tcs = TCS.TCS34725()
tcs.set_interrupt(False)

while True:
    r, g, b, _ = tcs.get_raw_data()
    temp = TCS.calculate_color_temperature(r, g, b)
    print('Temp :', temp)
    time.sleep(0.1)
    os.system('clear')
