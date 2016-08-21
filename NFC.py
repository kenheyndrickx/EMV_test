import sys
import csv
import matplotlib
import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
import matplotlib.mlab as mm
from sympy.physics.units import length

def movingaverage(data, window):
    weights = np.repeat(1.0, window)/window
    smav = np.convolve(data, weights, 'valid') 
    return smav

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

#Read CSV file
df = pd.read_csv('/home/ken/git/EMV_test/TypeA_data.csv', names=['time','voltage'])

f = 13560000 #Frequency in Hz
mavg = 1/f #window for the moving average filter
print('window = ' + str(mavg))

tmin = df['time'].min()
tmax = df['time'].max()
tdelta = (abs(tmin)+tmax)/(len(df.index))
print('time = ' + str(abs(tmin)+tmax))
print('delta = '+str(tdelta))
t_window = mavg/tdelta
print(t_window)

#  Using the Hilbert transform, find the envelope and zero crossings  
envelope = abs(scipy.signal.hilbert(df['voltage']))
phase = np.angle(scipy.signal.hilbert(df['voltage']))
zeroCrossing = mm.find(np.diff(np.sign(np.cos(phase)))==2)

#Moving average
smav = movingaverage(envelope, t_window)

plt.subplot(211)
plt.plot(df['time'],df['voltage'])
plt.subplot(212)
plt.plot(smav, 'r',label='Envelope')
plt.show()