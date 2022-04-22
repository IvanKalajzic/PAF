import ProjectileDrop as pd
import matplotlib.pyplot as plt
import numpy as np
import math

p1 = pd.ProjectileDrop()
p2 = pd.ProjectileDrop()

p1.set_initial_conditions(1000, 200, 0.01)
p1.promjena_visine(2000)
p2.set_initial_conditions(2000, 100, 0.01)
p2.promjena_brzine(200)