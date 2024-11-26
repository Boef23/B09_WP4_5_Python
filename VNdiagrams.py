"""Class 2 weight estimation - Gust Diagram"""
import numpy as np 
import matplotlib.pyplot as plt

#M for metric units, B for british units

#Constants
CLAlphaCruise = 6.669               # 1/rad 
CLAlphaFlaps = 7.8495               # 1/rad 
CLMax = 1.624                       # -                        

rhoCruiseM = 0.379597               #kg/m^3 ISA at 350000 ft  
rhoSeaLevelM = 1.225                #kg/m^3
uHatCruise = 25                     #ft/s
uHatHighAlpha = 66                  #ft/s  
uHatDive = 38                       #ft/s 
gM = 9.81                           #m/s^2 

#Aircraft paramters 
weightAirplaneM = 23731*9.81         # N
VCruiseM = 228.3                     # m/s
macM = 2.90                          # m 
wingAreaM = 98.85                    # m^2

#InitialCalculation
VmaxAlphaM = np.sqrt((weightAirplaneM*2)/(wingAreaM*rhoCruiseM*CLMax))
VDiveM = 1.25*VCruiseM

#Convert everything to british units 
weightAirplaneB = weightAirplaneM * 0.224808943     #pounds
VCruiseB = VCruiseM * 3.2808                        #ft/s 
VmaxAlphaB = VmaxAlphaM * 3.2808
VDiveB = VDiveM * 3.2808
rhoCruiseB = rhoCruiseM * 0.06242796                #pounds/cubic feet
wingAreaB = 98.85 * 10.7639104  
macB = 2.90  * 3.2808399   
gB = 32.2                      

#Detmine which rho to u


#Calculations for gust diagram 

def calculateDeltaN (rho, V, C_Lalpha, W, u_hat): 
    
    mu_g = (2*(W/wingAreaB))/(rho*gB*C_Lalpha*macB) 
    
    K = (0.88*mu_g)/(5.3+mu_g)
    
    u =K*u_hat
    
    deltaN = (rho*V*C_Lalpha*u)/(2*(W)/(wingAreaB))
    
    return deltaN
    
delta_n_stall = calculateDeltaN(rhoSeaLevelM , VmaxAlphaB, CLAlphaCruise, weightAirplaneB, uHatHighAlpha)
delta_n_cruise = calculateDeltaN(rhoSeaLevelM , VCruiseB, CLAlphaCruise, weightAirplaneB, uHatCruise)
delta_n_dive = calculateDeltaN(rhoSeaLevelM , VDiveB, CLAlphaCruise, weightAirplaneB, uHatDive)

print(delta_n_cruise, delta_n_stall, delta_n_cruise, delta_n_dive)


x = [0, VmaxAlphaM, VCruiseM, VDiveM]
y = [1, 1+delta_n_stall, 1+delta_n_cruise, 1+delta_n_dive]
z = [1, 1-delta_n_stall, 1-delta_n_cruise, 1-delta_n_dive]

print(VmaxAlphaM,VDiveM)


#Calculations for manoeuvre diagram


plt.plot(x,y)


# Show plot
plt.xlabel("Velocity [m/s]")
plt.ylabel("Load factor")
plt.title("V,n diagram")
plt.grid(True)  
plt.legend(["Gust diagram", "Maneuver diagram"], loc="upper left")
plt.show()
