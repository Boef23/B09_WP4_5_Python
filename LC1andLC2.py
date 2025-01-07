import numpy as np
import math
from Parameters import *

# variables


v = poisson_ratio
t_skin = 0.0015
t_front_spar = t_Fs
t_back_spar = t_Bs
WbFrac = 0.5
Cr = c_Root
taper = taper_Ratio
span = 30.65

rib_distances = [0.60, 0.63, 0.65, 0.68, 0.72, 0.76, 0.81, 0.86, 0.94, 1.04, 1.17, 1.38, 1.78, 3.28]

def get_a_and_C_max(z):
    if z < 0.60:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 0.0)
        return rib_distances[0], c_max
    elif 0.60 <= z < 1.23:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 0.60)
        return rib_distances[1], c_max
    elif 1.23 <= z < 1.88:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 1.23)
        return rib_distances[2], c_max
    elif 1.88 <= z < 2.56:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 1.88)
        return rib_distances[3], c_max
    elif 2.56 <= z < 3.28:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 2.56)
        return rib_distances[4], c_max
    elif 3.28 <= z < 4.04:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 3.28)
        return rib_distances[5], c_max
    elif 4.04 <= z < 4.85:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 4.04)
        return rib_distances[6], c_max
    elif 4.85 <= z < 5.71:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 4.85)
        return rib_distances[7], c_max
    elif 5.71 <= z < 6.65:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 5.71)
        return rib_distances[8], c_max
    elif 6.65 <= z < 7.69:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 6.65)
        return rib_distances[9], c_max
    elif 7.69 <= z < 8.86:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 7.69)
        return rib_distances[10], c_max
    elif 8.86 <= z < 10.24:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 8.86)
        return rib_distances[11], c_max
    elif 10.24 <= z < 12.02:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 10.24)
        return rib_distances[12], c_max
    else:
        c_max = Cr - (2 * (1 - taper) * (Cr / span) * 12.02)
        return rib_distances[13], c_max

# aprroximates value of K_s based on a_b ratio of each bay

def calculate_ks(a_b_ratio):
    if a_b_ratio <= 0.1:
        return 15.0
    elif 0.1 < a_b_ratio <= 0.2:
        return 14.8
    elif 0.2 < a_b_ratio <= 0.3:
        return 14.6
    elif 0.3 < a_b_ratio <= 0.4:
        return 14.4
    elif 0.4 < a_b_ratio <= 0.5:
        return 14.2
    elif 0.5 < a_b_ratio <= 0.6:
        return 14.0
    elif 0.6 < a_b_ratio <= 0.7:
        return 13.8
    elif 0.7 < a_b_ratio <= 0.8:
        return 13.6
    elif 0.8 < a_b_ratio <= 0.9:
        return 13.4
    elif 0.9 < a_b_ratio <= 1:
        return 13.2
    elif 1 < a_b_ratio <= 1.1:
        return 13.0
    elif 1.1 < a_b_ratio <= 1.2:
        return 12.8
    elif 1.2 < a_b_ratio <= 1.3:
        return 12.6
    elif 1.3 < a_b_ratio <= 1.4:
        return 12.4
    elif 1.4 < a_b_ratio <= 1.5:
        return 12.2
    elif 1.5 < a_b_ratio <= 1.6:
        return 12.0
    elif 1.6 < a_b_ratio <= 1.7:
        return 11.8
    elif 1.7 < a_b_ratio <= 1.8:
        return 11.6
    elif 1.8 < a_b_ratio <= 1.9:
        return 11.4
    elif 1.9 < a_b_ratio <= 2:
        return 11.2
    elif 2 < a_b_ratio <= 2.01:
        return 11.0
    elif 2.01 < a_b_ratio <= 2.02:
        return 10.99
    elif 2.02 < a_b_ratio <= 2.03:
        return 10.98
    elif 2.03 < a_b_ratio <= 2.04:
        return 10.97
    elif 2.04 < a_b_ratio <= 2.05:
        return 10.96
    elif 2.05 < a_b_ratio <= 2.06:
        return 10.95
    elif 2.06 < a_b_ratio <= 2.07:
        return 10.94
    elif 2.07 < a_b_ratio <= 2.08:
        return 10.93
    elif 2.08 < a_b_ratio <= 2.09:
        return 10.92
    elif 2.09 < a_b_ratio <= 2.1:
        return 10.91
    elif 2.1 < a_b_ratio <= 2.2:
        return 10.9
    elif 2.2 < a_b_ratio <= 2.3:
        return 10.8
    elif 2.3 < a_b_ratio <= 2.4:
        return 10.7
    elif 2.4 < a_b_ratio <= 2.5:
        return 10.6
    elif 2.5 < a_b_ratio <= 2.6:
        return 10.5
    elif 2.6 < a_b_ratio <= 2.7:
        return 10.4
    elif 2.7 < a_b_ratio <= 2.8:
        return 10.3
    elif 2.8 < a_b_ratio <= 2.9:
        return 10.2
    elif 2.9 < a_b_ratio <= 3:
        return 10.1
    else:
        return 9.7
    
# aprroximates value of K_c based on a_b ratio of each bay

def calculate_kc(a_b_ratio):
    if a_b_ratio <= 0.6:
        return 14.0
    elif 0.6 < a_b_ratio <= 0.62:
        return 13.9
    elif 0.62 < a_b_ratio <= 0.64:
        return 13.8
    elif 0.64 < a_b_ratio <= 0.66:
        return 13.7
    elif 0.66 < a_b_ratio <= 0.68:
        return 13.6
    elif 0.68 < a_b_ratio <= 0.7:
        return 13.5
    elif 0.7 < a_b_ratio <= 0.72:
        return 13.4
    elif 0.72 < a_b_ratio <= 0.74:
        return 13.3
    elif 0.74 < a_b_ratio <= 0.76:
        return 13.2
    elif 0.76 < a_b_ratio <= 0.78:
        return 13.1
    elif 0.78 < a_b_ratio <= 0.8:
        return 13.0
    elif 0.8 < a_b_ratio <= 0.82:
        return 12.9
    elif 0.82 < a_b_ratio <= 0.84:
        return 12.8
    elif 0.84 < a_b_ratio <= 0.86:
        return 12.7
    elif 0.86 < a_b_ratio <= 0.88:
        return 12.6
    elif 0.88 < a_b_ratio <= 0.9:
        return 12.5
    elif 0.9 < a_b_ratio <= 0.92:
        return 12.4
    elif 0.92 < a_b_ratio <= 0.94:
        return 12.3
    elif 0.94 < a_b_ratio <= 0.96:
        return 12.2
    elif 0.96 < a_b_ratio <= 0.98:
        return 12.1
    elif 0.98 < a_b_ratio <= 1.0:
        return 12.0
    elif 1.0 < a_b_ratio <= 1.05:
        return 11.8
    elif 1.05 < a_b_ratio <= 1.1:
        return 11.6
    elif 1.1 < a_b_ratio <= 1.15:
        return 11.4
    elif 1.15 < a_b_ratio <= 1.2:
        return 11.2
    elif 1.2 < a_b_ratio <= 1.25:
        return 11.0
    elif 1.25 < a_b_ratio <= 1.3:
        return 10.8
    elif 1.3 < a_b_ratio <= 1.35:
        return 10.6
    elif 1.35 < a_b_ratio <= 1.4:
        return 10.4
    elif 1.4 < a_b_ratio <= 1.45:
        return 10.2
    elif 1.45 < a_b_ratio <= 1.5:
        return 10.0
    elif 1.5 < a_b_ratio <= 1.55:
        return 9.9
    elif 1.55 < a_b_ratio <= 1.6:
        return 9.8
    elif 1.6 < a_b_ratio <= 1.65:
        return 9.7
    elif 1.65 < a_b_ratio <= 1.7:
        return 9.6
    elif 1.7 < a_b_ratio <= 1.75:
        return 9.5
    elif 1.75 < a_b_ratio <= 1.8:
        return 9.4
    elif 1.8 < a_b_ratio <= 1.85:
        return 9.3
    elif 1.85 < a_b_ratio <= 1.9:
        return 9.2
    elif 1.9 < a_b_ratio <= 1.95:
        return 9.1
    elif 1.95 < a_b_ratio <= 2.0:
        return 9.0
    elif 2.0 < a_b_ratio <= 2.1:
        return 8.9
    elif 2.1 < a_b_ratio <= 2.2:
        return 8.8
    elif 2.2 < a_b_ratio <= 2.3:
        return 8.7
    elif 2.3 < a_b_ratio <= 2.4:
        return 8.6
    elif 2.4 < a_b_ratio <= 2.5:
        return 8.5
    else:
        return 7


#LC1

shearStressCriticalFront = np.zeros_like(np.arange(0.00, 15.33, 0.01))
shearStressCriticalBack = np.zeros_like(np.arange(0.00, 15.33, 0.01))
z_values = np.arange(0.00, 15.33, 0.01)

for i, z in enumerate(z_values):
    a, cMax = get_a_and_C_max(z)
    b_front = cMax * 0.1092
    b_back = cMax * 0.0732

    a_b_ratio_front = a / b_front
    a_b_ratio_back = a / b_back

    k_s_front = calculate_ks(a_b_ratio_front)
    k_s_back = calculate_ks(a_b_ratio_back)

    shearStressCriticalFront[i] = (((math.pi)**2) * k_s_front * E * (t_front_spar**2)) / (12 * (1 - (v**2)) * (b_front**2))
    shearStressCriticalBack[i] = (((math.pi)**2) * k_s_back * E * (t_back_spar**2)) / (12 * (1 - (v**2)) * (b_back**2))

#LC2

skinStressCriticalCompUPPER = np.zeros_like(np.arange(0.00, 15.33, 0.01))
skinStressCriticalCompLOWER = np.zeros_like(np.arange(0.00, 15.33, 0.01))

for i, z in enumerate(z_values):
    a, cMax = get_a_and_C_max(z)
    b_upper = delta_Top
    b_lower = delta_Bottom
    b = cMax * 0.5

    a_b_ratio = a/b

    k_c = calculate_kc(a_b_ratio)

    skinStressCriticalCompUPPER[i] = (((math.pi)**2) * k_c * E * (t_skin**2)) / (12 * (1 - (v**2)) * (b_upper**2))
    skinStressCriticalCompLOWER[i] = (((math.pi)**2) * k_c * E * (t_skin**2)) / (12 * (1 - (v**2)) * (b_lower**2))


    z += 0.01
if __name__ == '__main__':
    print(skinStressCriticalCompUPPER)
    print(skinStressCriticalCompLOWER)
    print(shearStressCriticalFront)
    print(shearStressCriticalBack)
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Define the z-axis (spanwise location)
    z_axis = np.arange(0.00, 15.33, 0.01)

    # Create subplots for better visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot Shear Stress Critical (Front)
    axes[0, 0].plot(z_axis, shearStressCriticalFront, label="Shear Stress Critical Front", color='blue')
    axes[0, 0].set_title("Shear Stress Critical (Front)")
    axes[0, 0].set_xlabel("Spanwise Location (z) [m]")
    axes[0, 0].set_ylabel("Critical Shear Stress [Pa]")
    axes[0, 0].grid(True)
    axes[0, 0].legend()

    # Plot Shear Stress Critical (Back)
    axes[0, 1].plot(z_axis, shearStressCriticalBack, label="Shear Stress Critical Back", color='red')
    axes[0, 1].set_title("Shear Stress Critical (Back)")
    axes[0, 1].set_xlabel("Spanwise Location (z) [m]")
    axes[0, 1].set_ylabel("Critical Shear Stress [Pa]")
    axes[0, 1].grid(True)
    axes[0, 1].legend()

    # Plot Skin Stress Critical Compression (Upper)
    axes[1, 0].plot(z_axis, skinStressCriticalCompUPPER, label="Skin Stress Critical Upper", color='green')
    axes[1, 0].set_title("Skin Stress Critical Compression (Upper)")
    axes[1, 0].set_xlabel("Spanwise Location (z) [m]")
    axes[1, 0].set_ylabel("Critical Skin Stress [Pa]")
    axes[1, 0].grid(True)
    axes[1, 0].legend()

    # Plot Skin Stress Critical Compression (Lower)
    axes[1, 1].plot(z_axis, skinStressCriticalCompLOWER, label="Skin Stress Critical Lower", color='purple')
    axes[1, 1].set_title("Skin Stress Critical Compression (Lower)")
    axes[1, 1].set_xlabel("Spanwise Location (z) [m]")
    axes[1, 1].set_ylabel("Critical Skin Stress [Pa]")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    # Adjust layout for better readability
    plt.tight_layout()
    plt.show()