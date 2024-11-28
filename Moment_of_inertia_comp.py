from Moment_of_Inertia2 import *

#create final function as a function of (z)]
def geometryproperties(z):
    h_Fs, h_Bs, l_Top, l_Bottom, beta = geometry(z)
    area_Fs, area_Bs, area_Top, area_Bottom, area_Total = areas_segments(h_Fs, h_Bs, l_Top, l_Bottom)
    area_stringer = area_stringer()
    return I_XX_Wb, I_YY_wb, J_Wb


