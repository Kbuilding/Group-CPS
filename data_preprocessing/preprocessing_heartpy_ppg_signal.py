import matplotlib.pyplot as plt
import heartpy as hp
import pandas as pd 
import numpy as np 
from scipy import signal, interpolate
from scipy.signal.signaltools import medfilt # This was a suggested add-on by Pylance
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

# E4_folder = './E4_data/'

# BVP.csv is the output data from the photoplethysmograph.

# bvp_path = E4_folder + 'BVP.csv' # bvp_path creates a pathway for the BVP data, noting that you get the data via the E4_data folder 

# bvp_df = pd.read_csv(bvp_path, header=None) 

data = hp.get_data('BVP.csv')

"""
# first let's load the clean PPG signal
data, timer = bvp_path(0)
# hp.load_exampledata(0)

# to visualise the data
plt.figure(figsize=(12,4)) 
plt.plot(data)
plt.show()

# run the analysis
wd, m = hp.process(data, sample_rate = 100.0)  # wd = working data, m = measures

# to visualize the results of the analysis

# set large figure
plt.figure(figsize=(12,4)) # dictates the size of the figure

# call plotter
hp.plotter(wd, m)

# display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

data, timer = hp.load_exampledata(1)

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

# computes sample rate based on a ms-timer
sample_rate = hp.get_samplerate_mstimer(timer)

wd, m = hp.process(data, sample_rate)

#plot
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

# recording that uses datetime strings to encode time

data, timer = hp.load_exampledata(2) # computes sample_rate based on a column in datetime values 

print(timer[0])

# Note: When computing the sample rate we need to give get_samplerate_datetime() the format of the string (by default it expects HH:MM:SS.ms)

sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')

print('sample rate is: %f Hz' %sample_rate)

wd, m = hp.process(data, sample_rate, report_time = True)

#plot
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#let's zoom in on a bit
plt.figure(figsize=(12,4))
plt.xlim(20000, 30000)
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
    """