"""Column Buckling"""
#creates an equation for columb buckling
#becomes and equation with respect to z, and is then plotted to show the critical stress

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Parameters import l_Stringer, t_Stringer, b
from Moment_of_inertia_comp import  zlist


elasticModulus = 72.4 * 10**9 # Pa
K = 4 #due to ribs, two sides are clamped
Ixx = 5/24 * t_Stringer * (l_Stringer/2)**3

def distanceArray():
    # Original array influencing step lengths
    original_values = np.array([0.00, 0.60, 1.23, 1.88, 2.56, 3.28, 4.04, 
                            4.84, 5.71, 6.65, 7.68, 8.86, 10.24, 12.02, 15.30])

    # Step values to distribute
    step_values = np.array([0.60, 0.63, 0.65, 0.68, 0.72, 0.76, 0.81, 
                        0.86, 0.94, 1.04, 1.17, 1.38, 1.78, 3.28])

    # Desired size of the output array
    total_size = 1533

    # Calculate differences in the original array
    differences = np.diff(original_values)

    # Normalize the differences to determine the step lengths
    normalized_lengths = differences / differences.sum()
    step_lengths = (normalized_lengths * total_size).astype(int)

    # Adjust for rounding to ensure total size is exactly 1533
    remainder = total_size - step_lengths.sum()
    step_lengths[:remainder] += 1  # Add the remainder to the first steps

    # Generate the result array
    result = np.concatenate([np.full(length, value) for length, value in zip(step_lengths, step_values)])
    return result

# Plot the graph
plt.figure(figsize=(12, 6))
plt.plot(distanceArray(), label="Generated Array (Proportional Steps)", color="blue")
plt.xlabel("Half Spanwise position (in centimeters)", fontsize=12)
plt.ylabel("Lengths between consecutive ribs (in meters)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.show()



def stringerArea():
    return t_Stringer * l_Stringer

def columnBuckling():
    sigmaCritical = K * np.pi**2 * elasticModulus * Ixx / (distanceArray()**2) * stringerArea())
    return sigmaCritical

print(f'The critical stress is {columnBuckling()} Pa' )

#Prints the plots for the critical stress

plt.plot(zlist, columnBuckling()/(10**6))
plt.xlabel("Half Spanwise position (in meters)", fontsize=12)
plt.ylabel("Critical Stress[MPa]", fontsize=12)
plt.show()

