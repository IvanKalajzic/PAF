import matplotlib.pyplot as plt
import harmonic_oscilator as osc
p1 = osc.HarmonicOscilator()
p1.__init__()
p1.set_initial_conditions(1000.0, 0.5, 0.0, 3.0, 0.0, 0.0, 0.01)
print(p1.period())
