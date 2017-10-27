import serial

srl = serial.Serial('/dev/ttyUSB0')
srl.baudrate=19200

while True:
    srl.write(b'A')
    print(srl.read(1))
