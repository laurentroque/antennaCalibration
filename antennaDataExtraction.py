# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:19:25 2018

@author: ilvr2

The measurements for the antenna are taken at different frequency stamps than 
the other measurements for the RAPID data. This script will plot antenna data 
and get a best fit line in order to extract approximate measurements at the 
deisred frequency stamps that match the rest of the data for calibration
"""

def antennaDataExtraction(filename, comparisonFile):
    import numpy as np
    import matplotlib.pyplot as plt
    from regularGetData import regularGetData
    
    # Importing the PSD data for the antenna with switch in antenna position
    antennaData = []
    antennaData = regularGetData(filename)
    
    # Lists that will be populated with frequency stamps and PSD measurements
    frequencyValues = []
    antennaMeasurements = []
    
    # Polulating the above lists
    for eachFrequency in antennaData:
        frequencyValues.append(eachFrequency[0])
        antennaMeasurements.append(eachFrequency[1])
        
    # plt.plot(frequencyValues, antennaMeasurements)
    
    # Fitting the data with a polynomial
    fittedData = np.polyfit(frequencyValues, antennaMeasurements, 5)
    polynomial = np.poly1d(fittedData)
    polyCurve = polynomial(frequencyValues)
    
    # plt.plot(frequencyValues, polyCurve)
    
    # Extracting fitted measurements from the polynomial at desired frequencies
    comparisonData = []
    comparisonData = regularGetData(comparisonFile)
    
    # Populating a list of only frequencies
    correctedFreq = []
    for eachFrequency in comparisonData:
        correctedFreq.append(eachFrequency[0])
    
    # This is a list of approximate measurements at corrected frequencies
    newData = []
    for eachFrequency in correctedFreq:
        newData.append([eachFrequency, polynomial(eachFrequency)])
    
    '''
    # List of only the measurements for plotting's sake
    measurements = []
    for eachFrequency in newData:
        measurements.append(eachFrequency[1])

    
    plt.plot(correctedFreq, measurements)
    plt.show()   
    '''
    
    return newData
    
filename = 'PA_antenna.prn'
comparisonFile = 'PA_cab_open.prn'
data = antennaDataExtraction('%s' %filename, '%s' %comparisonFile)
