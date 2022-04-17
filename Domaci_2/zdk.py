import modul as mod
import numpy as np
import matplotlib.pyplot as plt

def jednoliko(v, s, t):
    return 8.0

def harmonijsko(v, s, t):
    return -12.0*s    

p1 = mod.Gibanje(jednoliko, 3.0, 0.0, 0.0, 0.0)
p2 = mod.Gibanje(harmonijsko, 3.0, 0.0, 0.5, 0.0)

p1.graf()
p2.graf()


