import matplotlib.pyplot as plt
import numpy as np
import math
import electromagnetic as emg
p1 = emg.particles()
def vektor(x, y, z):
    return np.array([x, y, z])
p1.set_initial_conditions(vektor(0.1, 0.1, 0.1), 1.0, vektor(0.0, 0.0, 0.0), vektor(0.0, 0.0, 1.0), -1.0)
x, y, z = p1.Euler_method(10.0)
x1, y1, z1 = p1.Runge_Kutta_method(10.0)

fig = plt.figure()
axs = plt.axes(projection='3d')

axs.set_title("Euler vs Runge Kutta")
axs.set_xlabel("x")
axs.set_ylabel("y")
axs.set_zlabel("z")

axs.plot(x, y, z, 'b')
axs.plot(x1, y1, z1, 'g--')
plt.show()