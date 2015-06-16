"""
 python application to talk to ardunio.
 logs data from arduino and displays it to GUI.
"""
from serial import Serial
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
TIMEOUT = 1

#establish connection with arduino
ser = Serial(COM_PORT, BAUD_RATE, timeout=TIMEOUT)
ser.write("a")


#read data
while ser.isOpen():
	print(ser.read())

#manipulate data
#store data
#display data


