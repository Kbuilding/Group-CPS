# Preprocess BVP 

This guide is adapted from Dr Xuanying Zhu's tutorial for preprocessing EDA (Electrodermal Activity) data.

## Step 1 - Import Libraries 

The first step is to import the required libraries and set up paths.

For preprocessing Heart Rate (HR) and Blood Volume Pulse (BVP) data, the key libraries are:

- SciPy (Scientific and technical computing library for Python) https://scipy.org
- Scikit-learn (Machine learning library for Python) github.com/scikit-learn/scikit-learn
- NumPy (Numerical manipulation library for Python) https://numpy.org
- Matplotlib (Plotting library for Python) https://matplotlib.org
- Pandas (Data manipulation and analysis library for Python) https://pandas.pydata.org
- Heartpy (Heart rate analysis toolkit for Python) heartpy

## Step 2 - Read and Plot BVP

Create a path to the BVP data by way of the folder containing the .csv files. 

> bvp_path = E4_folder + 'BVP.csv'

Read the BVP.csv file. 

> bvp_df = pd.read_csv(bvp_path, header=None)

Get start epoch time.

> bvp_start_epoch = bvp_df[0][0]

Get sample rate. 

> bvp_hz = bvp_df[0][1]

Get BVP recording. 
