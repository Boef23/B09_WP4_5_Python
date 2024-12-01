import scipy
from scipy import integrate, interpolate
import numpy as np
import scipy.integrate
import scipy.interpolate
from Parameters import b, mlg_Pos
from ShearDiagram import totalTorqueDist
from Moment_of_inertia_comp import geometryproperties, J_Zlist, zlist

shearModulus = shearModulus = 28 * 10**9 #Pa

def division(z): #calculates the division term and makes a new function of z for it
    divider = totalTorqueDist / (shearModulus * J_Zlist)
    distributionFunction = scipy.interpolate.interp1d(zlist, divider, kind = "cubic", fill_value= "extrapolate")
    return distributionFunction(z)

def integral_1(z): #calculates the integral, as there is a discontinuity at the landing gear position, two integrals are calculated
    def integrand(z):
        return division(z)
    int_1, error1 = scipy.integrate.quad(integrand, 0, mlg_Pos)
    int_2, error2 = scipy.integrate.quad(integrand, mlg_Pos, z)
    return int_1 + int_2

print(f'Total Deflection at tip is: {integral_1(b/2) * 180 / np.pi} [deg]')
