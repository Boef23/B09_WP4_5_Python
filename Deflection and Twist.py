"""Still needed: Ixx as a function of z, and the dimensions of the wingbox at root and tip"""


import scipy
import numpy as np
import scipy.integrate
import sympy
from scipy.integrate import quad,  dblquad
from sympy import symbols, integrate, lambdify
from LiftDistribution import LiftCurve
from Parameters import b
from ShearDiagram import reactionMoment, reactionShear, totalTorqueDist, zAxis, dz
from Moment_of_Inertia2 import total_Inertia_XX
print(total_Inertia_XX)

#import constants from file




e = 16.3
f = -365.47
landingGearLength = 2.3461 #m
Ry = reactionShear #N
elasticModulus = 72.4 * 10**9 # Pa
shearModulus = 28 * 10**9 #Pa
I_xx = 10 * 10 ** -5 #mm^4
I_xxAtRoot = 10
I_xxAtTip = 5
J_z = 1
massLandingGear = 302.67
massEngine = 1111.3
gravity = 9.80665
l_1 = 10
dl_1 = 3
t_1 = 0.001
l_2 = 20
dl_2 = 4
t_2 = 0.001
l_3 = 3
dl_3 = 1
t_3 = 0.001
l_4 = 1
dl_4 = 0
t_4 = 0.001
wingboxLength = b/2 #metres
thickness = 2 * 10**(-3) #metres
z = symbols('z')
secondMomentOfInertia = total_Inertia_XX

def wingWeightDistribution(e,f,z):#gives the Mccauley of the wingweight
    return (e*z + f)*z**3

def landingGearWeightDistribution(massLandingGear,gravity,L,z): #gives the Mccauley of the landing gear, distinction between locations are made later
    return (massLandingGear*gravity/landingGearLength)*z**2

def engineWeight(massEngine, gravity): #gives the Mccauley of the Engine
    return (massEngine*gravity)*z

def reactionY(Ry,z): #gives the Mccauley of the reaction force in the y-direction, calculated from summing all the forces
    return Ry*z
def Ixxchanger(I_xxAtRoot, I_xxAtTip, wingboxLength, z):
    Ixx = I_xxAtRoot - (I_xxAtRoot - I_xxAtTip)*z/wingboxLength
    return Ixx
Ixx = Ixxchanger(I_xxAtRoot, I_xxAtTip, wingboxLength, z)

    




#The following fuctions serve the single purpose of integrating. No constants are added as the boundary conditions state that the integration constants are zero
#The integrations are done sepereatley and are added later


def integral_1(z):
    return scipy.integrate.quad(LiftCurve / secondMomentOfInertia,0,z)[0]
def integral_2(z):
    return scipy.integrate.quad(integral_1,0,z)[0]

print(integral_2(wingboxLength),"bonjour")

def vWingWeight(wingWeightDistribution): #deflection for the wingweight
    # Perform symbolic integration
    vprimeWing_symbolic = integrate(wingWeightDistribution(e, f, z) / secondMomentOfInertia, z)

    # Convert to a numerical function
    vprimeWing_numeric = lambdify(z, vprimeWing_symbolic, 'numpy')

    # Perform numerical integration over [0, halfwingspan]
    vWing, error = quad(vprimeWing_numeric, 0, wingboxLength)

    return vWing, vprimeWing_symbolic, vprimeWing_numeric
vWing, vprimeWing_symbolic, vprimeWing_numeric = vWingWeight(wingWeightDistribution)

def landingGear(landingGearWeightDistribution): #deflection for the landing gear
    # Perform symbolic integration
    vprimeLG_symbolic = integrate(landingGearWeightDistribution(massLandingGear,gravity,landingGearLength,z) / secondMomentOfInertia,z)

    # Convert to a numerical function
    vprimeLG_numeric = lambdify(z, vprimeLG_symbolic, 'numpy')

    # Perform numerical integration over [0, halfwingspan - landinggearposition]
    vLG, error = quad(vprimeLG_numeric, 0, wingboxLength-landingGearLength)

    return vLG, vprimeLG_symbolic, vprimeLG_numeric
vLG, vprimeLG_symbolic, vprimeLG_numeric = landingGear(landingGearWeightDistribution)

def landingGear2(landingGearWeightDistribution): #"turns off" the landing gear loading
    # Perform symbolic integration
    vprimeLG2_symbolic = integrate(landingGearWeightDistribution(massLandingGear,gravity,landingGearLength,z),z)

    # Convert to a numerical function
    vprimeLG2_numeric = lambdify(z, vprimeLG2_symbolic, 'numpy')

    # Perform numerical integration over [landinggearlocation, halfwingspan]
    vLG2, error = quad(vprimeLG_numeric, 0, 2)

    return vLG2, vprimeLG2_symbolic, vprimeLG2_numeric
vLG2, vprimeLG2_symbolic, vprimeLG2_numeric = landingGear2(landingGearWeightDistribution)

def engine(engineWeight): #deflection for the engines
    # Perform symbolic integration
    vprimeE_symbolic = integrate(engineWeight(massEngine, gravity),z)

    # Convert to a numerical function
    vprimeE_numeric = lambdify(z, vprimeE_symbolic, 'numpy')

    # Perform numerical integration over [0, 1]
    vE, error = quad(vprimeE_numeric, 0, 1)

    return vE, vprimeE_symbolic, vprimeE_numeric
vE, vprimeE_symbolic, vprimeE_numeric = engine(engineWeight)

def verticalReaction(reactionY): #deflection for the reactionforce
    # Perform symbolic integration
    vprimeR_symbolic = integrate(reactionY(Ry,z),z)

    # Convert to a numerical function
    vprimeR_numeric = lambdify(z, vprimeR_symbolic, 'numpy')

    # Perform numerical integration over [0, 3]
    vR, error = quad(vprimeR_numeric, 0, 3)

    return vR, vprimeR_symbolic, vprimeR_numeric
vR, vprimeR_symbolic, vprimeR_numeric = verticalReaction(reactionY)


def momentOfInertia(Ixx): #deflection for the reactionforce
    # Perform symbolic integration
    vprimeIxx_symbolic = integrate(Ixx,z)

    # Convert to a numerical function
    vprimeIxx_numeric = lambdify(z, vprimeIxx_symbolic, 'numpy')

    # Perform numerical integration over [0, 3]
    vIxx, error = quad(vprimeIxx_numeric, 0, 3)

    return vR, vprimeR_symbolic, vprimeR_numeric

vIxx, vprimeIxx_symbolic, vprimeIxx_numeric = momentOfInertia(Ixx)




#final calculation to determine the deflection, mind sign convention
def deflectionResult(integral_2, vWingWeight, landingGear, landingGear2, engine):
    return ((-elasticModulus*I_xx)**-1)*(integral_2 + vWing + vLG - vLG2 +vE + vR)

#Twist equations
#Now the twist is calculated, this is a fucntion of z, maximum twist is most important
def torqueIntegrator(totalTorqueDist): #defines the torque as a function of z
    scipy.integrate.quad(integral_1,0,z)[0]
    return Torque

def lineIntegralCalculator(l_1, l_2, dl_1, dl_2,l_3, l_4, dl_3, dl_4, wingboxLength, t_1, t_2 ,t_3 ,t_4, z):
    lineIntegral = ((l_1 - z * (l_1 - dl_1)/wingboxLength)/t_1 + (l_2 - z * (l_2 - dl_2)/wingboxLength)/t_2 + (l_3 - z * (l_3 - dl_3)/wingboxLength)/t_3 + (l_4 - z * (l_4 - dl_4)/wingboxLength)/t_4 )
    return lineIntegral
print(lineIntegralCalculator(l_1, l_2, dl_1, dl_2,l_3, l_4, dl_3, dl_4, wingboxLength, t_1, t_2 ,t_3 ,t_4, z))

def areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, z):
    enclosedArea = l_1 * l_2 - (l_1 * dl_2 + l_2 * dl_1 - dl_1 * dl_2) * z /wingboxLength
    return enclosedArea
print(areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, z))

def dividerIntegral(areaCalculator, z):
    area = areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, z)
    #leDIV = totalTorqueDist / area**2
    #return scipy.integrate.quad(leDIV,0, wingboxLength)[0]
    return area
#print(dividerIntegral(areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, z), totalTorqueDist, wingboxLength))

leDIV = totalTorqueDist / areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, zAxis)**2 * lineIntegralCalculator(l_1, l_2, dl_1, dl_2,l_3, l_4, dl_3, dl_4, wingboxLength, t_1, t_2 ,t_3 ,t_4, zAxis)#makes a Riemann sum for the array
sumTorque = np.sum(leDIV * dz) / ( 4 * shearModulus)
print(f'Torque sum: {sumTorque}')

#twist = 0.25 * lineIntegralCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, thickness, z) *torqueIntegrator / (shearModulus * areaCalculator(l_1, l_2, dl_1, dl_2, wingboxLength, z) **2 )













































print(vWing) #prints for the wing weight
print("Symbolic Integral (vprime_symbolic):", vprimeWing_symbolic)
print(vLG) #print for the landing gear
print("Symbolic Integral (vprime_symbolic):", vprimeLG_symbolic)
print(vLG2) #prints for the turning off of the landing gear
print("Symbolic Integral (vprime_symbolic):", vprimeLG2_symbolic)
print(vE) #prints for the engines
print("Symbolic Integral (vprime_symbolic):", vprimeE_symbolic)
print(vR) #prints for the reaction force
print("Symbolic Integral (vprime_symbolic):", vprimeR_symbolic)

print(deflectionResult(integral_2(wingboxLength), vWing, landingGear, landingGear2, engine)) #prints the final result