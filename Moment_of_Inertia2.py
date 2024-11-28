#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio, t_Wb, b
import numpy as np


#Chord length as function of spanwise position
def geometry(c_Root, taper_Ratio, b, z):
    chord = c_Root - c_Root*(1-taper_Ratio)* (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5013 * chord #length of bottom flange
    beta = np.atan((h_Fs-h_Bs)/l_Top) #angle of bottom flange
    return h_Fs, h_Bs, l_Top, l_Bottom, beta

def centroids(h_Fs, h_Bs, l_Top, l_Bottom, beta, t_Wb):
    X_Centroid = (h_Fs*t_Wb*l_Top + l_Top*t_Wb*0.5*l_Top + l_Bottom*t_Wb*0.5*l_Bottom*np.cos(beta))/((h_Fs+l_Top+h_Bs+l_Bottom)*t_Wb)
    Y_Centroid = (h_Fs*t_Wb*0.5*h_Fs + h_Bs*t_Wb*0.5*h_Bs + l_Bottom*t_Wb*(0.5*l_Bottom*np.sin(beta)+h_Bs))/((h_Fs+l_Top+h_Bs+l_Bottom)*t_Wb)
    return X_Centroid, Y_Centroid

def plate_Inertia_X():
    return plate_Inertia_X

def plate_Inertia_Y():
    return plate_Inertia_Y

def stringers_Inertia_X():
    return stringers_Inertia_X

def stringers_Inertia_Y():
    return stringers_Inertia_Y