from Moment_of_Inertia2 import geometry, areas_segments
from ShearDiagram import zAxis, totalMomentDist, totalShearDist, totalTorqueDist
from LiftDistribution import chord
import numpy as np
from Moment_of_inertia_comp import geometryproperties
from Skin_Buckling import enclosedarea, Ymaxfinder
from Parameters import t_Fs
from Moment_of_inertia_3 import *

#Coefficients
kv = 1.8

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
y_max_top = Ymaxfinder(zAxis, calculate_Centroid(zAxis)[1])[1]
normalStress = totalMomentDist * y_max_top / Ixx

