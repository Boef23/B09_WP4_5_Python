#Moment of inertia and torsional stiffness diagrams
#Root parameters
import math
from Parameters import c_Root #Root chord
from Parameters import lambda_LE #Sweep
from Parameters import taper_Ratio #Taper ratio
from Parameters import t_Wb #Wing box skin thickness
h_Fs_Root = 0.1092 * c_Root
h_Bs_Root = 0.0732 * c_Root
l_Top_Root = 0.5 * c_Root
l_Bottom_Root = math.sqrt(l_Top_Root**2 + (h_Fs_Root-h_Bs_Root)**2)

#Centroid location at the root
x_Root = (h_Fs_Root * t_Wb * l_Top_Root + l_Top_Root)