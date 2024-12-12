from Moment_of_Inertia2 import geometry, areas_segments
from ShearDiagram import zAxis, totalMomentDist, totalShearDist
from LiftDistribution import chord
import numpy as np
from Moment_of_inertia_comp import geometryproperties

#Coefficients
kv = 1.5

#Spar geometry
geo = geometry(zAxis)
area = areas_segments(geo[0], geo[1], geo[2], geo[3])
sparArea = area[0] + area[1]

#Shear stresses
tau_avg = totalShearDist / sparArea
tau_max = kv * tau_avg

#Normal stress
Ixx = geometryproperties(zAxis)[0]
y = -0.06 * chord(zAxis)
normalStress = totalMomentDist * y / Ixx

print(normalStress)

