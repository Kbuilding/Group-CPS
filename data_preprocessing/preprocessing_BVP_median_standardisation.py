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

# constructs a pandas dataframe for the filtered BVP data to be stored

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

# [Step 3: Standardise the BVP data]

def standardisation(data): #(x - x.min)/ x.standard_deviation 
    x = data.reshape(-1, 1) # Create x (reshaped data required by sklearn)
    z_score_scaler = preprocessing.StandardScaler()
    x_scaled = z_score_scaler.fit_transform(x) # Create an object to transform the data to fit standardised/z-score processor 
    return x_scaled[:, 0]  # Run the standardiser on the dataframe; return standardised data 

bvp_std_norm = standardisation(bvp_filtered_df['filtered_bvp'].values)

bvp_filtered_df['scaled_bvp'] = bvp_std_norm

bvp_filtered_df['scaled_bvp']

# [Step 4: Create a plot graph to show original BVP, filtered BVP and scaled BVP]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original BVP')
axs[1].title.set_text('Median Filtered BVP') 
axs[2].title.set_text('Standardised BVP')

# Plot the curves 
axs[0].plot(bvp_values.index, bvp_values.values)
axs[1].plot(bvp_filtered_df.index, bvp_filtered_median)
axs[2].plot(bvp_filtered_df.index, bvp_filtered_df['scaled_bvp'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display the output 
plt.show()
