#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio, t_Wb
import numpy as np


#Chord length as function of spanwise position
def centroids(c_Root, taper_Ratio, t_Wb):
    list_X_Centroids = []
    list_Y_Centroids = []
    for i in range(1,1000000):
        chord = c_Root - c_Root*(1-taper_Ratio)*(i/1000000)
        h_Fs = 0.1092 * chord #height of front spar
        h_Bs = 0.0732 * chord #height of back spar
        l_Top = 0.5 * chord #length op top flange
        l_Bottom = 0.5013 * chord #length of bottom flange
        beta = np.atan((h_Fs-h_Bs)/l_Top) #angle of bottom flange
        X_Centroid = (h_Fs*t_Wb*l_Top + l_Top*t_Wb*0.5*l_Top + l_Bottom*t_Wb*0.5*l_Bottom*np.cos(beta))/((h_Fs+l_Top+h_Bs+l_Bottom)*t_Wb)
        list_X_Centroids.append(X_Centroid)
        Y_Centroid = (h_Fs*t_Wb*0.5*h_Fs + h_Bs*t_Wb*0.5*h_Bs + l_Bottom*t_Wb*(0.5*l_Bottom*np.sin(beta)+h_Bs))/((h_Fs+l_Top+h_Bs+l_Bottom)*t_Wb)
        list_Y_Centroids.append(Y_Centroid)
    return list_X_Centroids, list_Y_Centroids