import pandas as pd # open source data analysis and manipulation tool https://anaconda.org/anaconda/pandas
import numpy as np # python library that supports large, multi-dimensional arrrays and matrices, as well as high-level mathematical functions https://anaconda.org/anaconda/numpy
from scipy import signal, interpolate
from scipy.signal.signaltools import medfilt # scipy ("Sigh Pie") is an open source Python library used for scientific computing and technical computing https://anaconda.org/anaconda/scipy
from sklearn import preprocessing # sklearn (Scikit-learn) is a free software machine learning library for Python https://scikit-learn.org/stable/install.html
import matplotlib.pyplot as plt # matplotlib is a Python 2D plotting library https://anaconda.org/conda-forge/matplotlib 
import os # The OS module provides functions for interacting with the operating system, including making directories. 

E4_folder = './E4_data/'

eda_path = E4_folder + 'EDA_XZ.csv' # eda_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

# hr_path = E4_folder + 'HR_XZ.csv' 

eda_df = pd.read_csv(eda_path, header=None) # Ask XY what she means by 'eda_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

eda_start_epoch = eda_df[0][0] # Ask Robin about epoch time 

eda_hz = eda_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

eda_values = eda_df[0][2:] # Ask Robin about eda recording 

eda_values.index = eda_start_epoch + (eda_values.index - 2) / eda_hz #XZ provided code that could convert eda index to epoch, which she noted would be useful when segmenting eda data by timestamps 

plt.plot(eda_values.index, eda_values) # This plots the original EDA (How can I see the plot?)

"""Noise in the data (i.e., unexpected peaks), likely caused by the natural movements of the participants, requires filtering and normalisation """

# Folder creation 

def mkdir_if_not_exist(path): # 'Def' is the keyword for defining a function, 'mkdir_if_not_exist' is the parameter(s) and ':' signals the start of the function body. A function that is called will return a value. This function makes a directory in the absence of an existing one. 
    if not isinstance(path, str): # This is the negative form of Python's isinstance function. The isinstance function returns a boolean value.
         path = os.path.join(*path) # This creates a default path (set to the path of python the machine; default function)
    if not os.path.exist(path): # This says, if there a operating system path does not exist, then make a directory
        os.makedirs(path)

# Filter selection 

"""Standard Butterworth lowpass filter
    def butter_lowpass (cutoff, sample_rate, order=2):

Parameters
-----------
cutoff: int or float 
    Frequency in Hz that acts as cutoff for filter. All frequencies above cutoff are filtered out.
sample_rate: int or float 
    Sample rate of the supplied signal.
order: int 
    Filter order, defines the strenght of the roll-off around the cutoff frequency. Orders above 6 are not used frequently, with 2 as the default. 

Returns 
--------
out: tuple 
    Numerator and  denominator (b, a) polynominals of the defined Butterworth IIR filter. 

Example: b, a = butter_lowpass(cutoff = 2, sample_rate = 100, order = 2)

Glossary 
---------
nyq = Nyquist frequency (folding frequency) coverts a continuous function or signal into a discrete sequence. It's value is one-half of the sampling rate. Used to see what is the max frequency that you can extract from a signal. 
btype = butterworth type 
nyq = 0.5 * sample_rate
normal_cutoff = cutoff / nyq
b, a = butter(order, normal_cutoff, btype='low', analog=False), return b,a 
Hz = cycles per second 
Sample rate = samples per second

         """

def butter_lowpass(lowcut, sample_rate, order=6): # standard lowpass filter 
    nyq = 0.5 * sample_rate
    low_cutoff = lowcut/ nyq 
    b, a = signal.butter(order, low_cutoff, btype='low', analog=False)
    return b, a 

"""def butter_highpass(cuttoff, sample_rate, order=2): # standard highpass filter 
        nyq = 0.5 * sample_rate
        normal_cutoff = cutoff /nyq
        b, a = butter(order, normal_cutoff, bytpe='high', analog=False)
        return b, a
        
    def butter_bandpass(lowcut, highcut, sample_rate, order=2): # standard bandpass filter, which filters out frequencies outside the frequency range defined by [lowcut, highcut]
        nyq = 0.5 * sample_rate
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a
        """

def butter_lowpass_filter(data, lowcut, sample_rate, order=6):

    b, a = butter_lowpass(lowcut, sample_rate, order=order) # This creates a lowpass butterworth filter

    y = signal.lfilter(b, a, data) #This applies the filter to the signal (Not clear on how this works)

    return y 

def median_filter(data, window_length=11): # Median filter is used to remove noise 

     """ Parameters 
     ---------------
     data = physiological data to be filtered
     window length = the length of the filter window; positive int 
     return = filtered data 
     """
     return signal-medfilt(data, window_length)   
    
