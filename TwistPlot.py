from TwistFinal import division, integral_1
import matplotlib.pyplot as plt
from scipy import integrate, interpolate
import numpy as np
import scipy.integrate
import scipy.interpolate
from Parameters import b, mlg_Pos
from ShearDiagram import totalTorqueDist
from Moment_of_inertia_comp import geometryproperties, J_Zlist, zlist





zt = np.arange(0, b/2, 0.25)
value = np.ones_like(zt)

for i in range(zt.size):
    value[i] = integral_1(zt[i])

plt.plot(zt, value)
plt.ylabel('Twist [deg]')
plt.xlabel('z [m]')
plt.axhline(0, color='black', linestyle='-')
plt.title('Twist vs. Semi-Span Position')
plt.show()