import scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import scipy.interpolate
from scipy.integrate import quad,  dblquad
from LiftDistribution import LiftCurve
from Parameters import b, engine_Mass, mlg_Pos
from ShearDiagram import  reactionShear, zAxis, dz, totalMomentDist
from Moment_of_Inertia2 import *
from Moment_of_inertia_comp import zlist, geometryproperties

elasticModulus = 72.4 * 10**9 # Pa
massLandingGear = 302.67 #kg

momentOfInertia_X, momentOfInertia_Y, momentOfInertia_J = geometryproperties(zlist) #takes the geometric properties.


def divider(z): #calculates the division term and turns it into a function of z, so it can be integrated
    division = totalMomentDist / (momentOfInertia_X * elasticModulus)
    distributionFunction =  scipy.interpolate.interp1d(zAxis, division, kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)


def int_1(z):#Calculates the first integral
    def intregrand(z):
        return divider(z)
    return scipy.integrate.quad(intregrand,0,z)[0]
def int_2(z): #calculates the first intregral
    return scipy.integrate.quad(int_1,0, z)[0]

print(f'Total Deflection at tip is: {int_2(b/2)} [m]' ) #prints the deflection, takes a lot of time to compute

def int_2converter(z):
    deflection = int_2
    return deflection(z)

def int_2list(z):
    return de

#plot lift distribution
plt.plot(zAxis, int_2list(zAxis))
plt.title('Wing Deflection')
plt.xlabel('Z postion [m]')
plt.ylabel('Deflection [m]')
plt.show()
