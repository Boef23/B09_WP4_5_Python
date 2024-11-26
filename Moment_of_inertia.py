#Moment of inertia and torsional stiffness diagrams
#Root parameters
#Coordinate system first definition: origin at aft top point of wingbox with x to the front and y down, 
#such that the wingbox is in the all positive quadrant.
import math
from Parameters import c_Root #Root chord
from Parameters import lambda_LE #Sweep
from Parameters import taper_Ratio #Taper ratio
from Parameters import t_Wb #Wing box skin thickness
from Parameters import b #Wing span
from Parameters import lambda_Dihedral #dihedral angle
#Definitions of lengths
h_Fs_Root = 0.1092 * c_Root
h_Bs_Root = 0.0732 * c_Root
l_Top_Root = 0.5 * c_Root
l_Bottom_Root = math.sqrt(l_Top_Root**2 + (h_Fs_Root-h_Bs_Root)**2)
beta_Root = math.atan((h_Bs_Root-h_Fs_Root)/l_Top_Root)
z = 0
#Centroid location at the root
x_Root = (h_Fs_Root * t_Wb * l_Top_Root + l_Top_Root * t_Wb * 0.5 * l_Top_Root + l_Bottom_Root * t_Wb * 0.5 * l_Bottom_Root * math.cos(beta_Root))/(h_Fs_Root * t_Wb + l_Top_Root * t_Wb + h_Bs_Root * t_Wb + l_Bottom_Root * t_Wb)
y_Root = (h_Fs_Root * t_Wb * 0.5 * h_Fs_Root + h_Bs_Root * t_Wb * 0.5 * h_Bs_Root + l_Bottom_Root * t_Wb * (0.5 * l_Bottom_Root * math.sin(beta_Root) + h_Bs_Root))/(h_Fs_Root * t_Wb + l_Top_Root * t_Wb + h_Bs_Root * t_Wb + l_Bottom_Root * t_Wb)

#Centroid location at spanwise position (function of z)
#z between 0 and b/2, then symmetric for other half wing
#Put into loop to evaluate for every spanwise position.
x_Local = x_Root - z * (math.tan(lambda_LE) - (1 - 0.3 * c_Root - x_Root) * ((2 * c_Root) / b) * (1 - taper_Ratio))
y_Local = y_Root - (z / (0.5 * b)) * math.tan(lambda_Dihedral)

#Definitions of positions root
x_AB_Root = l_Top_Root - x_Root
y_AB_Root = 0.5 * h_Fs_Root - y_Root
x_BC_Root = 0.5 * l_Top_Root - x_Root
y_BC_Root= -y_Root
x_CD_Root = - x_Root
y_CD_Root = 0.5 * h_Bs_Root - y_Root
x_AD_Root = 0.5 * l_Bottom_Root * math.cos(beta_Root) - x_Root
y_AD_Root = h_Bs_Root + 0.5 * l_Bottom_Root * math.sin(beta_Root) - y_Root

#Moment of inertia about x-axis per side for root 
I_xx_AB_Root = (t_Wb * h_Fs_Root ** 3)/12 + t_Wb * h_Fs_Root * y_AB_Root ** 2
I_xx_BC_Root = (l_Top_Root * t_Wb ** 3)/12 + t_Wb * l_Top_Root * y_BC_Root ** 2
I_xx_CD_Root = (t_Wb * h_Bs_Root ** 3)/12 + t_Wb * l_Top_Root * y_CD_Root ** 2
I_xx_AD_Root = (t_Wb * l_Bottom_Root ** 3 * (math.sin(beta_Root)) ** 2)/12 + t_Wb * l_Bottom_Root * y_AD_Root ** 2
I_yy_AB_Root = (h_Fs_Root * t_Wb ** 3)/12 + t_Wb * h_Fs_Root * x_AB_Root ** 2
I_yy_BC_Root = (t_Wb * l_Top_Root ** 3)/12 + t_Wb * l_Top_Root * x_BC_Root ** 2
I_yy_CD_Root = (h_Bs_Root * t_Wb ** 3)/12 + t_Wb * h_Bs_Root * x_CD_Root ** 2
I_yy_AD_Root = (t_Wb * l_Bottom_Root ** 3 * (math.cos(beta_Root)) ** 2)/12 + t_Wb * l_Bottom_Root * x_AD_Root ** 2