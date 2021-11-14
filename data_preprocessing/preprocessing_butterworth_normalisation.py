import pandas as pd 
import numpy as np 
from scipy import signal, interpolate 
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

#  [Step 1: Import the data]
E4_folder = './E4_data/'

hr_path = E4_folder + 'HR.csv' # hr_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

hr_df = pd.read_csv(hr_path, header=None) # Ask XY what she means by 'eda_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

hr_start_epoch = hr_df[0][0] # Ask Robin about epoch time 

hr_hz = hr_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

hr_values = hr_df[0][2:] # Ask Robin about eda recording 

hr_values.index = hr_start_epoch + (hr_values.index - 2) / hr_hz #XZ provided code that could convert eda index to epoch, which she noted would be useful when segmenting eda data by timestamps 

plt.plot(hr_values.index, hr_values) # This plots the original hr 

# [Step 2: Remove noise using the lowpass Butterworth filter]
# Apply the Butterworth filter
def butter_lowpass(lowcut, sample_rate, order=6): # standard lowpass filter 
    nyq = 0.5 * sample_rate
    low_cutoff = lowcut/ nyq 
    b, a = signal.butter(order, low_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, lowcut, sample_rate, order=6):

    b, a = butter_lowpass(lowcut, sample_rate, order=order) # This creates a lowpass butterworth filter

    y = signal.lfilter(b, a, data) #This applies the filter to the signal (Not clear on how this works)

    return y 

hr_filtered_lp = butter_lowpass_filter(hr_values, 1, hr_hz, 6)

# constructs a pandas dataframe for the filtered hr data to be stored

hr_filtered_df = pd.DataFrame(index=hr_values.index)
hr_filtered_df['filtered_hr'] = hr_filtered_lp

"""# Create a plot graph of the two datasets to compare the original hr data and filtered hr data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original hr')
axs[1].title.set_text('Filtered hr') 

# Plot the curves 
# print("hr_values.index: ", hr_values.index) # array of float; data type = float 64; length=8784
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_lp) # *What is hr_filtered_df.index refers to the pandas dataframe where the filtered data is stored. 
#axs[1].plot(hr_values.index, hr_filtered_lp)

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()

plt.show() # display function """

# [Step 3: Normalise the hr data] 

# Physiological signals are subject-dependent (specific to the participant), which means the standard practice is to scale the data into a standard range. Normalisation can also assist with hiding personal information from body signals. There are two main normalisation methods: 
# (1) Min-max normalisation: calculated as (hr - min)(max - min)
# (2) standardisation: calculated as (hr - mean)/standard_deviation 

"Min-max normalisation & standardisation normalisation" 
def min_max_normalisation(data): # (x - x.min) / (x.max - x.min)

     x = data.reshape(-1,1) # Create x (reshaped data required by sklearn) - Why does sklearn require reshaped data? What is reshaped data and how is it different to other types of data?

     min_max_scaler = preprocessing.MinMaxScaler() # Create a minimum and maximum processor object 

     x_scaled = min_max_scaler.fit_transform(x) #Create an object to transform the data to fit minmax processor

     return x_scaled[:, 0] # Return the normaliser on the dataframe; return normalised data 


# Scale using min-max normalisation 
hr_norm = min_max_normalisation(hr_filtered_df['filtered_hr'].values) # not defined


# constructs a pandas dataframe for the normalised hr data to be stored

hr_filtered_df['scaled_hr'] = hr_norm


# [Step 4: Create a plot graph to show original hr, filtered hr and scaled hr]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original HR')
axs[1].title.set_text('Butterworth Lowpass Filtered HR') 
axs[2].title.set_text('Normalised HR')

# Plot the curves 
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_lp) #hr_filtered_df.index not defined 
axs[2].plot(hr_filtered_df.index, hr_filtered_df['scaled_hr'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display output 
plt.show()
