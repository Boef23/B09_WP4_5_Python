"""I_xx, I_yy calculation"""
from Parameters import * 
from 

#Temporary parameters 
# a = w_Stringer  #[m] width of the stringers 
# t_s = t_Stringer  #[m] thickness of the stringers
# c = 4.9 #This must be changed to a function 
# L_wb = 0.5*c #Length rectangularsised wing box
# H_wb = 0.0732*c #HeightRectangularsied wing box 
# m = 16
# n = 16
# j = 11
# k = 10

#Centroid determination 
def calculate_Centroid(z, b=b, t_Fs = t_Fs, t_Bs = t_Bs, t_Bottom = t_Bottom, t_Top = t_Top, a = w_Stringer, b  m = n_str_Top, n = n_str_Bottom):
     #Calculate Coord along Z
     chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
     c = chord

     #Calculate H_BS, L_top 
     h_Bs = 0.0732 * chord #height of back spar
     l_top = 0.5 * chord #length op top flange 
     
     #Calculate area of the wing box and area of the stringers
     A_wb = (t_Top + t_Bottom) * l_top + (t_Fs + t_Bs) * h_Bs
     A_str = (m + n) * (a)

     #Calculate centroid with respect to the middle of the wing bock
     y_centroid = 

     #Redefine the reference point to top left 
     
     return x_centroid, y_centroid 

def calculate_Centroid_Stringer(a_Str, t_Str_a, b_Str, t_Str_b):
     x_Centroid_Stringer = (0.5 * t_Str_b * b_Str ** 2)/(a_Str * t_Str_a + b_Str * t_Str_b)
     y_Centroid_Stringer = (0.5 * t_Str_a * a_Str ** 2)/(a_Str * t_Str_a + b_Str * t_Str_b)
     return x_Centroid_Stringer, y_Centroid_Stringer

def calculate_Inertia_Local_Stringer(a_Str, t_Str_a, b_Str, t_Str_b, x_Centroid_Stringer, y_Centroid_Stringer):
     Ixx_Local_Stringer = (b_Str * t_Str_b ** 3)/12 + b_Str * t_Str_b * y_Centroid_Stringer ** 2 + (t_Str_a * a_Str ** 3)/12 + a_Str * t_Str_a * (0.5 * a_Str - y_Centroid_Stringer) ** 2
     Iyy_Local_Stringer = (t_Str_b * b_Str ** 3)/12 + b_Str * t_Str_b * (0.5 * b_Str - x_Centroid_Stringer) ** 2 + (a_Str * t_Str_a ** 3)/12 + a_Str * t_Str_a * x_Centroid_Stringer ** 2
     return Ixx_Local_Stringer, Iyy_Local_Stringer