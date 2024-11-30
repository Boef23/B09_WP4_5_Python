from Moment_of_Inertia2 import *
from Moment_of_inertia_comp import *



I_XX_Zlist = []
I_YY_Zlist = []
J_Zlist = []
zlist = np.arange(0, 1.01, 0.01)
I_XX_Zlist, I_YY_Zlist, J_Zlist = geometryproperties(zlist)


plt.subplot(1,3,1)
plt.plot(zlist,I_XX_Zlist)
plt.title('I_XX')
plt.xlabel('Z postion')
plt.ylabel('I_XX')
plt.grid(True)

plt.subplot(1,3,2)
plt.plot(zlist,I_YY_Zlist)
plt.title('I_YY')
plt.xlabel('Z postion')
plt.ylabel('I_YY')
plt.grid(True)

plt.subplot(1,3,3)
plt.plot(zlist,J_Zlist)
plt.title('J')
plt.xlabel('Z postion')
plt.ylabel('J')
plt.grid(True)

plt.show()



