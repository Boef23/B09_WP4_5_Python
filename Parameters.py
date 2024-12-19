#Wing
lambda_LE = 0.4363 #Leading edge sweep angle (rad) placeholder value
taper_Ratio = 0.316 #Taper ratio (-)
b = 30.65 #wing span (m)
S = 98.75   #Wing area (m^2)
lambda_Dihedral = 0.0349 #dihedral angle (rad) placeholder value

#Airfoil
c_Root = 4.9 #Root chord (m)
c_Tip = c_Root - c_Root*(1-taper_Ratio)

#Stringers
t_str_a = 0.002 #Thickness long side (m) placeholder value
t_str_b = 0.002 #Thickness short side
a_str = 0.20 #Stringer width in plane of the skin it is attached to (m) placeholder value
b_str = 0.15 #Stringer height out of plane of the skin it is attached to (m) placeholder value

#Number of stringer spars
wb_Frac = 0.5
n_str_Fs = 0
n_str_Bs = 0

#Number of stringers plates
n_str_Top_ztip = 2
n_str_Bottom_ztip = 10

#Increment Stringers Per Bay Top Plate 
# #Should be even amount
n_str_Top_1incr = 0
n_str_Top_2incr = 2
n_str_Top_3incr = 2
n_str_Top_4incr = 2
n_str_Top_5incr = 2
n_str_Top_6incr = 2
n_str_Top_7incr = 2
n_str_Top_8incr = 2
n_str_Top_9incr = 2
n_str_Top_10incr = 2
n_str_Top_11incr = 2
n_str_Top_12incr = 2
n_str_Top_13incr = 2
n_str_Top_14incr = 2

#Increment Stringers Per Bay Top Plate
#Should be even amount
n_str_Bottom_1incr = 0
n_str_Bottom_2incr = 2
n_str_Bottom_3incr = 2
n_str_Bottom_4incr = 2
n_str_Bottom_5incr = 2
n_str_Bottom_6incr = 2
n_str_Bottom_7incr = 2
n_str_Bottom_8incr = 2
n_str_Bottom_9incr = 2
n_str_Bottom_10incr = 2
n_str_Bottom_11incr = 2
n_str_Bottom_12incr = 2
n_str_Bottom_13incr = 2
n_str_Bottom_14incr = 2

#Spacings
delta_Top = (c_Tip)/(n_str_Top_ztip + 1)
delta_Bottom = (c_Tip)/(n_str_Bottom_ztip + 1)

#Spars
t_Fs = 0.006 #thickness front spar (m) placeholder value
t_Bs = 0.006 #thickness back spar (m) placeholder value
h_Fs = 0.3 #fornt spar heighr(m) placeholder value
h_Bs = 0.2 #back spar height (m) placeholder value


#Plates
t_Top = 0.0015 #thickness top plate (m) placeholder value
t_Bottom = 0.0015 #thickness bottom plate (m) placeholder value

#Cruise
cruise_Velocity = 228   #Cruise velocity (m/s), M=0.77 at 35000ft alt
cruise_Density = 0.3796 #Cruise density (kg/m^3) at 35000ft alt

#Landing Gear
mlg_Pos = 4.35  #Lateral position of MLG on wing (m)

#Engine
z_Engine_Frac = 0.35 #Fractional lateral position w.r.t. half span of engine on wing (m)
engine_Mass = 1111.3    #Mass of engine (kg)

#AL2024-T81

E = 7.24*10**9 # Modulus of elasticity [Pa]
poisson_ratio = 1/3 # Unitless
