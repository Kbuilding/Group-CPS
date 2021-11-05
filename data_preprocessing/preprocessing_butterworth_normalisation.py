import pandas as pd 
import numpy as np 
from scipy import signal, interpolate 
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

#  [Step 1: Import the data]
E4_folder = './E4_data/'

eda_path = E4_folder + 'EDA_XZ.csv' # eda_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

# hr_path = E4_folder + 'HR_XZ.csv' 

eda_df = pd.read_csv(eda_path, header=None) # Ask XY what she means by 'eda_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

eda_start_epoch = eda_df[0][0] # Ask Robin about epoch time 

eda_hz = eda_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

eda_values = eda_df[0][2:] # Ask Robin about eda recording 

eda_values.index = eda_start_epoch + (eda_values.index - 2) / eda_hz #XZ provided code that could convert eda index to epoch, which she noted would be useful when segmenting eda data by timestamps 

plt.plot(eda_values.index, eda_values) # This plots the original EDA 

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

eda_filtered_lp = butter_lowpass_filter(eda_values, 1, eda_hz, 6)

# constructs a pandas dataframe for the filtered eda data to be stored

eda_filtered_df = pd.DataFrame(index=eda_values.index)
eda_filtered_df['filtered_eda'] = eda_filtered_lp

"""# Create a plot graph of the two datasets to compare the original EDA data and filtered EDA data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original EDA')
axs[1].title.set_text('Filtered EDA') 

# Plot the curves 
# print("eda_values.index: ", eda_values.index) # array of float; data type = float 64; length=8784
axs[0].plot(eda_values.index, eda_values.values)
axs[1].plot(eda_filtered_df.index, eda_filtered_lp) # *What is eda_filtered_df.index refers to the pandas dataframe where the filtered data is stored. 
#axs[1].plot(eda_values.index, eda_filtered_lp)

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()

plt.show() # display function """

# [Step 3: Normalise the EDA data] 

# Physiological signals are subject-dependent (specific to the participant), which means the standard practice is to scale the data into a standard range. Normalisation can also assist with hiding personal information from body signals. There are two main normalisation methods: 
# (1) Min-max normalisation: calculated as (EDA - min)(max - min)
# (2) standardisation: calculated as (EDA - mean)/standard_deviation 

"Min-max normalisation & standardisation normalisation" 
def min_max_normalisation(data): # (x - x.min) / (x.max - x.min)

     x = data.reshape(-1,1) # Create x (reshaped data required by sklearn) - Why does sklearn require reshaped data? What is reshaped data and how is it different to other types of data?

     min_max_scaler = preprocessing.MinMaxScaler() # Create a minimum and maximum processor object 

     x_scaled = min_max_scaler.fit_transform(x) #Create an object to transform the data to fit minmax processor

     return x_scaled[:, 0] # Return the normaliser on the dataframe; return normalised data 


# Scale using min-max normalisation 
eda_norm = min_max_normalisation(eda_filtered_df['filtered_eda'].values) # not defined


# constructs a pandas dataframe for the normalised eda data to be stored

eda_filtered_df['scaled_eda'] = eda_norm


# [Step 4: Create a plot graph to show original EDA, filtered EDA and scaled EDA]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original EDA')
axs[1].title.set_text('Butterworth Lowpass Filtered EDA') 
axs[2].title.set_text('Normalised EDA')

# Plot the curves 
axs[0].plot(eda_values.index, eda_values.values)
axs[1].plot(eda_filtered_df.index, eda_filtered_lp) #eda_filtered_df.index not defined 
axs[2].plot(eda_filtered_df.index, eda_filtered_df['scaled_eda'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display output 
plt.show()

