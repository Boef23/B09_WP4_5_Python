# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:20:17 2024

@author: Bjorn
"""

import numpy as np 
import matplotlib.pyplot as plt

#M for metric units, B for british units

#Constants
CLAlphaCruise = 6.669               # 1/rad 
CLAlphaFlaps = 7.8495               # 1/rad 
CLMax = 1.624                       # -                        

rhoCruiseM = 0.379597               #kg/m^3 ISA at 350000 ft  
rhoSeaLevelM = 1.225                #kg/m^3
uHatCruiseSL = 25                     #ft/s
uHatHighAlphaSL = 66                  #ft/s  
uHatDiveSL = 38                       #ft/s 
uHatCruiseCL = 38                     #ft/s
uHatHighAlphaCL = 52                  #ft/s  
uHatDiveCL = 19                       #ft/s 

gM = 9.81                           #m/s^2 

#Aircraft paramters 
weightAirplaneM = 21000*9.81         # N
VCruiseM = 228.3                     # m/s
macM = 2.90                          # m 
wingAreaM = 98.85                    # m^2

#InitialCalculation
VstallM = np.sqrt((weightAirplaneM*2)/(wingAreaM*rhoCruiseM*CLMax))
VDiveM = 1.25*VCruiseM

#Convert everything to british units 
weightAirplaneB = weightAirplaneM * 0.224808943     #pounds
VCruiseB = VCruiseM * 3.2808                        #ft/s 
VstallB = VstallM * 3.2808
VDiveB = VDiveM * 3.2808
rhoCruiseB = rhoCruiseM * 0.00194                #slug/cubic feet
rhoSeaLevelB = 1.225 * 0.00194
wingAreaB = 98.85 * 10.7639104  
macB = 2.90  * 3.2808399   
gB = 32.2                      
        


def calculateDeltaN (W, S, rho, uhat, V):
    mu = (2*(W/S))/(rho*gB*macB*CLAlphaCruise)
    
    K = (0.88 * mu)/(5.3 + mu)
    
    u = K*uhat 
    
    deltaN = (rho*V*CLAlphaCruise*u)/(2*(W/S))
    
    return deltaN 

#Calculate values for current weight settings and cruise conditions
deltaNStallCL = calculateDeltaN(weightAirplaneB , wingAreaB , rhoCruiseB , uHatHighAlphaCL  , VstallB) 
deltaNCruiseCL =  calculateDeltaN(weightAirplaneB , wingAreaB , rhoCruiseB , uHatCruiseCL , VCruiseB)
deltaNDiveCL = calculateDeltaN(weightAirplaneB , wingAreaB , rhoCruiseB , uHatDiveCL , VDiveB)

#Calculate values for current weight settings and cruise conditions
deltaNStallSL = calculateDeltaN(weightAirplaneB , wingAreaB , rhoSeaLevelB , uHatHighAlphaSL  , VstallB) 
deltaNCruiseSL =  calculateDeltaN(weightAirplaneB , wingAreaB , rhoSeaLevelB , uHatCruiseSL , VCruiseB)
deltaNDiveSL = calculateDeltaN(weightAirplaneB , wingAreaB , rhoSeaLevelB , uHatDiveSL , VDiveB)


print(deltaNStallCL , deltaNCruiseCL, deltaNStallCL)
print(deltaNStallSL , deltaNCruiseSL, deltaNStallSL)

xCL = [0, VstallM , VCruiseM , VDiveM]
yCL = [1, 1+ deltaNStallCL, 1+ deltaNCruiseCL, 1+ deltaNDiveCL]
zCL = [1, 1- deltaNStallCL, 1- deltaNCruiseCL, 1- deltaNDiveCL]

xSL = [0, VstallM , VCruiseM , VDiveM]
ySL = [1, 1+ deltaNStallSL, 1+ deltaNCruiseSL, 1+ deltaNDiveSL]
zSL = [1, 1- deltaNStallSL, 1- deltaNCruiseSL, 1- deltaNDiveSL]


#Calculations for manoeuvre diagram
def ncurve (rho, C_LMAX, ws):
    q = 0.5 * rho 
    n = C_LMAX * q / ws
    return n

Nmax = 2.1 + (24000/(weightAirplaneM *2.205 + 10000)) #It must be converted to pounds
print(f"nMax = {Nmax}")
Nmin = -1
wingloading = weightAirplaneM/wingAreaM
n = ncurve (rhoCruiseM, CLMax, wingloading)


V_a = np.sqrt(Nmax/n)

V_vals_1 = np.linspace(0, V_a, 100)  # Velocity values for the positive parabolic portion
V_vals_2 = np.linspace(V_a, VDiveM , 100)  # Velocity values for the straight line portion at n_max
V_vals_neg_1 = np.linspace(0, VCruiseM , 100)  # Velocity values for the negative parabolic portion
V_vals_neg_2 = np.linspace(VCruiseM ,VDiveM  , 100)  # Straight line segment from (Vc, -1) to (Vd, 0)

# Positive portion definitions
n_vals_1 = n * V_vals_1**2  # Positive parabolic portion (n * V^2)
n_vals_1[n_vals_1 > Nmax] = Nmax  # Clip values exceeding Nmax to n_max
n_vals_2 = np.full_like(V_vals_2, Nmax)  # Constant line at n_max between Va and Vd

# Negative portion definitions
n_vals_neg_1 = -n * V_vals_neg_1**2  # Negative parabolic portion (-n * V^2)
n_vals_neg_1[n_vals_neg_1 < Nmin] = Nmin  # Clip values less than Nmin to n_min

# Linear part from (Vc, -1) to (Vd, 0)
n_vals_neg_2 = np.linspace(Nmin, 0, len(V_vals_neg_2))

# Vertical lines at Vd
V_vals_vert = [VDiveM, VDiveM]  # Velocity for vertical line
n_vals_vert_pos = [Nmax, 0]  # Positive vertical line


# Plotting
#Plot sea level
#plt.plot(xCL,yCL, color="red")

plt.plot(V_vals_1, n_vals_1, color='blue')

#plt.plot(xCL, zCL, color = "red")
plt.plot(V_vals_2, n_vals_2, color='blue')
plt.plot(V_vals_vert, n_vals_vert_pos, color='blue')  # Vertical line for positive load

plt.plot(V_vals_neg_1, n_vals_neg_1, color='blue')
plt.plot(V_vals_neg_2, n_vals_neg_2, color='blue')

plt.xlabel("Velocity [m/s]")
plt.ylabel("Load factor")
plt.title("V,n diagram - cruise altitude")
plt.grid(True)  
plt.legend(["Gust diagram", "Maneuver diagram"], loc="upper left")
plt.show()

#plt.plot(xSL,ySL, color="red")

plt.plot(V_vals_1, n_vals_1, color='blue')

#plt.plot(xSL, zSL, color = "red")
plt.plot(V_vals_2, n_vals_2, color='blue')
plt.plot(V_vals_vert, n_vals_vert_pos, color='blue')  # Vertical line for positive load

plt.plot(V_vals_neg_1, n_vals_neg_1, color='blue')
plt.plot(V_vals_neg_2, n_vals_neg_2, color='blue')

plt.xlabel("Velocity [m/s]")
plt.ylabel("Load factor")
plt.title("V,n diagram - Sea level")
plt.grid(True)  
plt.legend(["Maneuver diagram"], loc="upper left")
plt.show()

