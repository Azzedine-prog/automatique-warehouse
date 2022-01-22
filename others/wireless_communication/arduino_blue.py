#! /usr/bin/python
import serial
from time import sleep
bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
count = None
while count == None:
    try:
        count = int(raw_input( "Please enter the number of times to blink the L"))
    except:
        pass    # Ignore any errors that may occur and try again
bluetoothSerial.write( str(count) )
print(bluetoothSerial.readline())
