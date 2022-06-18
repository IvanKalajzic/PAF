import matplotlib.pyplot as plt
import harmonic_oscilator as osc
p1 = osc.HarmonicOscilator()
p2 = osc.HarmonicOscilator()
p3 = osc.HarmonicOscilator()

p1.set_initial_conditions(100.0, 1.0, 0.0, 3.0, 0.0, 0.0, 0.1)
p1.period(3)
p1.periodA()

p2.set_initial_conditions(100.0, 1.0, 0.0, 3.0, 0.0, 0.0, 0.01)
p2.period(3)
p2.periodA()

p3.set_initial_conditions(100.0, 1.0, 0.0, 3.0, 0.0, 0.0, 0.001)
p3.period(3)
p3.periodA()


