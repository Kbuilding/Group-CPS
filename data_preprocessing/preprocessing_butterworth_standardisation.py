import pandas as pd 
import numpy as np 
from scipy import signal, interpolate 
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

# [Step 1: Import the data]
E4_folder = './E4_data/'

hr_path = E4_folder + 'HR.csv' # hr_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

# hr_path = E4_folder + 'HR_XZ.csv' 

hr_df = pd.read_csv(hr_path, header=None) # Ask XY what she means by 'hr_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

hr_start_epoch = hr_df[0][0] # Ask Robin about epoch time 

hr_hz = hr_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

hr_values = hr_df[0][2:] # Ask Robin about hr recording 

hr_values.index = hr_start_epoch + (hr_values.index - 2) / hr_hz #XZ provided code that could convert hr index to epoch, which she noted would be useful when segmenting hr data by timestamps 

plt.plot(hr_values.index, hr_values) # This plots the original HR 

#[Step 2: Remove the noise using the lowpass Butterworth filter]
# Apply the Butterworth filter
"""def butter_lowpass(lowcut, sample_rate, order=6): # standard lowpass filter 
    nyq = 0.5 * sample_rate
    low_cutoff = lowcut/ nyq 
    b, a = signal.butter(order, low_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, lowcut, sample_rate, order=6):

    b, a = butter_lowpass(lowcut, sample_rate, order=order) # This creates a lowpass butterworth filter

    y = signal.lfilter(b, a, data) #This applies the filter to the signal

    return y 

hr_filtered_lp = butter_lowpass_filter(hr_values, 1, hr_hz, 6)"""

"""cutoff = 0.75
def butter_highpass(cutoff, sample_rate, order=2): # standard highpass filter 
        nyq = 0.5 * sample_rate
        normal_cutoff = cutoff /nyq
        b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

def butter_highpass_filter(data, cutoff, sample_rate, order=6):

    b, a = butter_highpass(cutoff, sample_rate, order=order) # This creates a highpass butterworth filter

    y = signal.lfilter(b, a, data) #This applies the filter to the signal 

    return y 

hr_filtered_lp = butter_highpass_filter(hr_values, 1, hr_hz, 6)"""

def butter_bandpass(lowcut, highcut, sample_rate, order=2): # standard bandpass filter, which filters out frequencies outside the frequency range defined by [lowcut, highcut]
        nyq = 0.5 * sample_rate
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

def butter_bandpass_filter(data, lowcut, highcut, sample_rate, order=6):

    b, a = butter_bandpass(lowcut, highcut, sample_rate, order=order) # This creates a bandpass butterworth filter

    y = signal.lfilter(b, a, data) #This applies the filter to the signal 

    return y 

hr_filtered_lp = butter_bandpass_filter(hr_values, 1, hr_hz, 6)
# constructs a pandas dataframe for the filtered HR data to be stored

hr_filtered_df = pd.DataFrame(index=hr_values.index)
hr_filtered_df['filtered_hr'] = hr_filtered_lp

"""# Create a plot graph of the two datasets to compare the original HR data and filtered HR data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original HR')
axs[1].title.set_text('Filtered HR') 

# Plot the curves 
# print("hr_values.index: ", hr_values.index) # array of float; data type = float 64; length=8784
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_lp) # *What is hr_filtered_df.index refers to the pandas dataframe where the filtered data is stored. 
#axs[1].plot(hr_values.index, hr_filtered_lp)

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()

plt.show() # display function"""

# [Step 3: Standardise the data]
def standardisation(data): #(x - x.min)/ x.standard_deviation 

    x = data.reshape(-1, 1) # Create x (reshaped data required by sklearn)
    z_score_scaler = preprocessing.StandardScaler()
    x_scaled = z_score_scaler.fit_transform(x) # Create an object to transform the data to fit standardised/z-score processor 
    return x_scaled[:, 0]  # Run the standardiser on the dataframe; return standardised data 

hr_std_norm = standardisation(hr_filtered_df['filtered_hr'].values)

hr_filtered_df['scaled_hr'] = hr_std_norm

hr_filtered_df['scaled_hr']

# [Step 4: Create a plot graph to show original HR, filtered HR and scaled HR]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original HR')
axs[1].title.set_text('Butterworth Lowpass Filtered HR') 
axs[2].title.set_text('Standardised HR')

# Plot the curves 
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_lp) #hr_filtered_df.index not defined 
axs[2].plot(hr_filtered_df.index, hr_filtered_df['scaled_hr'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display the output 
plt.show() 


