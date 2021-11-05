import pandas as pd 
import numpy as np 
from scipy import signal, interpolate
from scipy.signal.signaltools import medfilt # This was a suggested add-on by Pylance
from sklearn import preprocessing 
import matplotlib.pyplot as plt 
import os 

E4_folder = './E4_data/'

eda_path = E4_folder + 'EDA_XZ.csv' # eda_path creates a pathway for the electrodermal activity data, noting that you get the data via the cps_project folder 

# hr_path = E4_folder + 'HR_XZ.csv' 

eda_df = pd.read_csv(eda_path, header=None) # Ask XY what she means by 'eda_df' (i.e., does 'df' denote data file?) and about header=None. Pandas is used to read the csv file. 

# hr_df = pd.read_csv(hr_path, header=None)

eda_start_epoch = eda_df[0][0] # Ask Robin about epoch time 

eda_hz = eda_df[0][1] # Ask Robin about sampling rate. 'hz' refers to hertz.

eda_values = eda_df[0][2:] # Ask Robin about eda recording 

eda_values.index = eda_start_epoch + (eda_values.index - 2) / eda_hz #XZ provided code that could convert eda index to epoch, which she noted would be useful when segmenting eda data by timestamps 

#plt.plot(eda_values.index, eda_values) # This plots the original EDA

# [Step 2: Remove noise using the median filter] 

def median_filter(data, window_length=11): # Median filter is used to remove noise 

    return signal.medfilt(data, window_length)   

""" Parameters 
     ---------------
     data = physiological data to be filtered
     window length = the length of the filter window; positive int 
     return = filtered data 
     """

# Apply the median filter 

eda_filtered_median = median_filter(eda_values, 31) # median filter is not defined

# constructs a pandas dataframe for the filtered eda data to be stored

eda_filtered_df = pd.DataFrame(index=eda_values.index)

eda_filtered_df['filtered_eda'] = eda_filtered_median 

"""# Create a plot graph of the two datasets to compare the original EDA data and filtered EDA data

# Define a space of two rows 
fig, axs = plt.subplots(2) 

# Assign titles to the graphs 
axs[0].title.set_text('Original EDA')
axs[1].title.set_text('Filtered EDA') 

# Plot the curves 
axs[0].plot(eda_values.index, eda_values.values)
axs[1].plot(eda_filtered_df.index, eda_filtered_median) #eda_filtered_df.index not defined 

# Format the two graphs to ensure that they don't overlap
plt.tight_layout()"""

# [Step 3: Standardise the EDA data]

def standardisation(data): #(x - x.min)/ x.standard_deviation 
    x = data.reshape(-1, 1) # Create x (reshaped data required by sklearn)
    z_score_scaler = preprocessing.StandardScaler()
    x_scaled = z_score_scaler.fit_transform(x) # Create an object to transform the data to fit standardised/z-score processor 
    return x_scaled[:, 0]  # Run the standardiser on the dataframe; return standardised data 

eda_std_norm = standardisation(eda_filtered_df['filtered_eda'].values)

eda_filtered_df['scaled_eda'] = eda_std_norm

eda_filtered_df['scaled_eda']

# [Step 4: Create a plot graph to show original EDA, filtered EDA and scaled EDA]

# Define a space of three rows 
fig, axs = plt.subplots(3) 

# Assign titles to the graphs 
axs[0].title.set_text('Original EDA')
axs[1].title.set_text('Butterworth Median Filtered EDA') 
axs[2].title.set_text('Standardised EDA')

# Plot the curves 
axs[0].plot(eda_values.index, eda_values.values)
axs[1].plot(eda_filtered_df.index, eda_filtered_median) #eda_filtered_df.index not defined 
axs[2].plot(eda_filtered_df.index, eda_filtered_df['scaled_eda'])

# Format the three graphs to ensure that they don't overlap
plt.tight_layout()

# Display the output 
plt.show()
