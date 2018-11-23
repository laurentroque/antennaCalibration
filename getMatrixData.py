# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:04:31 2018

@author: ilvr2

This program is used to get calibration data that is stored in a matrix such as
S11's S22's etc. Each calibration parameter will be stored in a 2D matrix with
its corresponding frequency stamp.

**This function will not work on two column data such as Power Spectral Denstiy
readings. 

This script is tested using RAPID calibration data 'rapidcal_cab_open_s11.s2p'

Code makes use of scikit-rf, an open-source Python package for RF and Microwave 
applications.

scikit-rf found here: http://scikit-rf.org/index.html#
                      https://scikit-rf.readthedocs.io/en/latest/index.html
"""

# Basic skrf packages
import skrf as rf
from pylab import *
from skrf import Network, Frequency
# For plotting
from matplotlib import pyplot as plt
# For arithmetic operations
from skrf.data import wr2p2_short as short
from skrf.data import wr2p2_delayshort as delayshort
# Optional for interpolation and concatenation
from skrf.data import wr2p2_line1 as line1
# For use with complex arithmetic
import math
import cmath

# calling function to get regular two-column calibration data
from regularGetData import regularGetData

# Variables for matrix data and calibration measurements for comparison
S11Data = []
S21Data = []
S12Data = []
S22Data = []
frequency = []

# Variables for frequency stamps
frequencyStampOfLoadedData = 0
frequencyStampOfmatrixData = 0

# Insert the name/location of the matrix data you want to retrieve and one of 
# the PSD data that corresponds to the matrix recordings
def getMatrixData(matrixFilename, frequencyFilename):
    frequency = regularGetData(frequencyFilename)
    matrixData = Network(matrixFilename)
    
    # Frequency data of a spectral density measurement set and the matrix 
    # measurements are matched here because some matrix measurements were taken 
    # at frequency points where not taken for the spectral measurements and 
    # so we cannot build a sky model for those points without complete data
    
    for i in range(0, len(matrixData)):
        if matrixData.f[i] == frequency[i][0]:
            S11Data.append([matrixData.f[i], matrixData.s[i, 0, 0]])
            S21Data.append([matrixData.f[i], matrixData.s[i, 1, 0]])
            S12Data.append([matrixData.f[i], matrixData.s[i, 0, 1]])
            S22Data.append([matrixData.f[i], matrixData.s[i, 1, 1]])

'''
# Tests
getMatrixData('rapidcal_cab_open_s11.s2p', 'PA_antenna.prn')
print len(S22Data)
print "S11's", S22Data
''' 
    
        
    
    
    
    

