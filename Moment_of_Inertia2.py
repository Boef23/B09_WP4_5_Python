#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio, t_Fs, t_Bs, t_Top, t_Bottom, b
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

def areas_segments(h_Fs, h_Bs, l_Top, l_Bottom, t_Fs, t_Bs, t_Top, t_Bottom):
    area_Fs = h_Fs * t_Fs
    area_Bs = h_Bs * t_Bs
    area_Top = l_Top * t_Top
    area_Bottom = l_Bottom * t_Bottom
    area_Total = area_Fs + area_Bs + area_Top + area_Bottom
    return area_Fs, area_Bs, area_Top, area_Bottom, area_Total

def centroids(area_Fs, area_Bs, area_Top, area_Bottom, area_Total, h_Fs, h_Bs, l_Top, l_Bottom, beta):
    X_Centroid = (area_Fs * l_Top + area_Top * 0.5 * l_Top + area_Bottom * 0.5 * l_Bottom *np.cos(beta))/area_Total
    Y_Centroid = (area_Fs * 0.5 * h_Fs + area_Bs * 0.5 * h_Bs + area_Bottom * (0.5 * l_Bottom * np.sin(beta) + h_Bs))/area_Total
    return X_Centroid, Y_Centroid

def local_Centroids(h_Fs, h_Bs, l_Top, l_Bottom, X_Centroid, Y_Centroid, beta):
    X_Centroid_Fs = l_Top - X_Centroid
    Y_Centroid_Fs = 0.5 * h_Fs - Y_Centroid
    X_Centroid_Top = 0.5 * l_Top - X_Centroid
    Y_Centroid_Top = -Y_Centroid
    X_Centroid_Bs = -X_Centroid
    Y_Centroid_Bs = 0.5 * h_Bs - Y_Centroid
    X_Centroid_Bottom = 0.5 * l_Bottom * np.cos(beta) - X_Centroid
    Y_Centroid_Bottom = h_Bs + 0.5 * l_Bottom *np.sin(beta) - Y_Centroid
    return X_Centroid

def plate_Inertia_X():
    return plate_Inertia_X

def plate_Inertia_Y():
    return plate_Inertia_Y

def stringers_Inertia_X():
    return stringers_Inertia_X

def stringers_Inertia_Y():
    return stringers_Inertia_Y