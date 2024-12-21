from Parameters import *
from LiftDistribution import chord
from ShearDiagram import zAxis
import numpy as np

#Chord
h_Fs, h_Bs, l_Top, l_Bottom = geometry(zAxis)

#Rib placement semi span wise position, [m]
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

#stringers contribution
#Obtain chord at rib positions
rib_Chords = np.array([])
for item in rib_Placement_TtR:
    rib_Chords = np.append(rib_Chords, [0.5 * chord(item)])

rib_Chords = rib_Chords[0:-1:1]

#Determine whether amount of stringers is even or odd and set a starting distance from the centroid
n_Str_Top = n_Str_Top_incr[0]
if n_Str_Top % 2 == 1:
    dist_Top = delta_Top
else:
    dist_Top = delta_Top / 2

n_Str_Bot = n_Str_Bottom_incr[0]
if n_Str_Bot % 2 == 1:
    dist_Bot = delta_Bottom
else:
    dist_Bot = delta_Bottom / 2

#Make an array for stringer contribrution in each bay
I_yy_Top_Str = np.array([])
n_Str_Top = 0

I_yy_Bot_Str = np.array([])
n_Str_Bot = 0

#Top stringers
for i in range(np.size(rib_Chords)): 
    n_Str_Top += n_Str_Top_incr[i]

    #Add local stringer contribution
    add_Iyy_Str_Top = n_Str_Top * I_yy_Stringer

    #Add parallel axis contribution
    if n_Str_Top % 2 == 1:
        for j in range(int((n_Str_Top - 1)/2)):
            x = delta_Top * (j + 1)

            #Check for stringer fitting
            if 2 * x + delta_Top > rib_Chords[i]:
                print(f'There are too many top stringers in bay {i+1} from the tip')
                break

            add_Iyy_Str_Top += 2 * Str_Area * x**2

    else:
        for j in range(int(n_Str_Top/2)):
            x = dist_Top + delta_Top * j

            #Check for stringer fitting
            if 2 * x + delta_Top > rib_Chords[i]:
                print(f'There are too many top stringers in bay {i+1} from the tip')
                break

            add_Iyy_Str_Top += 2 * Str_Area * x**2

    I_yy_Top_Str = np.append(I_yy_Top_Str, [add_Iyy_Str_Top])


#Bottom stringers
for i in range(np.size(rib_Chords)): 
    n_Str_Bot += n_Str_Bottom_incr[i]

    #Add local stringer contribution
    add_Iyy_Str_Bot = n_Str_Bot * I_yy_Stringer

    #Add parallel axis contribution
    if n_Str_Bot % 2 == 1:
        for j in range(int((n_Str_Bot - 1)/2)):
            x = delta_Bottom * (j + 1)

            #Check for stringer fitting
            if 2 * x + delta_Bottom > rib_Chords[i]:
                print(f'There are too many bottom stringers in bay {i+1} from the tip')
                break

            add_Iyy_Str_Bot += 2 * Str_Area * x**2

    else:
        for j in range(int(n_Str_Bot/2)):
            x = dist_Bot + delta_Bottom * j

            #Check for stringer fitting
            if 2 * x + delta_Bottom > rib_Chords[i]:
                print(f'There are too many bottom stringers in bay {i+1} from the tip')
                break

            add_Iyy_Str_Bot += 2 * Str_Area * x**2

    I_yy_Bot_Str = np.append(I_yy_Bot_Str, [add_Iyy_Str_Bot])


#Total stringer contribution per bay
I_yy_Total_Str = I_yy_Top_Str + I_yy_Bot_Str

