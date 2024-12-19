from Parameters import *
from LiftDistribution import chord
from ShearDiagram import zAxis

#Chord
chords = chord(zAxis)

#Parameters
a_Str = 1   #long length stringer
b_Str = 1   #short length stringer

Str_Area = a_Str * t_str_a + b_Str * t_str_b

#stringer xbar calc
x_Bar_Str = b_Str**2 / (2 * (a_Str + b_Str))

#Stringer Iyy calc
I_yy_Stringer = t_str_b * b_Str**3 / 12 + a_Str * t_str_a * x_Bar_Str**2 + b_Str * t_str_b * (x_Bar_Str - b_Str/2)**2

#General 
I_yy_Top_Plate = t_Top * (0.5 * chords)**3 / 12
I_yy_Bottom_Plate = t_Bottom * (0.5 * chords)**3 / 12

#Steiner Theorem
I_yy_Fs = 


