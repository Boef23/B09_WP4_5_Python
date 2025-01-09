from Parameters import *
from ShearDiagram import zAxis
import numpy as np

density_AL = 2780 #kg/m^3
span = 30.65 #m
Str_Area = a_Str * t_Str_a + b_Str * t_Str_b #m^2
rib_Distances = [0.60, 0.63, 0.65, 0.68, 0.72, 0.76, 0.81, 0.86, 0.94, 1.04, 1.17, 1.38, 1.78, 3.28]
rib_Placement_RtT = np.array([0.00, 0.60, 1.23, 1.88, 2.56, 3.28, 4.04, 
                            4.84, 5.71, 6.65, 7.68, 8.86, 10.24, 12.02, 15.30]) #Root to tip
rib_Placement_TtR = rib_Placement_RtT[::-1]  #Tip to root
n_Str_Top_incr = [n_Str_Top_ztip, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0]

def calculateWeightstringers(n_Str_incr):
    lengthstringer = 0
    Mass_stringers = 0
    for j in range(len(n_Str_incr)):
        Mass_one_stringer = 0
        lengthstringer = rib_Placement_TtR[j]
        volumestringer = lengthstringer*Str_Area
        Mass_one_stringer = volumestringer*n_Str_incr[j]*density_AL
        Mass_stringers += Mass_one_stringer
    return Mass_stringers

def calculateWeightplates(zAxis, t_Fs = t_Fs, t_Bs = t_Bs, t_Top = t_Top, t_Bottom = t_Bottom):
    chord = c_Root - c_Root*(1-taper_Ratio) * (zAxis/(0.5 * span))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5 * chord #length of bottom flange
    areaplates = h_Fs*t_Fs + h_Bs*t_Bs + l_Top*t_Top + l_Bottom*t_Bottom
    volumelist = 0.01*areaplates
    masslist = volumelist*density_AL
    massplates = np.sum(masslist)
    return massplates

Mass_WB = calculateWeightplates(zAxis) + calculateWeightstringers(n_Str_Top_incr) + calculateWeightstringers(n_Str_Bottom_incr)
print(f'This is the weight of the WB {Mass_WB} kg of half span')