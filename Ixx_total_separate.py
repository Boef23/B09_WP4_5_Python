from Parameters import * 

def Ixx_Fs():
    Ixx_Fs = (t_Fs * h_Bs ** 3)/12 + t_Fs * h_Bs * (0.5 * h_Bs - y_centroid) ** 2
    #From geometry function, h_Bs is used instead of h_Fs due to assumption
    return Ixx_Fs

def Ixx_Top():
    Ixx_Top = (l_Top * t_Top ** 3)/12 + l_Top * t_top * y_centroid ** 2
    #From geometry function
    return Ixx_Top

def Ixx_Bs():
    Ixx_Bs = (t_Bs * h_Bs ** 3)/12 + t_Bs * h_Bs * (0.5 * h_Bs - y_centroid) ** 2

def Ixx_Bottom():


def Ixx_Stringers():

