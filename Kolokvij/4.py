import ProjectileDrop as pd
import matplotlib.pyplot as plt
import numpy as np
import math

p1 = pd.ProjectileDrop()
p2 = pd.ProjectileDrop()
p1.__init__()
p1.set_initial_conditions(2000, 200, 0.01)
print(p1.vrijeme_trajanja_pada())

lista_dt = []
lista_t = []

def graf_ovisnosti_dt_t():
    for i in range(100):
        dt = i/1000
        lista_dt.append(dt)

        p2.set_initial_conditions(2000, 200, dt)

        lista_t.append(p2.vrijeme_trajanja_pada())

    fig, axs = plt.subplots()

    axs.plot(lista_dt, lista_t)
    axs.set_title("ovisnost vrementa trajanja o koraku")


    plt.show()

    return

graf_ovisnosti_dt_t()    