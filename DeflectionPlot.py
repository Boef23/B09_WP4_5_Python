from DeflectionFinal import divider, int_1, int_2
from ShearDiagram import zAxis
from Parameters import b
import matplotlib.pyplot as plt
import numpy as np


z = np.arange(0, b/2, 0.25)
value = np.ones_like(z)

for i in range(z.size):
    value[i] = int_2(z[i])

plt.plot(z, value)
plt.ylabel('Deflection [m]')
plt.xlabel('z [m]')
plt.axhline(0, color='black', linestyle='-')
plt.title('Deflection vs. Semi-Span Position')
plt.show()
