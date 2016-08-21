import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as mp
import matplotlib.mlab as mm
import csv
from matplotlib.axis import Axis

#df = pd.read_csv('/home/ken/git/EMV_test/TypeA_data.csv')
#df.head()

f = 13560000 #Frequency in Hz
mavg = 1/f #window for the moving average filter

x = []
y = []

with open('/home/ken/git/EMV_test/TypeA_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])
        

# Moving average filter

        
#  Using the Hilbert transform, find the envelope and zero crossings
envelope = abs(scipy.signal.hilbert(y))
phase = np.angle(scipy.signal.hilbert(y))
zeroCrossing = mm.find(np.diff(np.sign(np.cos(phase)))==2)

Vmax = max(envelope)
print(Vmax)

mp.subplot(211)
mp.plot(x,y,label='Waveform')
#mp.hold('on')
mp.subplot(212)
mp.plot(x,envelope, 'r',label='Envelope')
mp.axis('tight')
mp.xlabel('Time')
mp.ylabel('Amplitude')
mp.title('Type A waveform')
mp.legend()
mp.show()