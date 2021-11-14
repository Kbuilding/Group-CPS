import pandas as pd 
import numpy as np 
from scipy import signal, interpolate
from scipy.signal.signaltools import medfilt # This was a suggested add-on by Pylance
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

E4_folder = './E4_data/'

hr_path = E4_folder + 'HR.csv' # hr_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

# hr_path = E4_folder + 'HR_XZ.csv' 

hr_df = pd.read_csv(hr_path, header=None) # Ask XY what she means by 'hr_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

hr_start_epoch = hr_df[0][0] # Ask Robin about epoch time 

hr_hz = hr_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

hr_values = hr_df[0][2:] # Ask Robin about hr recording 

hr_values.index = hr_start_epoch + (hr_values.index - 2) / hr_hz #XZ provided code that could convert hr index to epoch, which she noted would be useful when segmenting hr data by timestamps 

#plt.plot(hr_values.index, hr_values) # This plots the original hr

# [Step 2: Remove noise using the median filter] 

def median_filter(data, window_length=11): # Median filter is used to remove noise 

    return signal.medfilt(data, window_length)   

""" Parameters 
     ---------------
     data = physiological data to be filtered
     window length = the length of the filter window; positive int 
     return = filtered data 
     """

# Apply the median filter (used to remove noise from the signal)

hr_filtered_median = median_filter(hr_values, 31) 

# constructs a pandas dataframe for the filtered hr data to be stored

hr_filtered_df = pd.DataFrame(index=hr_values.index)

hr_filtered_df['filtered_hr'] = hr_filtered_median 

"""# Create a plot graph of the two datasets to compare the original hr data and filtered hr data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original HR')
axs[1].title.set_text('Filtered HR') 

# Plot the curves 
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_median) #hr_filtered_df.index not defined 

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()"""

# [Step 3: Standardise the HR data]

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
axs[1].title.set_text('Median Filtered HR') 
axs[2].title.set_text('Standardised HR')

# Plot the curves 
axs[0].plot(hr_values.index, hr_values.values)
axs[1].plot(hr_filtered_df.index, hr_filtered_median) #hr_filtered_df.index not defined 
axs[2].plot(hr_filtered_df.index, hr_filtered_df['scaled_hr'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display the output 
plt.show()
