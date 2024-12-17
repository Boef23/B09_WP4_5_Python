"""I_xx, I_yy calculation"""
from Parameters import * 

a = 0.01  #[m] width of the stringers 
t_s = 0.001  #[m] thickness of the stringers
c = 4.9 #This must be changed to a function 
L_wb = 0.5*c #Length rectangularsised wing box
H_wb = 0.0732*c #HeightRectangularsied wing box 
t_wb = 0.001 #[m] thickness of the wingbox 
m = 16
n = 15
j = 11
k = 10

#Centroid determination 

def calculate_Centroid(L_wb, H_wb, t_wb, t_s, a, m, n, j, k):
    A = (L_wb*2 + H_wb*2) * t_wb  #Area wing box
    
    #Y centroid I need to check these formulas
    if m >= n:
        y_centroid = ((A+2*(2*n+j+k)*t_s*a) * H_wb/2 + (m-n)*2*t_s*a*0.25*a)/(A+(n+m+k+j)*2*t_s*a)
    if n>m:
         y_centroid = ((A+2*(2*m+j+k)*t_s*a) * H_wb/2 + (n-m)*2*t_s*a*(H_wb - 0.25*a))/(A+(n+m+k+j)*2*t_s*a)
    
    #X centroid  formulas are not updated 
    if k >= j: 
         x_centroid = ((A+2*(2*n+m+k)*t_s*a) * H_wb/2 + (m-n)*2*t_s*a*0.25*a)/(A+(n+m+k+j)*2*t_s*a)
    if j < k: 
         x_centroid = ((A+2*(2*n+m+k)*t_s*a) * H_wb/2 + (m-n)*2*t_s*a*0.25*a)/(A+(n+m+k+j)*2*t_s*a)
