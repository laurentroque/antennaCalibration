# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:49:18 2018

@author: ilvr2

Test script for plotting data. (Simple)

Tested with 'PL_load.prn' from RAPID containing spectra of external load
"""

def plotData(filename):
    # Importing the functions from frequency stamp and data reading scripts
    from regularGetData import regularGetData
    import matplotlib.pyplot as plt

    # Taking data
    dataLines = regularGetData('PL_load.prn')
    frequency = []
    measurement = []
    for i in range(len(dataLines)):
        frequency.append(dataLines[i][0])
        
        # Converting Hz to Mhz
        frequency[i] = (frequency[i] / 1000000)
        measurement.append(dataLines[i][1])

    '''
    # For testing...
    print measurement
    print
    print frequency
    '''

    # Plotting data and labeling axes
    #          x-axis      y-axis
    plt.plot(frequency, measurement)
    plt.xlabel('Frequency in MHz')
    plt.ylabel('Power Spectral Density in W/Hz')
    plt.title('Plot of PSD of External Load in "load" Switch Position')
    plt.show()
 
#'''
# Test
plotData('PL_load.prn')
#'''