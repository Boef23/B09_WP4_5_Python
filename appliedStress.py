from Moment_of_Inertia2 import geometry, areas_segments
from ShearDiagram import zAxis, totalMomentDist, totalShearDist, totalTorqueDist
from LiftDistribution import chord
import numpy as np
from Skin_Buckling import enclosedarea, Ymaxfinder
from Parameters import t_Fs
from Moment_of_inertia_3 import *
from New_Iyy import *
import matplotlib.pyplot as plt

momentOfInertia_X = Ixx_list
momentOfInertia_y = I_yy_Total
momentOfInertia_J = momentOfInertia_X + momentOfInertia_y 

def geometry(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5 * chord #length of bottom flange
    return h_Fs, h_Bs, l_Top, l_Bottom


def areas_segments(h_Fs, h_Bs, l_Top, l_Bottom):
    area_Fs = h_Fs * t_Fs #Area front spar
    area_Bs = h_Bs * t_Bs #Area back spar
    area_Top = l_Top * t_Top #Area top plate
    area_Bottom = l_Bottom * t_Bottom #Area bottom plate
    area_Total = area_Fs + area_Bs + area_Top + area_Bottom #Total area
    return area_Fs, area_Bs, area_Top, area_Bottom, area_Total

 
#Coefficients
kv = 1.8

#Spar geometry
h_Fs, h_Bs, l_Top, l_Bottom = geometry(zAxis)
area = areas_segments(h_Fs, h_Bs, l_Top, l_Bottom)
sparArea = area[0] + area[1]

#print(sparArea)

#Shear force stresses
tau_avg = totalShearDist / sparArea
tau_max_force = kv * tau_avg

#Torque shear stresses
enclosedArea = enclosedarea(zAxis)
shearFlow = totalTorqueDist / (2 * enclosedArea)
tau_torque = shearFlow / t_Fs

#Total max shear stress
tau_max = tau_max_force + tau_torque


#Normal stress
Ixx = momentOfInertia_X
y_max_top = Ymaxfinder(zAxis, calculate_Centroid_wingbox(zAxis)[1])[0]
normalStress = totalMomentDist * y_max_top / Ixx

#Tensile Stress
y_max_bot = Ymaxfinder(zAxis, calculate_Centroid_wingbox(zAxis)[1])[1]
tensileStress = totalMomentDist * y_max_bot / Ixx * 10**-6  #MPa

maxTensile = np.ones_like(zAxis) * 450
tensileMoS = maxTensile / tensileStress

if __name__ == '__main__':
    plt.plot(zAxis, tensileMoS)
    plt.title('Tensile Strength Safety')
    plt.xlabel('z [m]')
    plt.ylabel('Margin of Safety [-]')
    plt.show()

#print(tau_max)
