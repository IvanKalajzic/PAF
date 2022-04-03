import calculus as cal
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return x**3

def f2(x):
    return np.sin(x)  

x1, dfx1 = cal.deriv2(f1, 0, 10, 0.01, 3)
x2, dfx2 = cal.deriv2(f2, 0, 10, 0.01, 3)
x1x, dfx1x = cal.deriv2(f1, 0, 10, 1, 2)
x2x, dfx2x = cal.deriv2(f2, 0, 10, 1, 2) 
x1x1, dfx1x1 = cal.deriv2(f1, 0, 10, 0.5, 3)
x2x2, dfx2x2 = cal.deriv2(f2, 0, 10, 0.5, 2)
x = np.linspace(0, 10, 50)
an1 = 3*(x**2)
an2 = np.cos(x)

fig, axs = plt.subplots(2)

axs[0].plot(x1, dfx1, 'bo')
axs[0].plot(x1x, dfx1x, 'r--')
axs[0].plot(x1x1, dfx1x1, 'g^')
axs[0].plot(x, an1)
axs[0].set_title("derivacije tocaka kubne funkcije")

axs[1].plot(x2, dfx2, 'bo')
axs[1].plot(x2x, dfx2x, 'r--')
axs[1].plot(x2x2, dfx2x2, 'g^')
axs[1].plot(x, an2)
axs[1].set_title("derivacije tocaka sinusne funkcije")

plt.show()



