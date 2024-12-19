from Parameters import *
from LiftDistribution import chord
from ShearDiagram import zAxis

#Chord
h_Fs, h_Bs, l_Top, l_Bottom = geometry(zAxis)



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


