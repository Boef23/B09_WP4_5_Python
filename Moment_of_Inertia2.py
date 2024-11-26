#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio, b

#Chord length as function of spanwise position
def chord_Length(c_Root, taper_Ratio, b):
    for i in range 10000:
        chord_Local = c_Root - c_Root*(1-taper_Ratio)*i/100000
