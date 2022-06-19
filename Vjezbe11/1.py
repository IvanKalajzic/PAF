import matplotlib.pyplot as plt
import numpy as np
import math
import gravity as grt
p1 = grt.SunEarth()
def vektor(x, y):
    return np.array([x, y])
p1.set_initial_conditions(vektor(0, 0), vektor(0, 29783), np.array([1.486*10**(11), 0]), np.array([0.1, 0.1]))
x, y, x1, y1 = p1.Euler_method()
fig, axs = plt.subplots(figsize=(6,6))
axs.plot(x, y)
axs.plot(x1, y1)
axs.legend(["Zemlja", "Sunce"])
axs.set_title("Zemlja-Sunce")
axs.set_xlabel("x")
axs.set_ylabel("y")
plt.show()