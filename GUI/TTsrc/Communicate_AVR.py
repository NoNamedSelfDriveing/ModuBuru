import serial
import time
import os
import Adafruit_TCS34725 as TCS

class ComAVR:
    def __init__(self):
        self.srl = serial.Serial('/dev/ttyUSB0')
        self.srl.baudrate = 19200
        self.tcs = TCS.TCS34725()
        self.tcs.set_interrupt(False)

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
        cash = money
        n_money = 0
        isInputting = False
        nlist = [0, 0, 0, 0, 0, 0]
        money_list = [5000, 10000, 20000, 50000, 100000, 500000]

        while cash > 0:
            r, g, b, _ = self.tcs.get_raw_data()
            temp = TCS.calculate_color_temperature(r, g, b)
            if temp in range(27000, 34000) and r < 140:
                print('Nope', temp, r)
                srl.write(b'MI0')
                pass
            else:
                while True:
                    r, g, b, _ = self.tcs.get_raw_data()
                    temp = TCS.calculate_color_temperature(r, g, b)
                    print('In', temp, r)
                    # 5000
                    if temp in range(50000, 77000):
                        if isInputting:
                            pass
                        else:
                            isInputting = True
                        srl.write(b'MI1')
                        nlist[0] += 1
                    # 10000
                    elif temp in range(500000, 5000000):
                        if isInputting:
                            pass
                        else:
                            isInputting = True
                        srl.write(b'MI2')
                        nlist[1] += 1
                    # 20000
                    elif temp in range(12000, 20000):
                        if isInputting:
                            pass
                        else:
                            isInputting = True
                        srl.write(b'MI3')
                        nlist[2] += 1
                    # 50000
                    elif temp in range(23000, 30000) and r > 200:
                        if isInputting:
                            pass
                        else:
                            isinputting = True
                        srl.write(b'MI4')
                        nlist[3] += 1
                    # 100000
                    elif temp in range(130000, 310000):
                        if isInputting:
                            pass
                        else:
                            isInputting = True
                        srl.write(b'MI5')
                        nlist[4] += 1
                    # 500000
                    elif temp < -10000:
                        if isInputting:
                            pass
                        else:
                            isInputting = True
                        srl.write(b'MI6')
                        nlist[5] += 1
                    elif temp in range(27000, 34000) and r > 140:
                        pass
                    elif temp in range(27000, 34000) and r < 140:
                        if isInputting:
                            t = 0
                            l = 0
                            for i in range(len(nlist)):
                                if t < nlist[i]:
                                    t = nlist[i]
                                    l = i

                            n_money = money_list[l]
                            cash -= n_money
                            for i in range(len(nlist)):
                                nlist[i] = 0

                            isInputting = False
                        break
        
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

    '''

a = ComAVR()
a.get_banknote(35000)
