from Parameters import * 

def Ixx_Fs():
    Ixx_Fs = (t_Fs * h_Bs ** 3)/12 + t_Fs * h_Bs * (0.5 * h_Bs - y_centroid) ** 2
    #From geometry function, h_Bs is used instead of h_Fs due to assumption
    return Ixx_Fs

def Ixx_Top():
    Ixx_Top = (l_Top * t_Top ** 3)/12 + l_Top * t_Top * y_centroid ** 2
    #From geometry function
    return Ixx_Top

def Ixx_Bs():
    Ixx_Bs = (t_Bs * h_Bs ** 3)/12 + t_Bs * h_Bs * (0.5 * h_Bs - y_centroid) ** 2
    #From geometry function
    return Ixx_Bs

def Ixx_Bottom():
    Ixx_Bottom = (l_Bottom * t_Bottom ** 3)/12 + l_Bottom * t_Bottom * (h_Bs - y_centroid) ** 2
    #From geometry function
    return Ixx_Bottom

def Ixx_Stringers():
    Ixx_Stringers = (n_Str_Top(i) + n_Str_Bottom(i)) * Ixx_Local_Stringer + 
    #From list of number of stringers per side and i is increment value to later put this in a loop per bay.
    #Ixx_Local_Stringer is from local inertia function
