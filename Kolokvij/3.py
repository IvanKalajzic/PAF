import ProjectileDrop as pd
import matplotlib.pyplot as plt
import numpy as np
import math

p1 = pd.ProjectileDrop()
p1.__init__()
p1.set_initial_conditions(2000, 200, 0.01)

x, t, vy, y = p1.range()

fig, axs = plt.subplots(2)

axs[0].plot(x, y)
axs[0].set_title("x-y")

axs[1].plot(t, vy)
axs[1].set_title("Vy-t")



plt.show()
