import matplotlib.pyplot as plt
import numpy as np
import math
import electromagnetic as emg
p1 = emg.particles()
p2 = emg.particles()
def vektor(x, y, z):
    return np.array([x, y, z])
p1.set_initial_conditions(vektor(0.1, 0.1, 0.1), 1.0, vektor(0.0, 0.0, 0.0), vektor(0.0, 0.0, 1.0), -1.0)
p2.set_initial_conditions(vektor(0.1, 0.1, 0.1), 1.0, vektor(0.0, 0.0, 0.0), vektor(0.0, 0.0, 1.0), 1.0)
x, y, z = p1.Euler_method(15.0)
x1, y1, z1 = p2.Euler_method(15.0)

fig = plt.figure()
axs = plt.axes(projection='3d')

axs.set_title("electron vs pozitron")
axs.set_xlabel("x")
axs.set_ylabel("y")
axs.set_zlabel("z")
axs.view_init(30, 40)

axs.plot(x, y, z, 'blue')
axs.plot(x1, y1, z1, 'red')
plt.show()

