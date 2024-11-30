import scipy
import numpy as np
import scipy.integrate
import scipy.interpolate
import sympy
from scipy.integrate import quad,  dblquad
from sympy import symbols, integrate, lambdify
from LiftDistribution import LiftCurve
from Parameters import b
from ShearDiagram import reactionMoment, reactionShear, totalTorqueDist, zAxis, dz
from Moment_of_Inertia2 import *
from Moment_of_inertia_comp import zlist, geometryproperties


momentOfInertia_X, momentOfInertia_Y, momentOfInertia_J = geometryproperties(zlist)

def liftDistribution(z):
    divison =  scipy.interpolate.interp1d(zAxis, LiftCurve(zAxis)/momentOfInertia_X, kind= "linear", fill_value= "extrapolate")
    return divison(z)
print(liftDistribution)

def integral_1(z):

    return scipy.integrate.quad(liftDistribution,0,z)[0]
def integral_2():
    return scipy.integrate.quad(integral_1,13, 15)[0]

print(integral_2())