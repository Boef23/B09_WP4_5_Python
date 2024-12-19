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
t_Str_a = 0.002 #Thickness long side (m) placeholder value
t_Str_b = 0.002 #Thickness short side
a_Str = 0.20 #Stringer width in plane of the skin it is attached to (m) placeholder value
b_Str = 0.15 #Stringer height out of plane of the skin it is attached to (m) placeholder value

#Number of stringer spars
wb_Frac = 0.5
n_Str_Fs = 0
n_Str_Bs = 0

#Number of stringers plates
n_Str_Top_ztip = 10
n_Str_Bottom_ztip = 2

#Increment Stringers Per Bay Top Plate 
# #Should be even amount
n_Str_Top_incr = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#Increment Stringers Per Bay Top Plate
#Should be even amount
n_Str_Bottom_incr = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#Spacings
delta_Top = (c_Tip)/(n_Str_Top_ztip + 1)
delta_Bottom = (c_Tip)/(n_Str_Bottom_ztip + 1)

#Spars
t_Fs = 0.006 #thickness front spar (m) placeholder value
t_Bs = 0.006 #thickness back spar (m) placeholder value


#Plates
t_Top = 0.0015 #thickness top plate (m) placeholder value
t_Bottom = 0.0015 #thickness bottom plate (m) placeholder value

#General Geometry
def geometry(z):
    chord = c_Root - c_Root*(1-taper_Ratio) * (z/(0.5 * b))
    h_Fs = 0.1092 * chord #height of front spar
    h_Bs = 0.0732 * chord #height of back spar
    l_Top = 0.5 * chord #length op top flange
    l_Bottom = 0.5 * chord #length of bottom flange
    return h_Fs, h_Bs, l_Top, l_Bottom

#Ribs
rib_Distances = [0.60, 0.63, 0.65, 0.68, 0.72, 0.76, 0.81, 0.86, 0.94, 1.04, 1.17, 1.38, 1.78, 3.28]

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
