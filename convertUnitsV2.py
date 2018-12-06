# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:19:07 2018

@author: ilvr2

This is the second iteration of unit conversion. This is to be used on a list
of data that has already been imported to the calibration script. I am 
uncertain whether it is better to convert from dBm to Watts upon importing the
data an then appending to a list or to import the data to a list first and then
convert the units.
"""

def convertUnits(listOfData):
    npts = len(listOfData)
    
    # Converting units to Watts. Formula taken from "readpower.m" by Dr. Nima 
    # Razavi-Ghods included as part of the RAPID collaboration
    for i in range (0, npts):
        listOfData[i][1] = 10.00** ((listOfData[i][1] - 30.00) / 10.0)
        
