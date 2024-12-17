from Parameters import *
def enclosedarea(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_wb = 0.5 * chord #Length 
    A_m = ((h_Bs+h_Fs)/2)*l_wb
    return A_m




def Ymaxfinder(z, Y_Centroid):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    t_max_airfoil = 0.12*chord
    h_Fs = 0.1092 * chord #height of front spar
    yskin_fs_atTmax = (t_max_airfoil - h_Fs)/2
    ymaxtop = -(Y_Centroid + yskin_fs_atTmax)
    ymaxbottom = abs(h_Fs - Y_Centroid + yskin_fs_atTmax)
    if ymaxtop >= ymaxbottom:
        return ymaxtop
    else:
        return ymaxbottom

def appliedskinstres(ymax, Ixx, Moment):
    skinstress = (Moment*ymax)/Ixx
    return skinstress