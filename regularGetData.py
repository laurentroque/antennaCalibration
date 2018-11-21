# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:43:00 2018

@author: ilvr2

This function will populate a list with frequency stamps and measurements from
data files supplied. Each event is stored in a 2D list event[i][j] with i being
the frequency stamp and j being the measurement. 

***This only works with two column data sets and cannot be used with sets
containing matricies such as S11 data. A seperate script will be created for 
that later

This script is tested with RAPID using 'PL_load.prn' containing spectra of an 
external load.
"""

def regularGetData(filename):
    # Open and read the files
    f = open(str(filename), 'r')
    dataInput = f.readlines()
    f.close()
   
    # Frequency stamps will temporarily be stored here before being returned
    dataLines = []
        
    # Removing new-line characters
    for i in range(2, len(dataInput)):
        dataLines.append(dataInput[i].rstrip(',\n').split(','))
    
    # Get number of data points plus 2 for headers
    npts = len(dataLines)
    
    for i in range(0, npts):
        for j in range(0, 2):
            # Converting string data into number data as double array
            dataLines[i][j] = float(dataLines[i][j])
        # Converting dB/HZ to W/Hz    
        dataLines[i][1] = 10.00** ((dataLines[i][1] - 30.00) / 10.0)            

        
    return dataLines

'''
# Test to see if it works
regularData = []
regularData = regularGetData('PL_load.prn')

print regularData
print type(regularData)
print len(regularData)
'''

