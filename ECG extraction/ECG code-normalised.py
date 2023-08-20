from math import ceil
import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import gnuplotpy as gp
plt.ion()

fig = plt.figure()

toc1 = 0
count = 0
x = list()
y = list()

ser = serial.Serial('COM3', 9600)
ser.close()
ser.open()
tic = time.time()
while count < 35:
    data = ser.readline()
    toc = time.time()
    toc1 = toc - tic
    tic = toc
    count += toc1
    value = float(data.decode())
    x.append(count)
    value = value / 10
    value = 10 * round(value)
    print(value)
    y.append(value)
    plt.plot(x,y,'g')
    plt.show()
    plt.pause(0.1)
plt.ioff()
plt.clf()
for i in y:
    y[i]=y[i]/max(y)
print(len(y))
print(x)
for i in range(len(y),188):
    y.append(0)
    x.append(x[len(x)-1])
plt.plot(x,y)
plt.savefig('wave1.png', dpi=800)
"""
args = {'the_title': 'ECG' , 'amp': max(y) , 'x_max': x[-1] , 'filename': 'test1.png'}
data = [x, y]
gp.gnuplot('test.gpi', args, data)
"""