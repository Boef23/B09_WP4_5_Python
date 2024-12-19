from Parameters import *
from LiftDistribution import chord
from ShearDiagram import zAxis
from ColumnBuckling import distanceArray
import numpy as np

#Chord
h_Fs, h_Bs, l_Top, l_Bottom = geometry(zAxis)

#
rib_Placement_RtT = np.array([0.00, 0.60, 1.23, 1.88, 2.56, 3.28, 4.04, 
                            4.84, 5.71, 6.65, 7.68, 8.86, 10.24, 12.02, 15.30]) #Root to tip
rib_Placement_TtR = rib_Placement_RtT[::-1]  #Tip to root


#Stringer local calculations
Str_Area = a_Str * t_Str_a + b_Str * t_Str_b
x_Bar_Str = b_Str**2 / (2 * (a_Str + b_Str))    #Centroid x from bottom left as seen -> L

I_yy_Stringer = t_Str_b * b_Str**3 / 12 + a_Str * t_Str_a * x_Bar_Str**2 + b_Str * t_Str_b * (x_Bar_Str - b_Str/2)**2

#Plates 
I_yy_Top_Plate = t_Top * (l_Top)**3 / 12            #Array
I_yy_Bottom_Plate = t_Bottom * (l_Bottom)**3 / 12   #Array

#Parallel Axis Theorem
I_yy_Fs = h_Fs * t_Fs * (l_Top / 2)**2      #Array
I_yy_Bs = h_Bs * t_Bs * (l_Bottom / 2)**2   #Array

#stringers shit
rib_Chords = np.array([])
for item in rib_Placement_TtR:
    rib_Chords = np.append(rib_Chords, [chord(item)])

n_Str_Top = n_Str_Top_ztip
for item in rib_Chords:
    if 
