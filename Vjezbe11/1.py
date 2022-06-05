import matplotlib.pyplot as plt
import numpy as np
import math
import gravity as grt
p1 = grt.SunEarth()
def vektor(x, y):
    return np.array([x, y])
p1.set_initial_conditions(vektor(0, 0), vektor(0, 29783), vektor(1.486*((10)**11), 0), vektor(0, 0))
x, y, x1, y1 = p1.Euler_method(365.0)
fig, axs = plt.subplots()

axs.plot(x, y)
axs.plot(x1, y1)
axs.set_title("sun-earth")

plt.show()
