import numpy as np
import matplotlib.pyplot as plt
from appliedStress import *
from DeflectionFinal import *
from TwistFinal import *
from ColumnBuckling import *
from Moment_of_inertia_3 import *
from LC1andLC2 import *
from Parameters import *

def marginofsafety(failuresigma, appliedsigma):
    marginofsafety = np.abs((failuresigma)/(appliedsigma))
    return marginofsafety


def areastringer(t_Str_a = t_Str_a, a_Str = a_Str, t_Str_b = t_Str_b, b_Str = b_Str):
    areastringer = t_Str_a * a_Str + t_Str_b + b_Str
    return areastringer

zAxis = np.arange(0, 15.325, 0.01)

I_XX_Zlist = Ixx_list
I_YY_Zlist = I_yy_Total
J_Zlist = I_XX_Zlist + I_YY_Zlist


LC1_Frontlist = shearStressCriticalFront
LC1_Backlist = shearStressCriticalBack
LC2_Upperlist = skinStressCriticalCompUPPER
LC2_Lowerlist = skinStressCriticalCompLOWER
LC3list = columnBuckling(K , elasticModulus, Iyy ,stringerArea)

LC4list = np.ones_like(zAxis)*450*10**6 #Yield stress
#################################################################################################################################
#Tool
#zAxis


#PLots?
Plots = True
#Compare Applied with Critical

#Ixx, Iyy, J
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


#LC1_Front
margin_LC1_Front = marginofsafety(LC1_Frontlist,tau_max_force)
#LC2_Back
margin_LC1_Back = marginofsafety(LC1_Backlist,normalStress)
#LC2_Front
margin_LC2_Upper = marginofsafety(LC2_Upperlist,tau_max_force)
#LC2_Back
margin_LC2_Lower = marginofsafety(LC2_Lowerlist,normalStress)
#LC3
margin_LC3 = marginofsafety(LC3list,normalStress)
#LC4
margin_LC4 = marginofsafety(LC4list,normalStress)

#Deflection
print(f'Total Deflection at tip is: {maxdeflectiontip} [m]' )
if maxdeflectiontip <= 4.5:
    print('Deflection correct')
else:
    print('Deflection incorrect')

#Twist
print(f'Total Twist at tip is: {maxtwisttip} [deg]')
if maxtwisttip <= 10:
    print('Twist correct')
else:
    print('Twist incorrect')

#PLOTS

if __name__ == '__main__':
    if Plots == True:
        plt.subplot(2,3,1)
        plt.plot(zAxis,margin_LC1_Front)
        plt.title('Margin of Stress LC1_Front')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)

        plt.subplot(2,3,2)
        plt.plot(zAxis,margin_LC1_Back)
        plt.title('Margin of Stress LC1_Back')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.subplot(2,3,3)
        plt.plot(zAxis,margin_LC2_Upper)
        plt.title('Margin of Stress LC2_Upper')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)

        plt.subplot(2,3,4)
        plt.plot(zAxis,margin_LC2_Lower)
        plt.title('Margin of Stress LC2_Lower')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)

        plt.subplot(2,3,5)
        plt.plot(zAxis,margin_LC3)
        plt.title('Margin of Stress LC3')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.subplot(2,3,6)
        plt.plot(zAxis,margin_LC4)
        plt.title('Margin of Stress LC4')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.show()