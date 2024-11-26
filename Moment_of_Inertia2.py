#Moment of inertia and torsional stiffness diagrams
from Parameters import c_Root, taper_Ratio

#Chord length as function of spanwise position
def chord_Length(c_Root, taper_Ratio):
    list_Chords = []
    for i in range(1,1000000):
        chord_Local = c_Root - c_Root*(1-taper_Ratio)*(i/1000000)
        list_Chords.append(chord_Local)
    return list_Chords

print(chord_Length)