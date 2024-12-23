from Moment_of_Inertia2 import *
import matplotlib.pyplot as plt
from Parameters import *
#create final function as a function of (z)

def geometryproperties(z):
    h_Fs, h_Bs, l_Top, l_Bottom, beta = geometry(z)
    area_Fs, area_Bs, area_Top, area_Bottom, area_Total = areas_segments(h_Fs, h_Bs, l_Top, l_Bottom)
    area_Stringer = calcarea_stringer()
    X_Centroid, Y_Centroid = centroid(area_Fs, area_Bs, area_Top, area_Bottom, area_Total, h_Fs, h_Bs, l_Top, l_Bottom, beta)
    X_Centroid_Fs, Y_Centroid_Fs , X_Centroid_Top, Y_Centroid_Top, X_Centroid_Bs, Y_Centroid_Bs, X_Centroid_Bottom, Y_Centroid_Bottom = local_Centroids(h_Fs, h_Bs, l_Top, l_Bottom, beta, X_Centroid, Y_Centroid)
    I_XX_Total_Plates = plate_Inertia_XX(h_Fs, h_Bs, l_Top, l_Bottom, beta, Y_Centroid_Fs, Y_Centroid_Top, Y_Centroid_Bs, Y_Centroid_Bottom)
    I_YY_Total_Plates = plate_Inertia_YY(h_Fs, h_Bs, l_Top, l_Bottom, beta, X_Centroid_Fs, X_Centroid_Top, X_Centroid_Bs, X_Centroid_Bottom)
    Spacing_Fs, Spacing_Bs, Spacing_Top, Spacing_Bottom = Calc_string_space(h_Fs, h_Bs, l_Top, l_Bottom)
    I_XX_Stringers_Fs, I_XX_Stringers_Bs, I_XX_Stringers_Top, I_XX_Stringers_Bottom = stringers_Inertia_X(Y_Centroid, area_Stringer, Spacing_Fs, Spacing_Bs, Spacing_Bottom, Y_Centroid_Top, h_Fs, beta)
    I_YY_Stringers_Fs, I_YY_Stringers_Bs, I_YY_Stringers_Top, I_YY_Stringers_Bottom = stringers_Inertia_Y(X_Centroid, area_Stringer, Spacing_Top, Spacing_Bottom, X_Centroid_Fs, X_Centroid_Bs, beta)
    I_XX_Total = total_Inertia_XX(I_XX_Total_Plates, I_XX_Stringers_Fs, I_XX_Stringers_Bs, I_XX_Stringers_Top, I_XX_Stringers_Bottom)
    I_YY_Total = total_Inertia_YY(I_YY_Total_Plates, I_YY_Stringers_Fs, I_YY_Stringers_Bs, I_YY_Stringers_Top, I_YY_Stringers_Bottom)
    J_Total = total_Inertia_J(I_XX_Total, I_YY_Total)
    return I_XX_Total, I_YY_Total, J_Total

# Run it
I_XX_Zlist = []
I_YY_Zlist = []
J_Zlist = []
zlist = np.arange(0, 15.325, 0.01)
I_XX_Zlist, I_YY_Zlist, J_Zlist = geometryproperties(zlist)

if __name__ == '__main__':
    plt.subplot(1,3,1)
    plt.plot(zlist,I_XX_Zlist)
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



