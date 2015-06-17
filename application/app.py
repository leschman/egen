"""
 python application to talk to ardunio.
 logs data from arduino and displays it to GUI.
"""
from serial import Serial


COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
TIMEOUT = 1
data = []

#establish connection with arduino
ser = Serial(COM_PORT, BAUD_RATE, timeout=TIMEOUT)
while ser.read() == 'A':
	ser.write("a")


#read data
while ser.isOpen():
	readings = []
	for i in range(0,9):
		voltage = ser.readline()
		#clean up input.
		voltage = voltage[:voltage.index('\r')]
		voltage = ( int(voltage, 2)* .004882812)
		readings.append(voltage)
	average = sum(readings)/len(readings)
	data.append(average)
	print voltage
	print len(data)	
#	print repr(voltage)

#manipulate data
#store data
#display data


