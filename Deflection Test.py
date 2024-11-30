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

print(len(zlist), len(zAxis))