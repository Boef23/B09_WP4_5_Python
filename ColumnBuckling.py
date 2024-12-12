"""Column Buckling"""
#creates an equation for columb buckling
#becomes and equation with respect to z, and is then plotted to show the critical stress

import numpy as np
import scipy as sp
from Parameters import l_Stringer, t_Stringer
from Moment_of_inertia_comp import I_XX_Zlist, zlist

elasticModulus = 72.4 * 10**9 # Pa
K = 4 #due to ribs, two sides are clamped
L = 1 #this is thus a fill in value, it has not been decided where the ribs go, so the stringer length is unkown. 
distanceList = []

def distanceArray():
    distance = 0
    for i in zlist:
        distanceList.append(distanceList)

print(len(zlist))
values = np.array([0.00, 0.60, 1.23, 1.88, 2.56, 3.28, 4.04, 
                   4.84, 5.71, 6.65, 7.68, 8.86, 10.24, 12.02, 15.30])



def stringerArea():
    return t_Stringer * l_Stringer

def columnBuckling():
    sigmaCritical = K * np.pi**2 * elasticModulus * I_XX_Zlist / (L**2 * stringerArea())
    return sigmaCritical

print(f'Total Deflection at tip is: {columnBuckling()} Pa' ) #prints the deflection, takes a lot of time to compute