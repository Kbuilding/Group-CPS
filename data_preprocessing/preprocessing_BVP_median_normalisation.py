# Dr Xuanying Zhu kindly provided starter code for the data pre-processing, which has been adapted to meet the purposes of our CPS. 

import pandas as pd 
import numpy as np 
from scipy import signal, interpolate
from scipy.signal.signaltools import medfilt # This was a suggested add-on by Pylance
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

E4_folder = './E4_data/'

bvp_path = E4_folder + 'BVP.csv' # bvp_path creates a pathway for the BVP data, noting that you get the data via the cps_project folder 

bvp_df = pd.read_csv(bvp_path, header=None) # 'df' denotes data file and Pandas is used to read the csv file. 

bvp_start_epoch = bvp_df[0][0] # epoch time 

bvp_hz = bvp_df[0][1] # 'hz' refers to hertz.

bvp_values = bvp_df[0][2:]

bvp_values.index = bvp_start_epoch + (bvp_values.index - 2) / bvp_hz #XZ provided code that could convert bvp index to epoch, which she noted would be useful when segmenting bvp data by timestamps 

plt.plot(bvp_values.index, bvp_values) # This plots the original BVP

# [Step 2: Remove noise using the median filter] 
def median_filter(data, window_length=11): # Median filter is used to remove noise 
     
     return signal.medfilt(data, window_length)
     """ Parameters 
     ---------------
     data = physiological data to be filtered
     window length = the length of the filter window; positive int 
     return = filtered data 
     """
   
# Apply the median filter (used to reduce noise in the signal)
bvp_filtered_median = median_filter(bvp_values, 31) 

# constructs a pandas dataframe for the filtered hr data to be stored

bvp_filtered_df = pd.DataFrame(index=bvp_values.index)
bvp_filtered_df['filtered_bvp'] = bvp_filtered_median 

"""# Create a plot graph of the two datasets to compare the original BVP data and filtered BVP data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original BVP')
axs[1].title.set_text('Filtered BVP') 

# Plot the curves 
axs[0].plot(bvp_values.index, bvp_values.values)
axs[1].plot(bvp_filtered_df.index, bvp_filtered_median) #bvp_filtered_df.index not defined 

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()"""

# [Step 3: Normalise the BVP data] 

# Physiological signals are subject-dependent (specific to the participant), which means the standard practice is to scale the data into a standard range. Normalisation can also assist with hiding personal information from body signals. There are two main normalisation methods: 
# (1) Min-max normalisation: calculated as (BVP - min)(max - min)
# (2) standardisation: calculated as (BVP - mean)/standard_deviation 

"Min-max normalisation & standardisation normalisation" 
def min_max_normalisation(data): # (x - x.min) / (x.max - x.min)

     x = data.reshape(-1,1) # Create x (reshaped data required by sklearn)

     min_max_scaler = preprocessing.MinMaxScaler() # Create a minimum and maximum processor object 

     x_scaled = min_max_scaler.fit_transform(x) #Create an object to transform the data to fit minmax processor

     return x_scaled[:, 0] # Return the normaliser on the dataframe; return normalised data 


# Scale using min-max normalisation 
bvp_norm = min_max_normalisation(bvp_filtered_df['filtered_bvp'].values) # not defined


# constructs a pandas dataframe for the normalised bvp data to be stored

bvp_filtered_df['scaled_bvp'] = bvp_norm

# [Step 4: Create a plot graph to show original BVP, filtered BVP and scaled BVP]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original BVP')
axs[1].title.set_text('Median Filtered BVP') 
axs[2].title.set_text('Normalised BVP')

# Plot the curves 
axs[0].plot(bvp_values.index, bvp_values.values)
axs[1].plot(bvp_filtered_df.index, bvp_filtered_median) #bvp_filtered_df.index not defined 
axs[2].plot(bvp_filtered_df.index, bvp_filtered_df['scaled_bvp'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display the output 
plt.show() 
