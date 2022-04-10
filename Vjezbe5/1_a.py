import matplotlib.pyplot as plt
import harmonic_oscilator as osc
p1 = osc.HarmonicOscilator()
p1.__init__()
p1.set_initial_conditions(1000.0, 0.5, 0.0, 3.0, 0.0, 0.0, 0.01)

a, t, v, x = p1.oscilate(3)


fig, axs = plt.subplots(3)

axs[0].plot(t, x)
axs[0].set_title("x-t")

axs[1].plot(t, v)
axs[1].set_title("v-t")

axs[2].plot(t, a)
axs[2].set_title("a-t")

plt.show()


