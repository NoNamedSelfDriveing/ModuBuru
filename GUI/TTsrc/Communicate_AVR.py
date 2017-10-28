import serial
import time
import os
import Adafruit_TCS34725 as TCS

class ComAVR:
    def __init__(self):
        self.srl = serial.Serial('/dev/ttyUSB0')
        self.srl.baudrate = 19200

    # Rotate banknote pane
    def move_banknote_pane(self, bntype):
        self.srl.write(b'A')
        if bntype == 6:
            self.srl.write(b'6')
        elif bntype == 5:
            self.srl.wrtte(b'5')
        elif bntype == 4:
            self.srl.write(b'4')
        elif bntype == 3:
            self.srl.write(b'3')
        elif bntype == 2:
            self.srl.write(b'2')
        elif bntype == 1:
            self.srl.write(b'1')

        while(chr(ord(self.srl.read(1))) != 'F'):
            pass

    # Get banknotes from player
    def get_banknote(self, money):
        srl.write(b'M')
        srl.write(b'I')
        while(chr(ord(srl.read(1))) != 'F'):
            pass
        # Return Cash
        print(cash)
        self.give_change(-cash)

    # Give money to player
    def give_banknote(self, money):
        cash = money

        while cash > 0:
            if cash / 500000 > 0:
                self.srl.write(b'MO6')
                cash -= 500000
            elif cash / 100000 > 0:
                self.srl.write(b'MO5')
                cash -= 100000
            elif cash / 50000 > 0:
                self.srl.write(b'MO4')
                cash -= 50000
            elif cash / 20000 > 0:
                self.srl.write(b'MO3')
                cash -= 20000
            elif cash / 10000 > 0:
                self.srl.write(b'MO2')
                cash -= 10000
            elif cash / 5000 > 0:
                self.srl.write(b'MO1')
                cash -= 5000

            while chr(ord(srl.read(1))) != 'F':
                pass

    # Return change to player
    def give_change(self, money):
        self.give_banknote(money)
       
    def move_buildings_pane(self):
        self.srl.write(b'B')

