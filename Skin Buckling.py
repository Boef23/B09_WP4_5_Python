from Parameters import *
def enclosedarea(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.0732 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_wb = 0.5 * chord #Length 
    A_m = ((h_Bs+h_Fs)/2)*l_wb
    return A_m




def Ymaxfinder(z, Y_cen):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    y_ref = Y_cen
    t_max_airfoil = 0.12*chord
    