# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:54:35 2018

@author: ilvr2

This script is the FIRST STEP OF CALIBRATION
It takes the initial PSD measurements and evaluates them in to an uncalibrated
temperature via Equation (1) from Monsalve arXiv:1602.08065v3

It returns a list that contains frequency stamps and uncalibrated temperature
measurements

Function takes three arguments as strings that are the .prn file names:
    1) PSD of calibration standard while switch is in antenna position 
    2) PSD of calibration standard while switch is in the load position
    3) PSD of calibration standard while switch is in the load+noise source 
       position


This needs to be run on all the calibration standards
    Measurements of the antenna
    Measurements of the ambient load
    Measurements of the hot load/noisy load
    Measurements of the open cable
    Measurements of the shorted cable
    
Script is tested with RAPID data 'PA_antenna.prn', 'PL_antenna.prn', 
'PNS_antenna.prn' commented out below
"""

def getUncalTemps(antData, loadData, noiseData):
    # Realistic assumption for the noise temperature of the load
    # This is set to 300K in the EDGES calibration and 296.15 in RAPID calibration
    T_L = 296.15
    # Realistic assumption for the noise temperature of the noise source
    # This is set to 350K in the EDGES calibration
    T_NS = T_L + 50
    # PSD of open cable when switch is in antenna position (in dBm)
    # This is for reference frequencies
    openCabAntData = 'PA_cab_open.prn'


    from regularGetData import regularGetData
    from antennaDataExtraction import antennaDataExtraction
    from convertUnitsV2 import convertUnits


    '''
    ---------------------STEP 1------------------------
    Import the Power Spectral Density (PSD) of the antenna in the antenna 
    position, load position, and load + noise source position
    '''
    # This will be the measurements of the antenna in the antenna positon
    antennaPositionData = []

    # Measurements of antenna in the load position
    loadPositionData = []

    # Meausements of antenna in load plus noise source postion
    noiseSourcePositionData = []

    # Populate the lists with frequency stamps and measurements
    antennaPositionData = antennaDataExtraction('%s' %antData, '%s' %openCabAntData)
    loadPositionData = regularGetData('%s' %loadData)
    noiseSourcePositionData = regularGetData('%s' %noiseData)

    # We need to convert all of the measurements from dBm/Hz to W/Hz
    convertUnits(antennaPositionData)
    convertUnits(loadPositionData)
    convertUnits(noiseSourcePositionData)

    '''
    ---------------------STEP 2---------------------
    Formulate the equation for the uncalibrateed temperature spectra from Monsalve
    Equation (1) arXiv:1602.08065v3
    '''
    # Just taking the frequencies to append to a list
    # There is probably a way to do this more consicely rather than to keep 
    # reading the frequencies from one list and appending them to another list but
    # I'll do that once I have a handle the calibration procedue ;)
    frequencyStamps = []
    for frequencies in antennaPositionData:
        frequencyStamps.append(frequencies[0])
    
    # Taking the PSD measurements and plugging them into Equation (1)
    uncalibratedTemps = []

    for measurements in range(0, len(antennaPositionData)):
        top = antennaPositionData[measurements][1] - loadPositionData[measurements][1]
        bottom = noiseSourcePositionData[measurements][1] - loadPositionData[measurements][1]
        quotient = top / bottom
    
        T_antStar = (T_NS * quotient) + T_L
    
        uncalibratedTemps.append(T_antStar)
    
    uncalibratedTemperatureData = []
    for points in range(0, len(uncalibratedTemps)):
        uncalibratedTemperatureData.append([frequencyStamps[points], uncalibratedTemps[points]])

    return uncalibratedTemperatureData

'''
FOR TESTING
# PSD of antenna when switch is in antenna position (in dBm)
antData = 'PA_antenna.prn'
# PSD of antenna when switch is in load position (in dBm)
loadData = 'PL_antenna.prn'
# PSD of antenna when switch is in noise source position (in dBm)
noiseData = 'PNS_antenna.prn'
'''
#uncalibratedTemperatureData = getUncalTemps('PA_antenna.prn', 'PL_antenna.prn', 'PNS_antenna.prn')
#print uncalibratedTemperatureData