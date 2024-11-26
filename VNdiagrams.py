"""Class 2 weight estimation - Gust Diagram"""
import numpy as np 
import matplotlib.pyplot as plt


#Constants
CLAlphaCruise = 6.669               # 1/rad 
CLAlphaFlaps = 7.8495               # 1/rad 
CLMax = 1.624                       # -                        

rhoCruise = 1.225                  # kg/m^2 
uHatCruise = 15.24 #11.499                 # m/s
uHatHighAlpha = 20.1168# 15.6972             # m/s   
uHatDive = 7.62 # 5.7912                   # m/s
g = 9.81                            # m/s^2 

#Aircraft paramters 
weightAirplane = 12640*9.81 # 21869 * 9.81       # N
VCruise = 228.3                     # m/s
mac = 2.90                          # m 
wingArea = 98                       # m^2


#InitialCalculation
V_b = np.sqrt((weightAirplane*2)/(wingArea*rhoCruise*CLMax))
VDive = 1.25*VCruise
wingLoading = weightAirplane/wingArea
print(f"WingLoading {wingLoading}")

#Calculations for gust diagram 

def calculateDeltaN (rho, V, C_Lalpha, W, u_hat): 
    
    mu_g = (2*(W/wingArea))/(rho*g*C_Lalpha*mac) 
    
    K = (0.88*mu_g)/(5.3+mu_g)
    
    u =K*u_hat
    
    deltaN = (rho*V*C_Lalpha*u)/(2*(W)/(wingArea))
    
    return deltaN
    
delta_n_stall = calculateDeltaN(rhoCruise, V_b, CLAlphaCruise, weightAirplane, uHatHighAlpha)
delta_n_cruise = calculateDeltaN(rhoCruise, VCruise, CLAlphaCruise, weightAirplane, uHatCruise)
delta_n_dive = calculateDeltaN(rhoCruise, VDive, CLAlphaCruise, weightAirplane, uHatDive)

print(delta_n_cruise, delta_n_stall, delta_n_cruise, delta_n_dive)


x = [0, V_b, VCruise, VDive]
y = [1, 1+delta_n_stall, 1+delta_n_cruise, 1+delta_n_dive]
z = [1, 1-delta_n_stall, 1-delta_n_cruise, 1-delta_n_dive]

print(V_b,VDive)


#Calculations for manoeuvre diagram


def ncurve (rho, C_LMAX, ws):
    q = 0.5 * rho 
    n = C_LMAX * q / ws
    return n

Nmax = 2.1 + (24000/(weightAirplane*2.205 + 10000)) #It must be converted to pounds
print(f"nMax = {Nmax}")
Nmin = -1
n = ncurve (rhoCruise, CLMax, wingLoading)


V_a = np.sqrt(Nmax/n)

V_vals_1 = np.linspace(0, V_a, 100)  # Velocity values for the positive parabolic portion
V_vals_2 = np.linspace(V_a, VDive, 100)  # Velocity values for the straight line portion at n_max
V_vals_neg_1 = np.linspace(0, VCruise, 100)  # Velocity values for the negative parabolic portion
V_vals_neg_2 = np.linspace(VCruise, VDive, 100)  # Straight line segment from (Vc, -1) to (Vd, 0)

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
V_vals_vert = [VDive, VDive]  # Velocity for vertical line
n_vals_vert_pos = [Nmax, 0]  # Positive vertical line

# Plotting
plt.plot(x,y, color="red")
plt.plot(V_vals_1, n_vals_1, color='blue')
plt.plot(x, z, color = "red")
plt.plot(V_vals_2, n_vals_2, color='blue')
plt.plot(V_vals_vert, n_vals_vert_pos, color='blue')  # Vertical line for positive load

plt.plot(V_vals_neg_1, n_vals_neg_1, color='blue')
plt.plot(V_vals_neg_2, n_vals_neg_2, color='blue')




# Show plot
plt.xlabel("Velocity [m/s]")
plt.ylabel("Load factor")
plt.title("V,n diagram")
plt.grid(True)  
plt.legend(["Gust diagram", "Maneuver diagram"], loc="upper left")
plt.show()
