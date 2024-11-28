from Moment_of_Inertia2 import *

#create final function as a function of (z)]
def geometryproperties(z):
    h_Fs, h_Bs, l_Top, l_Bottom, beta = geometry(z)
    return I_XX_Wb, I_YY_wb, J_Wb


z = 0.01
h_Fs, h_Bs, l_Top, l_Bottom, beta = geometry(z)
print(h_Fs, h_Bs, l_Top, l_Bottom, beta)