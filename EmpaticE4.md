# Empatica E4

The raw data from the Empatica E4 is accessible via the E4 connect portal. 

The raw data is presented in CSV format and downloaded as a compressed directory (ZIP).


Data that could be used for the visualisation: 

BVP.csv — Data from photoplethysmograph (PPG) (sampled at 64Hz). 

EDA.csv - Data from the electrodermal activity sensor in μS(sampled at 4 Hz).

IBI.csv - Inter beat intervals. (intermittent output with 1/64 second resolution). 

HR.csv - This file contains the average heart rate values, computed in spans of 10 seconds. For additional information, see https://support.empatica.com/hc/en-us/articles/360029469772-E4-data-HR-csv-explanation. 


Additional data captured by the Empatica E4 that will be excluded from the visualisation:

ACC.csv — Data  from 3-axis acceleometer sensor in the range [-2g, 2g] (sampled at 32 Hz). 

TEMP.csv - Data from temperature sensor expressed in degrees on the Celsius (°C) scale (sampled at 4 Hz).



# Resources 

Empatica Support (2021) Data export and formatting from E4 connect https://support.empatica.com/hc/en-us/articles/201608896-Data-export-and-formatting-from-E4-connect-

Empatica Support (2020) Recommended tools for signal processing and data analysis https://support.empatica.com/hc/en-us/articles/202872739-Recommended-tools-for-signal-processing-and-data-analysis 

