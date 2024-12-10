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

def stringerArea():
    return t_Stringer * l_Stringer

def columnBuckling():
    sigmaCritical = K * np.pi**2 * elasticModulus * I_XX_Zlist / (L**2 * stringerArea())
    return sigmaCritical

print(f'Total Deflection at tip is: {columnBuckling()} Pa' ) #prints the deflection, takes a lot of time to compute