"""
 python application to talk to ardunio.
 logs data from arduino and displays it to GUI.
"""
from serial import Serial
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

RESULTS_FILE = "./application/results.csv"
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
TIMEOUT = 1
GRAPH_WIDTH = 100
SAMPLE_SIZE = 100
count = 0
#establish connection with arduino
ser = Serial(COM_PORT, BAUD_RATE, timeout=TIMEOUT)
while ser.read() == 'A':
	ser.write("a")

#set up csv results file.
with open(RESULTS_FILE, 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows([['Time','Voltage']])

	#set up real time ploting
	fig = plt.figure()
	plt.axis([0,GRAPH_WIDTH,0,6])
	plt.title(' volts')
	plt.ion()
	plt.show()

	#read data
	while ser.isOpen():
		readings = []
		for i in range(0,SAMPLE_SIZE):
			voltage = ser.readline()
			#clean up input.
			voltage = voltage[:voltage.index('\r')]
			voltage = ( int(voltage, 2)* .004882812)
			readings.append(voltage)
		average = sum(readings)/len(readings)
		time = datetime.now().time()
		row = [[time.strftime('%H%M%S%f'),average]]
		writer.writerows(row)
		print voltage
		plt.scatter(count, average)
		plt.title('{:4.2f} volts'.format(average))
		plt.draw()
		count = count + 1
		if count == GRAPH_WIDTH:
			plt.clf()
			plt.axis([0,GRAPH_WIDTH,0,6])
			plt.title('volts')
			plt.ion()
			plt.show()
			count = 0
	print len(data)	



def update_line(num, data, line):
	line.set_data(data[...,:num])
	return line
#manipulate data
#store data
#display data


