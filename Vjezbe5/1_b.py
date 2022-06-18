import matplotlib.pyplot as plt
import harmonic_oscilator as osc
p1 = osc.HarmonicOscilator()
p2 = osc.HarmonicOscilator()
p3 = osc.HarmonicOscilator()
dtx =0.001
dtx2 = 0.01
dtx3 = 0.05
p1.set_initial_conditions(1000.0, 0.01, 1.0, 3.0, 0.0, 0.0, dtx)
p2.set_initial_conditions(1000.0, 0.01, 1.0, 3.0, 0.0, 0.0, dtx2)
p3.set_initial_conditions(1000.0, 0.01, 1.0, 3.0, 0.0, 0.0, dtx3)
x1, t1 = p1.oscilate2(3)
x2, t2 = p2.oscilate2(3)
x3, t3 = p3.oscilate2(3)

fig, axs = plt.subplots()

axs.plot(t1, x1, 'b--')
axs.plot(t2, x2, 'r--')
axs.plot(t3, x3, 'g--')
axs.set_title("Harmonijsko osciliranje")
plt.show()





