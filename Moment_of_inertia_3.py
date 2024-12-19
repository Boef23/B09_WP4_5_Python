"""I_xx, I_yy calculation"""
from Parameters import * 
import numpy as np
increment_z_Step = 0.01 #[m]
z_list = np.arange(0, 15.325, 0.01) 


def calculate_Centroid_Stringer(a_Str = a_Str, t_Str_a = t_Str_a, b_Str = b_Str, t_Str_b = t_Str_b):
     x_Centroid_Stringer = (0.5 * t_Str_b * b_Str ** 2)/(a_Str * t_Str_a + b_Str * t_Str_b)
     y_Centroid_Stringer = (0.5 * t_Str_a * a_Str ** 2)/(a_Str * t_Str_a + b_Str * t_Str_b)
     return x_Centroid_Stringer, y_Centroid_Stringer

def calculate_Inertia_Local_Stringer(a_Str = a_Str, t_Str_a = t_Str_a, b_Str = b_Str, t_Str_b = t_Str_b, x_Centroid_Stringer = calculate_Centroid_Stringer()[0], y_Centroid_Stringer = calculate_Centroid_Stringer()[1]):
     Ixx_Local_Stringer = (b_Str * t_Str_b ** 3)/12 + b_Str * t_Str_b * y_Centroid_Stringer ** 2 + (t_Str_a * a_Str ** 3)/12 + a_Str * t_Str_a * (0.5 * a_Str - y_Centroid_Stringer) ** 2
     Iyy_Local_Stringer = (t_Str_b * b_Str ** 3)/12 + b_Str * t_Str_b * (0.5 * b_Str - x_Centroid_Stringer) ** 2 + (a_Str * t_Str_a ** 3)/12 + a_Str * t_Str_a * x_Centroid_Stringer ** 2
     return Ixx_Local_Stringer, Iyy_Local_Stringer

#Centroid determination 
def calculate_Centroid_wingbox(z, b=b, t_Fs = t_Fs, t_Bs = t_Bs, t_Bottom = t_Bottom, t_Top = t_Top, m = n_Str_Bottom_ztip, n = n_Str_Top_ztip, t_str_a = t_Str_a, t_str_b = t_Str_b, a_str = a_Str, b_str = b_Str):
     #Calculate Coord along Z
     chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
     c = chord

     #Calculate H_BS, L_top 
     h_Bs = 0.0732 * chord #height of back spar
     l_top = 0.5 * chord #length op top flange 
     
     #Calculate area of the wing box and area of the stringers
     A_wb = (t_Top + t_Bottom) * l_top + (t_Fs + t_Bs) * h_Bs
     A_str = (a_str*t_str_a + b_str*t_str_b)

     #Calculate centroid of stringer
     y_centroid_str = calculate_Centroid_Stringer()[1]

     #Calculate centroid with respect to the middle of the wing bock
     y_Centroid = ((t_Bottom - t_Top) * (h_Bs*l_top/2) + (m-n)*(h_Bs/2 - y_centroid_str)*A_str)/((n+m)*A_str+A_wb)

     #Assumption 
     x_Centroid =  ((t_Fs - t_Bs)*(h_Bs*l_top/2))/(A_wb + (m+n)*A_str)


     #Redefine the reference point to top left 
     y_Centroid = h_Bs/2 - y_Centroid 
     x_Centroid = l_top/2 + x_Centroid


     return x_Centroid, y_Centroid 

def Ixx_Fs():
     Ixx_Fs = (t_Fs * h_Bs ** 3)/12 + t_Fs * h_Bs * (0.5 * h_Bs - y_Centroid) ** 2
     #From geometry function, h_Bs is used instead of h_Fs due to assumption
     return Ixx_Fs

def Ixx_Top():
    Ixx_Top = (l_Top * t_Top ** 3)/12 + l_Top * t_Top * y_Centroid ** 2
    #From geometry function
    return Ixx_Top

def Ixx_Bs():
    Ixx_Bs = (t_Bs * h_Bs ** 3)/12 + t_Bs * h_Bs * (0.5 * h_Bs - y_Centroid) ** 2
    #From geometry function
    return Ixx_Bs

def Ixx_Bottom():
    Ixx_Bottom = (l_Bottom * t_Bottom ** 3)/12 + l_Bottom * t_Bottom * (h_Bs - y_Centroid) ** 2
    #From geometry function
    return Ixx_Bottom

def Ixx_Stringers():
    Ixx_Stringers = (n_Str_Top(i) + n_Str_Bottom(i)) * Ixx_Local_Stringer + n_Str_Top(i) * ((a_Str * t_Str_a + b_Str * t_Str_b) * (y_Centroid - y_Centroid_Stringer) ** 2) + n_Str_Bottom(i) * ((a_Str * t_Str_a + b_Str * t_Str_b) * (h_Bs - y_Centroid_Stringer - y_Centroid) ** 2))
    #From list of number of stringers per side and i is increment value to later put this in a loop per bay.
    #Ixx_Local_Stringer is from local inertia function
    return Ixx_Stringers



def calculate_paramters_per_Bay(nbay, n_Str_Top_Bay, n_Str_Bottom_Bay):
    #Calculate Centroid per increment
    calculate_Centroid_wingbox(n = n_Str_Top_Bay, m = n_Str_Bottom_Bay)



    #Calculate increment 
     
     


#Defined, as bay = 0 is the tip
for z in z_list:
    if z < 0.60:
        #So now it is in bay 14
        
     
    elif 0.60 <= z < 1.23:
        #So now it is in bay 13, etc 
  
    elif 1.23 <= z < 1.88:
    
    elif 1.88 <= z < 2.56:
       
    elif 2.56 <= z < 3.28:

    elif 3.28 <= z < 4.04:

    elif 4.04 <= z < 4.85:

    elif 4.85 <= z < 5.71:

    elif 5.71 <= z < 6.65:

    elif 6.65 <= z < 7.69:
 
    elif 7.69 <= z < 8.86:

    elif 8.86 <= z < 10.24:

    elif 10.24 <= z < 12.02:

    else:

