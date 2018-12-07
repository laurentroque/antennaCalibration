# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:52:32 2018

@author: ilvr2

This script deals with the maths for complex numbers needed to build Equation 
(7) from Monsalve arXiv:1602.08065v3

It will import antenna and receiver S11's and calculate the F parameter from
Equation (3) and the phase from Equation (4)
The script will then calculate the complex values used in Equation (7) needed
to determine the coefficients C1, C2, T_unc, T_cos, and T_sin.
"""

import math
import cmath
import numpy as np
from getMatrixData import getMatrixData

receiverS11 = getMatrixData('rapidcal_rec_sparam_s11.s2p', 'PA_cab_open.prn')
antennaS11 = getMatrixData('rapidcal_antenna_s11.s1p', 'PA_cab_open.prn')

# Lists for the complex reflection coefficients of the receiver and the antenna
recReflec = []
antReflec = []

# Lists for the modulus of the receiver and antenna S11's
modRecS11 = []
modAntS11 = []

# We need the antenna reflection coefficients and the receiver refelection 
# coefficients multipled toegether at each frequency stamp to build Eqn (3)
gammaAntGammaRec = []

# Populating the lists
# Receiver reflection coefficients
for frequencies in receiverS11:
    recReflec.append(frequencies[1])
    
# Antenna reflection coefficents
for frequencies in antennaS11:    
    antReflec.append(frequencies[1])
    
for i in range(0, len(recReflec)):
    product = np.multiply(recReflec[i], antReflec[i])
    # Complex reflection coefficent products
    gammaAntGammaRec.append(product)
    
    # Lists of modulus of receiver and antenna reflection coefficients
    modRecS11.append(np.absolute(recReflec[i]))
    modAntS11.append(np.absolute(antReflec[i]))    

'''
-------------STEP 1-------------
Building the F parameter from Equation (3)
'''
# Tops and bottoms of an eventual quotient
top = []
bottom = []

# Populating a list of tops for the quotients
for i in range(0, len(modRecS11)):
    n = math.sqrt(1 - ((modRecS11[i]) ** 2))
    top.append(n)

# List for the bottoms of the quotients
for i in range(0, len(gammaAntGammaRec)):
    m = 1 - gammaAntGammaRec[i]
    bottom.append(m)

# Building F Equation (3)    
F = []

for i in range(0, len(top)):
    # Building the quotient
    quotient = top[i] / bottom[i]
    # Appending values to F
    F.append([receiverS11[i][0], quotient])
    
'''
-------------STEP 2-------------
Building the ALPHA from Equation (4)

In the electronics setup, noise is produced when the signal is reflected by the 
LNA imput toward the antenna. This refelction is due to imperfect impedance 
match an re-enters the receiver with phase ALPHA
'''
ALPHA = []
for i in range(0, len(F)):
    # Multiplying F with the correspinding antenna reflection coefficient
    prod = antReflec[i] * F[i][1]
    # Taking the complex argument
    prod = cmath.phase(prod)
    # Appending to ALPHA
    ALPHA.append([F[i][0], prod])
    
'''
-------------STEP 3-------------
This will do the complex mathematics on the right side of Equation (7). It 
builds the quotients that are in the square brackets.

We start for the maths in the brackets following the calibrated temperature
spectra T_ant
'''
# We need the modulus of F
modF = []
for i in range(0, len(F)):
    modulus = np.absolute(F[i][1])
    modF.append([F[i][0], modulus])

# Clearing the top and bottom lists for the next quotient    
top[:] = []
bottom[:] = []

# Populating the tops of the quotients
for i in range(0, len(modF)):
    l = (modAntS11[i]) ** 2
    l = 1 - l
    l = l * ((modF[i][1]) ** 2)
    top.append(l)

# And the bottoms 
for i in range(0, len(modRecS11)):
    o = modRecS11[i]
    o = o ** 2
    o = 1 - o
    bottom.append(o)

# taking the quotients and appending them to a list
mathsForT_ant = []
for i in range(0, len(top)):
    quotient = top[i] / bottom[i]
    mathsForT_ant.append([F[i][0], quotient])

'''
-------------STEP 4-------------
We move on to the maths in the brackets following the uncorrelated spectra
T_unc
'''

# Clearing the top list for the next quotient. Bottom stays the same
top[:] = []

# Re-populating the tops
for i in range(0, len(modF)):
    a = (modAntS11[i]) ** 2
    b = (modF[i][1]) ** 2
    c = a * b
    top.append(c)

# taking the quotients and appending them to a list
mathsForT_unc = []
for i in range(0, len(top)):
    quotient = top[i] / bottom[i]
    mathsForT_unc.append([F[i][0], quotient])
    
'''
-------------STEP 5-------------
Maths for in the brackets following the correlated cosine temperatures T_cos

THIS IS ASSUMED TO BE IN RADIANS BUT I AM NOT 100% SURE !!!!!!!!!!!!!!!!!!!!!!!
'''
# Clearing the top list again.
top[:] = []

# We now need a cosine of all the ALPHAS
cosALPHA = []
for i in range(0, len(ALPHA)): 
    d = math.cos(ALPHA[i][1])
    cosALPHA.append(d)

# Tops       
for i in range(0, len(modF)):
    a = modAntS11[i]
    b = modF[i][1]
    c = a * b
    top.append(c) 

# Taking the quotients, multiplying by cos(ALPHA) and appending to list
mathsForT_cos = []
for i in range(0, len(top)):
    quotient = quotient = top[i] / bottom[i]
    a = quotient * cosALPHA[i]
    mathsForT_cos.append([F[i][0], a])

'''
-------------STEP 6-------------
Maths for in the brackets following the correlated sine temperatures T_sin

THIS ALSO IS ASSUMED TO BE IN RADIANS BUT I AM NOT 100% SURE !!!!!!!!!!!!!!!!!!
'''
# Top and bottom of quotient stays the same

# We now need the sine of all the ALPHA's
sinALPHA = []
for i in range(0, len(ALPHA)): 
    d = math.sin(ALPHA[i][1])
    sinALPHA.append(d)
    
# Taking the quotient and multiplying by sin(ALPHA) then appending to list
mathsForT_sin = []
for i in range(0, len(top)):
    quotient = quotient = top[i] / bottom[i]
    a = quotient * sinALPHA[i]
    mathsForT_sin.append([F[i][0], a])
    
print mathsForT_sin
