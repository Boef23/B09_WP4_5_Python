#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio, t_Fs, t_Bs, t_Top, t_Bottom, b, t_Stringer, l_Stringer, n_str_Fs, n_str_Bs, n_str_Top, n_str_Bottom, w_Stringer, h_Stringer
import numpy as np

#Chord length as function of spanwise position
def geometry(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5 * chord #length of bottom flange
    beta = np.arctan((h_Fs-h_Bs)/l_Top) #angle of bottom flange
    return h_Fs, h_Bs, l_Top, l_Bottom, beta

#Calculates the area of individual segments and the total area
def areas_segments(h_Fs, h_Bs, l_Top, l_Bottom):
    area_Fs = h_Fs * t_Fs #Area front spar
    area_Bs = h_Bs * t_Bs #Area back spar
    area_Top = l_Top * t_Top #Area top plate
    area_Bottom = l_Bottom * t_Bottom #Area bottom plate
    area_Total = area_Fs + area_Bs + area_Top + area_Bottom #Total area
    return area_Fs, area_Bs, area_Top, area_Bottom, area_Total

#Calculates the area of a stringer
def calcarea_stringer():
    area_Stringer = l_Stringer * t_Stringer #Area stringer
    return area_Stringer

#Calculates the location of the centroid w.r.t. datum at the top of the back spar
def centroid(area_Fs, area_Bs, area_Top, area_Bottom, area_Total, h_Fs, h_Bs, l_Top, l_Bottom, beta):
    X_Centroid = (area_Fs * l_Top + area_Top * 0.5 * l_Top + area_Bottom * 0.5 * l_Bottom *np.cos(beta))/area_Total #X-position of the centroid
    Y_Centroid = (area_Fs * 0.5 * h_Fs + area_Bs * 0.5 * h_Bs + area_Bottom * (0.5 * l_Bottom * np.sin(beta) + h_Bs))/area_Total #Y-position of the centroid
    return X_Centroid, Y_Centroid

#Calculates the location of the centroids of individual segments w.r.t the centroid of the total wing box calculated in function centroid
def local_Centroids(h_Fs, h_Bs, l_Top, l_Bottom, beta, X_Centroid, Y_Centroid):
    X_Centroid_Fs = l_Top - X_Centroid #X-position of the centroid of the front spar
    Y_Centroid_Fs = 0.5 * h_Fs - Y_Centroid #Y-position of the centroid of the front spar
    X_Centroid_Top = 0.5 * l_Top - X_Centroid #X-position of the centroid of the top plate
    Y_Centroid_Top = -1 * Y_Centroid #Y-position of the centroid of the top plate
    X_Centroid_Bs = -1 * X_Centroid #X-position of the centroid of the back spar
    Y_Centroid_Bs = 0.5 * h_Bs - Y_Centroid #Y-position of the centroid of the back spar
    X_Centroid_Bottom = 0.5 * l_Bottom * np.cos(beta) - X_Centroid #X-position of the centroid of the bottom plate
    Y_Centroid_Bottom = h_Bs + 0.5 * l_Bottom *np.sin(beta) - Y_Centroid #Y-position of the centroid of the bottom plate
    return X_Centroid_Fs, Y_Centroid_Fs , X_Centroid_Top, Y_Centroid_Top, X_Centroid_Bs, Y_Centroid_Bs, X_Centroid_Bottom, Y_Centroid_Bottom

def plate_Inertia_XX(h_Fs, h_Bs, l_Top, l_Bottom, beta, Y_Centroid_Fs, Y_Centroid_Top, Y_Centroid_Bs, Y_Centroid_Bottom):
    I_XX_Fs = (t_Fs * h_Fs ** 3)/12 + t_Fs * h_Fs * Y_Centroid_Fs ** 2
    I_XX_Top = (l_Top * t_Top ** 3)/12 + t_Top * l_Top * Y_Centroid_Top ** 2 
    I_XX_Bs = (t_Bs * h_Bs **2)/12 + t_Bs * h_Bs * Y_Centroid_Bs ** 2
    I_XX_Bottom = (t_Bottom * l_Bottom ** 3 * (np.sin(beta)) ** 2)/12 + t_Bottom * l_Bottom * Y_Centroid_Bottom ** 2
    I_XX_Total_Plates = I_XX_Fs + I_XX_Top + I_XX_Bs + I_XX_Bottom
    return I_XX_Total_Plates

def plate_Inertia_YY(h_Fs, h_Bs, l_Top, l_Bottom, beta, X_Centroid_Fs, X_Centroid_Top, X_Centroid_Bs, X_Centroid_Bottom):
    I_YY_Fs = (h_Fs * t_Fs ** 3)/12 + t_Fs * h_Fs * X_Centroid_Fs ** 2
    I_YY_Top = (t_Top * l_Top ** 3)/12 + t_Top * l_Top * X_Centroid_Top ** 2
    I_YY_Bs = (h_Bs * t_Bs ** 3)/12 + t_Bs * h_Bs * X_Centroid_Bs ** 2
    I_YY_Bottom = (t_Bottom * l_Bottom ** 3 * (np.cos(beta)) ** 2)/12 + t_Bottom * l_Bottom * X_Centroid_Bottom ** 2
    I_YY_Total_Plates = I_YY_Fs + I_YY_Top + I_YY_Bs + I_YY_Bottom
    return I_YY_Total_Plates

def stringer_Inertia(t_Stringer, w_Stringer, h_Stringer):
    I_Stringer = (w_Stringer * t_Stringer ** 3)/12 + (t_Stringer * h_Stringer ** 3)/12 + t_Stringer * h_Stringer * (h_Stringer/2) ** 2
    return I_Stringer

def Calc_string_space(h_Fs, h_Bs, l_Top, l_Bottom):
    Spacing_Fs = h_Fs/n_str_Fs
    Spacing_Bs = h_Bs/n_str_Bs
    Spacing_Top = l_Top/n_str_Top
    Spacing_Bottom = l_Bottom/n_str_Bottom
    return Spacing_Fs, Spacing_Bs, Spacing_Top, Spacing_Bottom

def stringers_Inertia_X(Y_Centroid, area_Stringer, Spacing_Fs, Spacing_Bs, Spacing_Bottom, Y_Centroid_Top, h_Fs, beta):
    
    I_XX_Fs_tot = 0
    I_XX_Bs_tot = 0
    I_XX_Top_tot = 0
    I_XX_Bottom_tot = 0

    for i in range(n_str_Fs):
        Y_n_stringer_Fs = np.abs(Y_Centroid - (i - 0.5)*Spacing_Fs)
        I_XX_n_Fs = Y_n_stringer_Fs**2 * area_Stringer
        I_XX_Fs_tot += I_XX_n_Fs
    
    for j in range(n_str_Bs):
        Y_n_stringer_Bs = np.abs(Y_Centroid - (j - 0.5)*Spacing_Bs)
        I_XX_n_Bs = Y_n_stringer_Bs**2 * area_Stringer
        I_XX_Bs_tot += I_XX_n_Bs
                            
    I_XX_Top_tot = n_str_Top*area_Stringer*Y_Centroid_Top**2

    for k in range(n_str_Bottom):
        Y_n_stringer_Top = np.abs(Y_Centroid-h_Fs-(k-0.5)*Spacing_Bottom*np.tan(beta))
        I_XX_n_Top = Y_n_stringer_Top**2 * area_Stringer
        I_XX_Bottom_tot += I_XX_n_Top
    return I_XX_Fs_tot, I_XX_Bs_tot, I_XX_Top_tot, I_XX_Bottom_tot

def stringers_Inertia_Y(X_Centroid, area_Stringer, Spacing_Top, Spacing_Bottom, X_centroid_Fs, X_centroid_Bs, beta):
    
    I_YY_Fs_tot = 0
    I_YY_Bs_tot = 0
    I_YY_Top_tot = 0
    I_YY_Bottom_tot = 0

    I_YY_Fs_tot = n_str_Fs*area_Stringer*X_centroid_Fs**2
    I_YY_Bs_tot = n_str_Bs*area_Stringer*X_centroid_Bs**2

    for i in range(n_str_Top):
        X_n_stringer_Top = np.abs(X_Centroid-(i-0.5)*Spacing_Top)
        I_YY_n_Top = X_n_stringer_Top**2 * area_Stringer
        I_YY_Top_tot += I_YY_n_Top

    for k in range(n_str_Bottom):
        X_n_stringer_Bottom = np.abs(X_Centroid-(((k-0.5)*Spacing_Bottom)/np.tan(beta)))
        I_YY_n_Bottom = X_n_stringer_Bottom**2 * area_Stringer
        I_YY_Bottom_tot += I_YY_n_Bottom
    
    return I_YY_Fs_tot, I_YY_Bs_tot, I_YY_Top_tot, I_YY_Bottom_tot

def total_Inertia_XX(I_XX_Total_Plates, I_XX_Stringers_Fs, I_XX_Stringers_Bs, I_XX_Stringers_Top, I_XX_Stringers_Bottom):
    I_XX_Total = I_XX_Total_Plates + I_XX_Stringers_Fs + I_XX_Stringers_Bs + I_XX_Stringers_Top + I_XX_Stringers_Bottom
    return I_XX_Total

def total_Inertia_YY(I_YY_Total_Plates, I_YY_Stringers_Fs, I_YY_Stringers_Bs, I_YY_Stringers_Top, I_YY_Stringers_Bottom):
    I_YY_Total = I_YY_Total_Plates + I_YY_Stringers_Fs + I_YY_Stringers_Bs + I_YY_Stringers_Top + I_YY_Stringers_Bottom
    return I_YY_Total

def total_Inertia_J(I_XX_Total, I_YY_Total):
    J_Total = I_XX_Total + I_YY_Total
    return J_Total
