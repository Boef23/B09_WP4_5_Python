import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from LiftDistribution import chord, LiftCurve
from Parameters import mlg_Pos, b, z_Engine_Frac, engine_Mass, c_Root, taper_Ratio

# General variables
lgEndPos = mlg_Pos     # End of MLG wrt half span
dz = 0.01           # plot increment
span = b        # Full wing span
halfSpan = b/2       # m, half the full wing span
zEngineFrac = z_Engine_Frac      # fraction of position of engine wrt. half-span
zEngine = zEngineFrac * halfSpan    # position of engine on half-span

Cr = c_Root     #m, root chord
taper = taper_Ratio     #Wing taper ratio

MTOM = 23731    # kg, max take off mass
fuelFrac = 0.164    # -, fuel fraction of MTOM
wingMass = 3780     # kg, wing structural mass

fuelWeight = fuelFrac * MTOM * 9.81
wingWeight = wingMass * 9.81

# General z axis
zAxis = np.arange(0, halfSpan, dz)

# Distribution functions
def WingWeight(z):
    return chord(z) / Cr * 4 * (fuelWeight + wingWeight) / (3 * span * taper + 2 * span)


def MLGWeight(z):
    if z > lgEndPos:
        return 0
    else:
        return 302.67 * 9.81 / lgEndPos


def WingWeightMoment(z):
    return WingWeight(z) * z


def MLGWeightMoment(z):
    return MLGWeight(z) * z


def LiftMoment(z):
    return z * LiftCurve(z)


def LiftTorque(z):
    return 0.192 * LiftCurve(z) * chord(z)


# Distributed loads along wing
WingWeightDist = WingWeight(zAxis)      # Wing structural + fuel weight distributions

MLGWeightDist = np.zeros_like(zAxis)
for z in range(int(lgEndPos / dz)):
    MLGWeightDist[z] = 302.67 * 9.81 / lgEndPos     # MLG weight distribution

LiftDistribution = LiftCurve(zAxis)     # Lift distribution along wing

# Total distributed vertical load
TotDist = LiftDistribution - WingWeightDist - MLGWeightDist     # Sum of all distributed loads


# Reaction force/moment/torque magnitudes
engineWeight = engine_Mass * 9.81
reactionShear = sp.integrate.quad(WingWeight, 0, halfSpan)[0] + sp.integrate.quad(MLGWeight, 0, halfSpan)[0] + engineWeight - sp.integrate.quad(LiftCurve, 0, halfSpan)[0]    # N

reactionMoment = sp.integrate.quad(LiftMoment, 0, halfSpan)[0] - sp.integrate.quad(WingWeightMoment, 0, halfSpan)[0] - sp.integrate.quad(MLGWeightMoment, 0, halfSpan)[0] - engineWeight * zEngine             # Nm

engineTorque = 68250            # Nm
reactionTorque = sp.integrate.quad(LiftTorque, 0, halfSpan)[0] + engineTorque              # Nm


# Engine shear contribution (point force)
engineWeightDist = np.zeros_like(zAxis)
for z in range(int(zEngine/dz), zAxis.size):    # Engine weight contribution to shear distribution
    engineWeightDist[z] = -engineWeight

# Reaction shear/moment/torque contribution (point force/moment)
reactionShearDist = np.ones_like(zAxis) * reactionShear         # N
reactionMomentDist = np.ones_like(zAxis) * reactionMoment       # Nm
reactionTorqueDist = np.ones_like(zAxis) * reactionTorque       # Nm


# Shear Diagram Calculations
incrementalShear = TotDist * dz     # Load per unit span * incremental step
for z in range(1, zAxis.size):
    incrementalShear[z] += incrementalShear[z-1]    # Account for all previous contributions

totalShearDist = reactionShearDist + engineWeightDist + incrementalShear    # Total shear distribution along wing


# Moment Diagram Calculations
incrementalMoment = totalShearDist * dz     # Moment per unit span * incremental step
for z in range(1, zAxis.size):
    incrementalMoment[z] += incrementalMoment[z-1]  # Account for all previous contributions

totalMomentDist = incrementalMoment + reactionMomentDist    # Total moment distribution along wing


# Torque Diagram Calculations
engineTorqueDist = np.ones_like(zAxis)
for z in range(int(zEngine/dz), zAxis.size):        # Account for engine torque contribution
    engineTorqueDist[z] = engineTorque

incrementalTorque = LiftTorque(zAxis) * dz          # Torque per unit span * incremental step
for z in range(1, zAxis.size):
    incrementalTorque[z] += incrementalTorque[z-1]  # Account for all previous contributions

totalTorqueDist = reactionTorqueDist - engineTorqueDist - incrementalTorque     # Total torque distribution along wing


# Internal Loading Plots
if __name__ == '__main__':
    # Plot shear diagram
    plt.subplot(1, 3, 1)
    plt.plot(zAxis, totalShearDist / 1000, label='Shear')
    plt.axhline(0, color='black', linestyle='-')
    plt.ylabel('V [kN]')
    plt.xlabel('z [m]')
    plt.title('Shear vs. Semi-Span Position')

    # Plot moment diagram
    plt.subplot(1, 3, 2)
    plt.plot(zAxis, totalMomentDist / 1000, label='Moment')
    plt.axhline(0, color='black', linestyle='-')
    plt.ylabel('M [kNm]')
    plt.xlabel('z [m]')
    plt.title('Moment vs. Semi-Span Position')

    # Plot torque diagram
    plt.subplot(1, 3, 3)
    plt.plot(zAxis, totalTorqueDist / 1000, label='Torque')
    plt.axhline(0, color='black', linestyle='-')
    plt.ylabel('T [kNm')
    plt.xlabel('z [m]')
    plt.title('Torque vs. Semi-Span Position')

    plt.tight_layout()

    plt.show()

