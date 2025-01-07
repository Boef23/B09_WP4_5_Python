from Moment_of_Inertia2 import geometry, areas_segments
from ShearDiagram import zAxis, totalMomentDist, totalShearDist, totalTorqueDist
from LiftDistribution import chord
import numpy as np
from Skin_Buckling import enclosedarea, Ymaxfinder
from Parameters import t_Fs
from Moment_of_inertia_3 import *
from New_Iyy import *

momentOfInertia_X = Ixx_list
momentOfInertia_y = I_yy_Total
momentOfInertia_J = momentOfInertia_X * momentOfInertia_y 

def geometry(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5 * chord #length of bottom flange
    beta = np.arctan((h_Fs-h_Bs)/l_Top) #angle of bottom flange
    return h_Fs, h_Bs, l_Top, l_Bottom, beta

#Coefficients
kv = 1.5

#Spar geometry
geo = geometry(zAxis)
area = areas_segments(geo[0], geo[1], geo[2], geo[3])
sparArea = area[0] + area[1]

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
Ixx = geometryproperties(zAxis)[0]
y_max_top = Ymaxfinder(zAxis, calculate_Centroid_wingbox(zAxis)[1])[1]
normalStress = totalMomentDist * y_max_top / Ixx

print(tau_max)
