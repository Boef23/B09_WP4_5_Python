# Import libraries
from Parameters import*
import matplotlib.pyplot as plt
import numpy as np
import math

# Variables
Cr = 4.9  # Wing root chord [m]
taper = 0.316  # Wing taper ratio
span = 30.65  # Wing span [m]
v = 0.333  # Poisson's ratio
t = 0.0015  # Thickness [m]
E = 72.4 * (10**9)  # Young's Modulus [Pa]
WbFrac = 0.5  # Fraction of chord occupied by stringers
numString = 10  # Number of stringers

# Rib distances (a values) [m]
rib_distances = [0.60, 0.63, 0.65, 0.68, 0.72, 0.76, 0.81, 0.86, 0.94, 1.04, 1.17, 1.38, 1.78, 3.28]

# Z Positions
z_positions = [0]  
for distance in rib_distances:
    z_positions.append(z_positions[-1] + distance)  
# Chord function  
def chord(z):
    return Cr - 2 * (1 - taper) * Cr / span * z

# Function Ks
def calculate_ks(a_b_ratio):

    if a_b_ratio <= 1:
        return 15
    elif 1 < a_b_ratio <= 1.2:
        return 14
    elif 1.2 < a_b_ratio <= 1.4:
        return 12.5
    elif 1.4 < a_b_ratio <= 1.8:
        return 11.5
    elif 1.8 < a_b_ratio <= 2:
        return 10.5
    elif 2 < a_b_ratio <= 2.5:
        return 10
    elif 2.5 < a_b_ratio <= 3:
        return 9.76
    elif 3 < a_b_ratio <= 4:
        return 9.5
    elif 4 < a_b_ratio <= 5:
        return 9.6
    else:
        return 6.9

# Spanwise positions 
z_values = np.arange(0, z_positions[-1], 0.01) 
ks_array = np.zeros_like(z_values)

# Ks array calculation
rib_bay_indices = np.digitize(z_values, z_positions[1:])  # Map z_values to the corresponding rib bay
for i, rib_index in enumerate(rib_bay_indices):

    # Chord lengths at the start and end of the rib bay
    chord_start = chord(z_positions[rib_index])
    chord_end = chord(z_positions[rib_index + 1])
    
    # Average chord length
    b = (chord_start) * 0.0732  # Effective web height
    a = rib_distances[rib_index]  # Rib distance
    a_b_ratio = a / b  # a/b ratio

    # Get Ks value based on a/b ratio
    ks_array[i] = calculate_ks(a_b_ratio)



# Skin stress critical calculation
CritWebBucklingStress = np.zeros_like(z_values)

for i, z in enumerate(z_values):
    c = chord(z)  # Chord length at position z
    b = (chord_start) * 0.0732  # Effective bay width
    k_s = ks_array[i]  # Kc value at position z
    if k_s > 0:
        CritWebBucklingStress[i] = ((math.pi**2) * k_s * E * (t**2)) / (12 * (1 - v**2) * (b**2))
    else:
        CritWebBucklingStress[i] = 0  

print(CritWebBucklingStress)
