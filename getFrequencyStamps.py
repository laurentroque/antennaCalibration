# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:55:18 2018

@author: ilvr2

This script obtains the frequency stamps from the antenna calibration
measurements.

Code is tested using data from RAPID: "PL_load.prn"
"""

def getFrequencyStamps(filename):
    # Open and read the files
    f = open(str(filename), 'r')
    dataInput = f.readlines()
    f.close()
   
    # Frequency stamps will temporarily be stored here before being returned
    dataLines = []
    frequency = []
    
    # Removing new-line characters
    for i in range(len(dataInput)):
        dataLines.append(dataInput[i].rstrip('\n').split(','))
    
    # Get number of data points plus 2 for headers
    npts = len(dataLines)
    
    for i in range(2, npts):
        for j in range(0, 2):
            # Converting string data into number data as double array
            dataLines[i][j] = float(dataLines[i][j])
        
        # Adding frequencies to the list and returning
        frequency.append(dataLines[i][0])
    return frequency
    
# Test to see if it works
frequency = []
frequency = getFrequencyStamps('PL_load.prn')

print frequency
print type(frequency)
print len(frequency)