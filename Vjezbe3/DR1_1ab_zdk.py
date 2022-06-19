import particle as prt
p1 = prt.Particle()
p1.__init__()
p1.set_initial_conditions(0.0, 0.0, 10.0, 60.0)
print(p1.total_time())
print(p1.max_speed())
