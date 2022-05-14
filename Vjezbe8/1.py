import numpy as np
import matplotlib.pyplot as plt
import Projectile as pro
p1 = pro.projectile()
p2 = pro.projectile()
p3 = pro.projectile()
p1.__init__()
p1.set_initial_conditions(0.0, 0.0, 30.0, 60.0, 1.4, 1.22, 0.5, 3.0, 0.01)
x, y = p1.Euler_method()
p2.__init__()
p2.set_initial_conditions(0.0, 0.0, 30.0, 60.0, 1.4, 1.22, 0.5, 3.0, 0.001)
x1, y1 = p2.Euler_method()
p3.__init__()
p3.set_initial_conditions(0.0, 0.0, 30.0, 60.0, 1.4, 1.22, 0.5, 3.0, 0.1)
x2, y2 = p3.Euler_method()


fig, axs = plt.subplots()
axs.plot(x, y, 'b--')
axs.plot(x1, y1, 'g--')
axs.plot(x2, y2, 'r--')
axs.set_title("x-y za različite vremenske korake")
axs.set_xlabel("x/m")
axs.set_ylabel("y/m")


plt.show()

