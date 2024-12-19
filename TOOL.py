import numpy as np
import matplotlib.pyplot as plt
from appliedStress import *
from DeflectionFinal import *
from TwistFinal import *

def marginofsafety(failuresigma, appliedsigma):
    marginofsafety = (failuresigma)/(appliedsigma)
    return marginofsafety
#################################################################################################################################
#Tool
#zAxis
zAxis = np.arange(0, 15.325, 0.01)

#PLots?
Plots = True
#Compare Applied with Critical

#Ixx, Iyy, J
I_XX_Zlist, I_YY_Zlist, J_Zlist = #Need From Martijn
if __name__ == '__main__':
    if Plots == True:
        plt.subplot(1,3,1)
        plt.plot(zAxis,I_XX_Zlist)
        plt.title('I_XX [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('I_XX [m^4]')
        plt.grid(True)

        plt.subplot(1,3,2)
        plt.plot(zAxis,I_YY_Zlist)
        plt.title('I_YY [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('I_YY [m^4]')
        plt.grid(True)

        plt.subplot(1,3,3)
        plt.plot(zAxis,J_Zlist)
        plt.title('J [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('J [m^4]')
        plt.grid(True)

        plt.show()


#LC1
margin_LC1 = marginofsafety(,tau_max_force)
#LC2
margin_LC2 = marginofsafety(,normalStress)
#LC3
margin_LC3 = marginofsafety(,)
#LC4
margin_LC3

#Deflection
if maxdeflectiontip <= 4.5:
    print('Deflection correct')
else:
    print('Deflection incorrect')

#Twist
if maxtwisttip <= 10:
    print('Twist correct')
else:
    print('Twist incorrect')