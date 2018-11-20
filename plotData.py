# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:49:18 2018

@author: ilvr2

Test script for plotting data. (Simple)

Tested with 'PL_load.prn' from RAPID containing spectra of external load
"""

def plotData(filename):
    # Importing the functions from frequency stamp and data reading scripts
    from UnitConversion import convertUnits
    from getFrequencyStamps import getFrequencyStamps
    import matplotlib.pyplot as plt

    # Taking data
    externalLoadSpectra = []
    externalLoadSpectra = convertUnits(filename)
    frequency = []
    frequency = getFrequencyStamps(filename)

    '''
    # For testing...
    print externalLoadSpectra
    print frequency
    '''

    # Plotting data and labeling axes
    #          x-axis          y-axis
    plt.plot(frequency, externalLoadSpectra)
    plt.xlabel('Frequency in MHz (ignore the 1e8 ---->)')
    plt.ylabel('Power Spectral Density in W/Hz')
    plt.title('Plot of PSD of External Load in "load" Switch Position')
    plt.show()
 
'''
# Test
plotData('PL_load.prn')
'''