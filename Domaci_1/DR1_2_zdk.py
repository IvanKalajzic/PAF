import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1 = prt.Particle()
p1.__init__()
lista_kuteva = []
lista_dometa = []
lista_vremena = []

def graf_domet_vrijeme_kut():
    for i in range(180):
        d_theta = i
        lista_kuteva.append(d_theta)

        p1.set_initial_conditions(0.0, 0.0, 30.0, d_theta)

        lista_dometa.append(p1.range_d())
        lista_vremena.append(p1.range_t())

    fig, axs = plt.subplots(2)

    axs[0].plot(lista_kuteva, lista_dometa)
    axs[0].set_title("ovisnost dometa i kuta")

    axs[1].plot(lista_kuteva, lista_vremena)
    axs[1].set_title("ovisnost vremena i kuta")

    plt.show()

    return

graf_domet_vrijeme_kut()    

    
   