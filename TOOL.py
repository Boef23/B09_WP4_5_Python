import numpy as np
import matplotlib.pyplot as plt

#################################################################################################################################
#Tool
#zAxis
zAxis = np.arange(0, 15.325, 0.01)

#PLots?
Plots = False
#Compare Applied with Critical

#Ixx, Iyy, J
#I_XX_Zlist, I_YY_Zlist, J_Zlist =
if __name__ == '__main__':
    if Plots == True:
        plt.subplot(1,3,1)
        plt.plot(zAxis,I_XX_Zlist)
        plt.title('I_XX [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('I_XX [m^4]')
        plt.grid(True)

        plt.subplot(1,3,2)
        plt.plot(zlist,I_YY_Zlist)
        plt.title('I_YY [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('I_YY [m^4]')
        plt.grid(True)

        plt.subplot(1,3,3)
        plt.plot(zlist,J_Zlist)
        plt.title('J [m^4]')
        plt.xlabel('Z postion [m]')
        plt.ylabel('J [m^4]')
        plt.grid(True)

        plt.show()


#LC1

#LC2

#LC3

#LC4

#Deflection

#Twist