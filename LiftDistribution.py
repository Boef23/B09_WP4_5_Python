import numpy as np
from scipy import interpolate
import scipy as sp
import matplotlib.pyplot as plt
from Parameters import c_Root, S, taper_Ratio, b, cruise_Velocity, cruise_Density


# Parameters
rhoCruise = cruise_Density         # Cruise density, kg/m^3
velocityCruise = cruise_Velocity    # Cruise velocity, m/s
Cr = c_Root     #Wing root chord
taper = taper_Ratio #Wing taper ratio
span = b    #Wing span
loadFactor = 1


# Chord variation function
def chord(z):
    return Cr - 2 * (1 - taper) * Cr / span * z


# Generate CL values and z values from XFLR5
CLCurve = np.genfromtxt('MainWing_a=1.80_v=10.00ms.txt', skip_header=40, skip_footer=1030, usecols=(0,3))

ztab = CLCurve[:, 0]
chordTab = chord(ztab)
liftTab = 0.5 * rhoCruise * velocityCruise**2 * chordTab * CLCurve[:, 1]

# Interpolate CL function with scipy
LiftCurveInt = interpolate.interp1d(ztab, liftTab, kind='cubic', fill_value='extrapolate')

def LiftCurve(z):
    global LiftCurveInt, loadFactor
    return loadFactor * LiftCurveInt(z)

print(4 * sp.integrate.quad(LiftCurve, 0, span/2)[0] / (S * rhoCruise * velocityCruise**2))
# print(2 * sp.integrate.quad(LiftCurve, 0, span/2)[0])

#plot lift distribution
zAxis = np.arange(0, 15.325, 0.01)
plt.plot(zAxis, LiftCurve(zAxis))
plt.show()
