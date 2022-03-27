import particle as prt
p1 = prt.Particle()
p1.__init__()
p1.set_initial_conditions(0, 0, 30.0, 60.0)
p1.range()
p1.plot_trajectory()
p1.odstupanje_dometa(30.0, 60.0)
p1.reset()

