"""
 python application to talk to ardunio.
 logs data from arduino and displays it to GUI.
"""
from serial import Serial
from datetime import datetime
import csv

RESULTS_FILE = "./application/results.csv"
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
TIMEOUT = 1
data = []

#establish connection with arduino
ser = Serial(COM_PORT, BAUD_RATE, timeout=TIMEOUT)
while ser.read() == 'A':
	ser.write("a")

#set up csv results file.
with open(RESULTS_FILE, 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows([['Time','Voltage']])
	while ser.isOpen():
		readings = []
		#read data
		for i in range(0,9):
			voltage = ser.readline()
			#clean up input.
			voltage = voltage[:voltage.index('\r')]
			voltage = ( int(voltage, 2)* .004882812)
			readings.append(voltage)
		average = sum(readings)/len(readings)
		time = datetime.now().time()
		row = [[time.strftime('%H%M%S%f'),average]]
		writer.writerows(row)
		data.append(average)
		print voltage
		print len(data)	

#manipulate data
#store data
#display data


