import pandas as pd
import numpy as np
import scipy.signal
import matplotlib.pyplot as mp
import matplotlib.mlab as mm
import csv

#df = pd.read_csv('/home/ken/git/EMV_test/TypeA_data.csv')
#df.head()

x = []
y = []

with open('/home/ken/git/EMV_test/TypeA_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

mp.plot(x,y,label='type A')
mp.xlabel('x')
mp.ylabel('y')
mp.title('Type A waveform')
mp.legend()
mp.show()