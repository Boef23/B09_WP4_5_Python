import scipy
import numpy as np
import sympy
from scipy.integrate import quad
from sympy import symbols, integrate, lambdify

#import constants from file
a = 1
b = 1
c = 1
d = 1
e = 16.3
f = -365.47
g = 1
h = 1
L = 2.3461
Ry = 1
elastic = 1
I_xx = 1
J_z = 1
massLandingGear = 302.67
massEngine = 1111.3
gravity = 9.80665
z = symbols('z')

def liftDistribution(a,b,c,d,z): #gives the Mccauley of the lift
    return (a*z**3+b*z**2+c*z+d)*z**5

def wingWeightDistribution(e,f,z):#gives the Mccauley of the wingweight
    return (e*z + f)*z**3

def landingGearWeightDistribution(massLandingGear,gravity,L,z): #gives the Mccauley of the landing gear, distinction between locations are made later
    return (massLandingGear*gravity/L)*z**2

def engineWeight(massEngine, gravity): #gives the Mccauley of the Engine
    return (massEngine*gravity)*z

def reactionY(Ry,z): #gives the Mccauley of the reaction force in the y-direction, calculated from summing all the forces
    return Ry*z


#The following fuctions serve the single purpose of integrating. No constants are added as the boundary conditions state that the integration constants are zero
#The integrations are done sepereatley and are added later
def vLift(liftDistribution): #deflection for the lift
    # Perform symbolic integration
    vprime_symbolic = integrate(liftDistribution(a, b, c, d, z), z)

    # Convert to a numerical function
    vprime_numeric = lambdify(z, vprime_symbolic, 'numpy')

    # Perform numerical integration over [0, 3]
    v, error = quad(vprime_numeric, 0, 3)

    return v, vprime_symbolic, vprime_numeric
v, vprime_symbolic, vprime_numeric = vLift(liftDistribution)

def vWingWeight(wingWeightDistribution): #deflection for the wingweight
    # Perform symbolic integration
    vprimeWing_symbolic = integrate(wingWeightDistribution(e, f, z), z)

    # Convert to a numerical function
    vprimeWing_numeric = lambdify(z, vprimeWing_symbolic, 'numpy')

    # Perform numerical integration over [0, 3]
    vWing, error = quad(vprimeWing_numeric, 0, 3)

    return vWing, vprimeWing_symbolic, vprimeWing_numeric
vWing, vprimeWing_symbolic, vprimeWing_numeric = vWingWeight(wingWeightDistribution)

def landingGear(landingGearWeightDistribution): #deflection for the landing gear
    # Perform symbolic integration
    vprimeLG_symbolic = integrate(landingGearWeightDistribution(massLandingGear,gravity,L,z),z)

    # Convert to a numerical function
    vprimeLG_numeric = lambdify(z, vprimeLG_symbolic, 'numpy')

    # Perform numerical integration over [0, 3]
    vLG, error = quad(vprimeLG_numeric, 0, 3)

    return vLG, vprimeLG_symbolic, vprimeLG_numeric
vLG, vprimeLG_symbolic, vprimeLG_numeric = landingGear(landingGearWeightDistribution)

def landingGear2(landingGearWeightDistribution): #"turns off" the landing gear loading
    # Perform symbolic integration
    vprimeLG2_symbolic = integrate(landingGearWeightDistribution(massLandingGear,gravity,L,z),z)

    # Convert to a numerical function
    vprimeLG2_numeric = lambdify(z, vprimeLG2_symbolic, 'numpy')

    # Perform numerical integration over [0, 2]
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



#final calculation to determine the deflection, mind sign convention
def deflectionResult(vLift, vWingWeight, landingGear, landingGear2, engine):
    return ((-elastic*I_xx)**-1)*(v - vWing - vLG + vLG2 -vE + vR)


print(v) #print for the lift
print("Symbolic Integral (vprime_symbolic):", vprime_symbolic)
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

print(deflectionResult(vLift, vWing, landingGear, landingGear2, engine)) #prints the final result