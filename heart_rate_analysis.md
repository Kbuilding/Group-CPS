# Measurement of Emotional Reactions and Self-Regulation 

# Heart Rate (HR) as an Indictator for Emotional State (Level of Stress) 

Electrocardiograms (ECG) and photoplethysmograms (PPG) are commonly used to measure heart rate. ECG 'measures the eletrical activations that lead to the contraction of the heart muscle, using electrodes attached to the body', whereas PPG measures 'the discoloration of the skin as blood perfuses through it' using a 'small optical sensor in conjunction with a light source'.

https://github.com/paulvangentcom/heartrate_analysis_python/blob/master/docs/heartrateanalysis.rst 

# Data Acquisition   
## Empatica E4 Wristband

### Why the E4 wristband? 
*   Equipped with multiple sensors 
*   Desktop/Browser-based portal to access the raw data
*   Real-time monitoring and recording using the mobile app 
*   Raw data is presented in .csv format and downloaded as a compressed directory (ZIP). 

### What data does the wristband collect? 

*   BVP.csv — Data from photoplethysmograph (PPG) (sampled at 64Hz). 
*   EDA.csv - Data from the electrodermal activity sensor in μS(sampled at 4 Hz).
*   IBI.csv - Inter beat intervals. (intermittent output with 1/64 second resolution). 
*   HR.csv - This file contains the average heart rate values, computed in spans of 10 seconds. For additional information, see https://support.empatica.com/hc/en-us/articles/360029469772-E4-data-HR-csv-explanation. 
*   ACC.csv — Data  from 3-axis acceleometer sensor in the range [-2g, 2g] (sampled at 32 Hz). 
*   TEMP.csv - Data from temperature sensor expressed in degrees on the Celsius (°C) scale (sampled at 4 Hz).

### Which data is used to inform the cybernetic artwork/visaulisation? Why?

# Resources 

Empatica Support (2021) Data export and formatting from E4 connect https://support.empatica.com/hc/en-us/articles/201608896-Data-export-and-formatting-from-E4-connect-

Empatica Support (2020) Recommended tools for signal processing and data analysis https://support.empatica.com/hc/en-us/articles/202872739-Recommended-tools-for-signal-processing-and-data-analysis 

Empatica (2021) E4 Wristband - Real-time physiological signals https://www.empatica.com/en-eu/research/e4/
