import numpy as np
import matplotlib.pyplot as plt
from appliedStress import *
#from DeflectionFinal import *
from TwistFinal import *
from ColumnBuckling import *
from Moment_of_inertia_3 import *

def marginofsafety(failuresigma, appliedsigma):
    marginofsafety = (failuresigma)/(appliedsigma)
    return marginofsafety


def areastringer(t_Str_a = t_Str_a, a_Str = a_Str, t_Str_b = t_Str_b, b_Str = b_Str):
    areastringer = t_Str_a * a_Str + t_Str_b + b_Str
    return areastringer

zAxis = np.arange(0, 15.325, 0.01)

I_XX_Zlist = Ixx_list
I_YY_Zlist = I_yy_Total
J_Zlist = I_XX_Zlist + I_YY_Zlist


LC1list = zAxis
LC2list = zAxis
LC3list = columnBuckling(K , elasticModulus, Ixx = Ixx_list, stringerArea = areastringer()  )
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


#LC1
margin_LC1 = marginofsafety(LC1list,tau_max_force)
#LC2
margin_LC2 = marginofsafety(LC2list,normalStress)
#LC3
margin_LC3 = marginofsafety(LC3list,normalStress)
#LC4
margin_LC4 = marginofsafety(LC4list,normalStress)
'''
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
'''
#PLOTS

if __name__ == '__main__':
    if Plots == True:
        plt.subplot(2,2,1)
        plt.plot(zAxis,margin_LC1)
        plt.title('Margin of Stress LC1')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.subplot(2,2,2)
        plt.plot(zAxis,margin_LC2)
        plt.title('Margin of Stress LC2')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)

        plt.subplot(2,2,3)
        plt.plot(zAxis,margin_LC3)
        plt.title('Margin of Stress LC3')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.subplot(2,2,4)
        plt.plot(zAxis,margin_LC4)
        plt.title('Margin of Stress LC4')
        plt.xlabel('Z postion [m]')
        plt.ylabel('Margin of Stress [-]')
        plt.grid(True)


        plt.show()