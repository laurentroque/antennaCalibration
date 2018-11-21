# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:50:05 2018

@author: ilvr2

Script to onvert dBm/Hz to W/Hz for data collected with a 10Hz bandwidth
"""

def convertUnitsAtTen(filename):  
    # Read trace files (convert dBm/Hz to W/Hz) and convert to list
    f = open(str(filename), 'r')
    dataInput = f.readlines()
    f.close()
    
    dataLines = []
    frequency = []
    measurement = []
    # Remove newline characters
    for i in range(len(dataInput)):
        dataLines.append(dataInput[i].rstrip('\n').split(','))
    
    # Get number of data points plus 2 for headers
    npts = len(dataLines)  
    
    for i in range(2, npts):
        for j in range(0, 2):
            # Converting string data into number data as double array
            dataLines[i][j] = float(dataLines[i][j])
        
        frequency.append(dataLines[i][0])
        measurement.append(dataLines[i][1])

    # Mathematical conversion
    for i in range(len(measurement)):
        measurement[i] = 10.00** (((measurement[i] - 10) - 30.00) / 10.0)
    
    # Return the converted data points
    return measurement

'''
externalLoadSpectra = []
externalLoadSpectra = convertUnitsAtTen('PL_load.prn')

# More tests...
print externalLoadSpectra
print type(externalLoadSpectra)
print len(externalLoadSpectra)
'''