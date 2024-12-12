"""I_xx, I_yy calculation"""
from Parameters import * 

a = 0.01  #[m] width of the stringers 
t_s = 0.001  #[m] thickness of the stringers
t_wb = 0.001 #[m] thickness of the wingbox 
c = 4.9 #This must be changed to a function 
LenghthRectangularisedWingBox = 0.5*c
HeightRectangularisedWingBox = 0.0732*c 
m = 16
n = 15
J = 11
K = 10

#Centroid determination 

def calculate_Centroid():
    A = (LenghthRectangularisedWingBox*2 + HeightRectangularisedWingBox*2) * t_wb  #Area wing box