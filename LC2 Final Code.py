# Import libraries 
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

# Function Kc
def calculate_kc(a_b_ratio):

    if a_b_ratio <= 0.6:
        return 14.0
    elif 0.6 < a_b_ratio <= 0.75:
        return 12.5
    elif 0.75 < a_b_ratio <= 0.85:
        return 9.5
    elif 0.85 < a_b_ratio <= 1.0:
        return 8.0
    elif 1.0 < a_b_ratio <= 1.15:
        return 7.7
    elif 1.15 < a_b_ratio <= 1.3:
        return 7.5
    elif 1.3 < a_b_ratio <= 1.5:
        return 7.4
    elif 1.5 < a_b_ratio <= 1.8:
        return 7.3
    elif 1.8 < a_b_ratio <= 2.0:
        return 7.25
    elif 2.0 < a_b_ratio <= 2.5:
        return 7.2
    elif 2.5 < a_b_ratio <= 3.0:
        return 7.1
    elif 3.0 < a_b_ratio <= 3.5:
        return 7.05
    elif 3.5 < a_b_ratio <= 4.0:
        return 7.0
    elif 4.0 < a_b_ratio <= 4.5:
        return 6.95
    else:
        return 6.9

# Spanwise positions 
z_values = np.arange(0, z_positions[-1], 0.01) 
kc_array = np.zeros_like(z_values)

# Kc array calculation
rib_bay_indices = np.digitize(z_values, z_positions[1:])  # Map z_values to the corresponding rib bay
for i, rib_index in enumerate(rib_bay_indices):

    # Chord lengths at the start and end of the rib bay
    chord_start = chord(z_positions[rib_index])
    chord_end = chord(z_positions[rib_index + 1])
    
    # Max wingbox length
    b = (chord_start) / 2  # Effective bay width (average of start and end chords)
    a = rib_distances[rib_index]  # Rib distance
    a_b_ratio = b / a  # a/b ratio

    # Get Kc value based on a/b ratio
    kc_array[i] = calculate_kc(a_b_ratio)



# Skin stress critical calculation
skinStressCritical = np.zeros_like(z_values)

for i, z in enumerate(z_values):
    c = chord(z)  # Chord length at position z
    b = (WbFrac * c) / numString  # Effective bay width
    k_c = kc_array[i]  # Kc value at position z
    if k_c > 0:
        skinStressCritical[i] = ((math.pi**2) * k_c * E * (t**2)) / (12 * (1 - v**2) * (b**2))
    else:
        skinStressCritical[i] = 0  

print(skinStressCritical)
