"""I_xx, I_yy calculation"""
from Parameters import * 
import numpy as np
increment_z_Step = 0.01 #[m]
z_list = np.arange(0, 15.325, 0.01) 
Ixx_list = []

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


def Ixx_Wingbox(z, n_Str_Top, n_Str_Bottom, y_centroid_wingbox, b = b):
     chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
     h_Bs = 0.0732 * chord #height of back spar
     l_Top = 0.5 * chord #length op top flange 
     l_Bottom = l_Top

     y_Centroid = y_centroid_wingbox
     Ixx_Local_Stringer = calculate_Inertia_Local_Stringer()[0]
     y_Centroid_Stringer = calculate_Centroid_Stringer()[1]

     Ixx_Fs = (t_Fs * h_Bs ** 3)/12 + t_Fs * h_Bs * (0.5 * h_Bs - y_Centroid) ** 2
     Ixx_Top = (l_Top * t_Top ** 3)/12 + l_Top * t_Top * y_Centroid ** 2
     Ixx_Bs = (t_Bs * h_Bs ** 3)/12 + t_Bs * h_Bs * (0.5 * h_Bs - y_Centroid) ** 2
     Ixx_Bottom = (l_Bottom * t_Bottom ** 3)/12 + l_Bottom * t_Bottom * (h_Bs - y_Centroid) ** 2
     Ixx_Stringers = (n_Str_Top + n_Str_Bottom) * Ixx_Local_Stringer + n_Str_Top * ((a_Str * t_Str_a + b_Str * t_Str_b) * (y_Centroid - y_Centroid_Stringer) ** 2) + n_Str_Bottom * ((a_Str * t_Str_a + b_Str * t_Str_b) * (h_Bs - y_Centroid_Stringer - y_Centroid) ** 2)
     
     Ixx = Ixx_Fs + Ixx_Top + Ixx_Bs + Ixx_Bottom + Ixx_Stringers 

     return Ixx


    #Calculate increment 

def checkBay(z):  
     z = b/2 - z   
     if z < 0.60:
          #So now it is in bay 14
          n_str_top = sum(n_Str_Top_incr[0:14])
          n_str_bottom = sum(n_Str_Top_incr[0:14])
          
     elif 0.60 <= z < 1.23:
          #So now it is in bay 13, etc 
          n_str_top = sum(n_Str_Top_incr[0:13])
          n_str_bottom = sum(n_Str_Top_incr[0:13])
     
     elif 1.23 <= z < 1.88:
               n_str_top = sum(n_Str_Top_incr[0:12])
               n_str_bottom = sum(n_Str_Top_incr[0:12])
     
     elif 1.88 <= z < 2.56:
               n_str_top = sum(n_Str_Top_incr[0:11])
               n_str_bottom = sum(n_Str_Top_incr[0:11])
          
     elif 2.56 <= z < 3.28:
               n_str_top = sum(n_Str_Top_incr[0:10])
               n_str_bottom = sum(n_Str_Top_incr[0:10])

     elif 3.28 <= z < 4.04:
               n_str_top = sum(n_Str_Top_incr[0:9])
               n_str_bottom = sum(n_Str_Top_incr[0:9])

     elif 4.04 <= z < 4.85:
               n_str_top = sum(n_Str_Top_incr[0:8])
               n_str_bottom = sum(n_Str_Top_incr[0:8])

     elif 4.85 <= z < 5.71:
               n_str_top = sum(n_Str_Top_incr[0:7])
               n_str_bottom = sum(n_Str_Top_incr[0:7])

     elif 5.71 <= z < 6.65:
               n_str_top = sum(n_Str_Top_incr[0:6])
               n_str_bottom = sum(n_Str_Top_incr[0:6])

     elif 6.65 <= z < 7.69:
               n_str_top = sum(n_Str_Top_incr[0:5])
               n_str_bottom = sum(n_Str_Top_incr[0:5])
     
     elif 7.69 <= z < 8.86:
               n_str_top = sum(n_Str_Top_incr[0:4])
               n_str_bottom = sum(n_Str_Top_incr[0:4])

     elif 8.86 <= z < 10.24:
               n_str_top = sum(n_Str_Top_incr[0:3])
               n_str_bottom = sum(n_Str_Top_incr[0:3])

     elif 10.24 <= z < 12.02:
               n_str_top = sum(n_Str_Top_incr[0:2])
               n_str_bottom = sum(n_Str_Top_incr[0:2])

     else:
               n_str_top = sum(n_Str_Top_incr[0:1])
               n_str_bottom = sum(n_Str_Top_incr[0:1])  
     
     return n_str_top, n_str_bottom    



#Defined, as bay = 0 is the tip
for z in z_list:
     n_str = checkBay(z)
     n_str_top = n_str[0]
     n_str_bottom = n_str[1]
     centroid_wingbox = calculate_Centroid_wingbox(z, n = n_str_top, m = n_str_bottom)
     x_centroid_wingbox = centroid_wingbox[0]
     y_centroid_wingbox = centroid_wingbox[1]
     
     Ixx_wingbox_z = Ixx_Wingbox(z, n_str_top, n_str_bottom, y_centroid_wingbox)

     Ixx_list.append(Ixx_wingbox_z)

print(Ixx_list)