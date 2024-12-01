import scipy
import numpy as np
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

momentOfInertia_X, momentOfInertia_Y, momentOfInertia_J = geometryproperties(zlist)


def divider(z):
    division = totalMomentDist / (momentOfInertia_X * elasticModulus)
    distributionFunction =  scipy.interpolate.interp1d(zAxis, division, kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)


def int_1(z):
    def intregrand(z):
        return divider(z)
    return scipy.integrate.quad(intregrand,0,z)[0]
def int_2():
    return scipy.integrate.quad(int_1,0, 5)[0]
def int_3():
    return scipy.integrate.quad(int_1,5, 10)[0]
def int_4():
    return scipy.integrate.quad(int_1,10, 13)[0]
def int_5():
    return scipy.integrate.quad(int_1,13, b/2)[0]

print(f'Total Deflection at tip is: {int_5()+int_4()+int_2()+int_3()} [m]' ) #prints the deflection, takes a lot of time to compute




#after this, the code is basically unnessecary

def liftDistribution(z): #gives the lift distribution
    divison =  scipy.interpolate.interp1d(zAxis, LiftCurve(zAxis)/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return divison(z)
print(liftDistribution)

def wingWeight(z):
    i = 0
    weightFunction = 16.3*i - 365.47
    weightList = []
    for i in zAxis + 0.001:
        weightList.append(weightFunction)
        i =+ 0.001
    distributionFunction =  scipy.interpolate.interp1d(zAxis, weightList/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)

def engineWeight(z):
    weightFunction = engine_Mass * 9.81 
    weightList = []
    for i in zAxis + 0.001:
        weightList.append(weightFunction)
        i =+ 0.001
    distributionFunction =  scipy.interpolate.interp1d(zAxis, weightList/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)

def landingGearWeight(z): 
    weightFunction = massLandingGear * 9.81 * mlg_Pos
    weightList = []
    for i in zAxis + 0.001:
        weightList.append(weightFunction)
        i =+ 0.001
    distributionFunction =  scipy.interpolate.interp1d(zAxis, weightList/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)

def landingGearWeightOff(z): #turns off the Macauley function
    weightFunction = massLandingGear * 9.81 *mlg_Pos
    weightList = []
    for i in zAxis + 0.001:
        weightList.append(weightFunction)
        i =+ 0.001
    distributionFunction =  scipy.interpolate.interp1d(zAxis, weightList/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)


def shearReaction(z):
    weightFunction = reactionShear 
    weightList = []
    for i in zAxis + 0.001:
        weightList.append(weightFunction)
        i =+ 0.001
    distributionFunction =  scipy.interpolate.interp1d(zAxis, weightList/(momentOfInertia_X * elasticModulus), kind= "cubic", fill_value= "extrapolate")
    return distributionFunction(z)

def integral_1_Lift(z):
    def intregrand(z):
        return liftDistribution(z) * z**2
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_lift():
    return scipy.integrate.quad(integral_1_Lift,0, b/2)[0]

def integral_1_Wing(z):
    def intregrand(z):
        return wingWeight(z) * z**2
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_Wing():
    return scipy.integrate.quad(integral_1_Wing,0, 1)[0]

def integral_1_Engine(z):
    def intregrand(z):
        return engineWeight(z) * z
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_Engine():
    return scipy.integrate.quad(integral_1_Engine,0, 1)[0]

def integral_1_Landing(z):
    def intregrand(z):
        return landingGearWeight(z) * z**2
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_Landing():
    return scipy.integrate.quad(integral_1_Landing,0, 1)[0]

def integral_1_LandingOff(z):
    def intregrand(z):
        return landingGearWeightOff * z**2
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_LandingOff():
    return scipy.integrate.quad(landingGearWeightOff,0, 1)[0]

def integral_1_Reaction(z):
    def intregrand(z):
        return shearReaction(z) * z
    return scipy.integrate.quad(intregrand,0,z)[0]
def integral_2_Reaction():
    return scipy.integrate.quad(integral_1_Reaction,0, 1)[0]
