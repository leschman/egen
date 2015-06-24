"""
 python application to talk to ardunio.
 logs data from arduino and displays it to GUI.
"""
from serial import Serial
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt
from math import exp

RESULTS_FILE = "./application/results.csv"
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
TIMEOUT = 1
GRAPH_WIDTH = 100
SAMPLE_SIZE = 100
VOLTAGE_STEP_SIZE = .004882812
count = 0

def update_line(num, data, line):
	line.set_data(data[...,:num])
	return line

#manipulate data
def manipulate_data(data):
	try:
		data = data[:data.index('\r')]
		data = int(data, 2)  
		return data
	except ValueError:
		return 0.1 

#set up real time ploting
def setup_plot():
	plt.clf()
	plt.axis([0,GRAPH_WIDTH,0,30])
	plt.title(' volts')
	plt.ion()
	plt.show()

#establish connection with arduino
ser = Serial(COM_PORT, BAUD_RATE, timeout=TIMEOUT)
while ser.read() == 'A':
	print "Establishing serial connection, standby...     \r"
	ser.write("a")

print ""

#set up csv results file.
with open(RESULTS_FILE, 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows([['Time','Voltage']])

	fig = plt.figure()
	setup_plot()

	#read data
	while ser.isOpen():
		readings = []
		for i in range(0,SAMPLE_SIZE):
			voltage = ser.readline()
		
			#clean up input.
			data = manipulate_data(voltage)
			if data:
				salinity = 2 *10 ** -21 * exp(0.0677 * data)  
				readings.append(salinity)

		if len(readings) > 0:
			average = sum(readings)/len(readings)
			time = datetime.now().time()
			row = [[time.strftime('%H%M%S%f'),average]]
			writer.writerows(row)
			print '{0}, {1}, {2}'.format(data, average, count)
			plt.scatter(count, average)
			plt.title('{:4.2f} % solute by weight'.format(average))
			plt.draw()
			count = count + 1
			if count >= GRAPH_WIDTH:
				setup_plot()
				count = 0


