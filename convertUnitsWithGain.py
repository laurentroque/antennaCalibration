# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 15:38:44 2018

@author: ilvr2

Script to onvert dBm/Hz to W/Hz taking into account an extra 50dB gain at the 
output
"""

def convertUnitsWithGain(filename):
    
    '''
    # Part of SMOP conversion, may not be neccessary 
    varargin = readpower.varargin
    nargin = readpower.nargin
    '''
    
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
    
    '''
    # Test to print all the data collected
    print 'Data: -', type(dataLines) 
    print 'Number of points', str(npts-2)
    print dataLines
    
    print
    # print first data set
    print dataLines[2]
    # First data set, Measurement
    print dataLines[2][0]
    # First data set, Uncretainty
    print dataLines[2][1]
    # First data set superfluous line
    print dataLines[2][2]
    '''

    '''
    # From original MatLab code, may not be neccessary
    TYPE = fgetl(f)
    PARAM = fgetl(f)
    '''
    
    
    for i in range(2, npts):
        for j in range(0, 2):
            # Converting string data into number data as double array
            #tmp = str2num(fgetl(f))
            dataLines[i][j] = float(dataLines[i][j])
        
        frequency.append(dataLines[i][0])
        measurement.append(dataLines[i][1])
            #ff[ii] = tmp(1)
            #dd[ii] = tmp(2)
    

    # Mathematical conversion
    #dd = 10.0 ** ((dd - 30.0) / 10.0)
    for i in range(len(measurement)):
        measurement[i] = 10.00** (((measurement[i] + 50) - 30.00) / 10.0)
    
    '''
    # Checks for correct conversion
    print 'frequency', frequency
    print
    print 'measurement', measurement
    '''
    
    # Return the converted data points
    
    # All measurements are taken at the same frequencies I believe so I  have 
    # not returned the frequency stamps
    #return frequency
    return measurement
    #return ff
    #return dd

'''
#frequency = []
externalLoadSpectra = []
externalLoadSpectra = convertUnitsWithGain('PL_load.prn')

# More tests...
#print frequency
print externalLoadSpectra
print type(externalLoadSpectra)
print len(externalLoadSpectra)
'''