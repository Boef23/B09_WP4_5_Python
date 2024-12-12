from Moment_of_Inertia2 import *
z=0
h_Fs, h_Bs, l_Top, l_Bottom, beta = geometry(z)
area_Fs, area_Bs, area_Top, area_Bottom, area_Total = areas_segments(h_Fs, h_Bs, l_Top, l_Bottom)
area_Stringer = calcarea_stringer()
X_Centroid, Y_Centroid = centroid(area_Fs, area_Bs, area_Top, area_Bottom, area_Total, h_Fs, h_Bs, l_Top, l_Bottom, beta)
print("X = ", X_Centroid)
print("Y = ", Y_Centroid)