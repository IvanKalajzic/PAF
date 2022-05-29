import numpy as np
import matplotlib.pyplot as plt
import math
def jednoliko_gibanje(F = 8.0, m = 2.0):
    a = F/m
    v = 0
    s = 0
    dt = 0.01
    t = 0
    lista_brzina = []
    lista_puteva = []
    lista_akceleracija = []
    lista_vremena = []
    for i in range(1000):
        v = v+a*dt
        s = s+v*dt
    
        lista_brzina.append(v)
        lista_puteva.append(s)
        lista_akceleracija.append(a)
        lista_vremena.append(t)
        t = t+dt

    fig, axs = plt.subplots(3)

    axs[0].plot(lista_vremena, lista_puteva)
    axs[0].set_title("x-t")
    axs[0].set_xlabel("Vrijeme [s]")
    axs[0].set_ylabel("Put [m]")

    axs[1].plot(lista_vremena, lista_brzina)
    axs[1].set_title("v-t")
    axs[1].set_xlabel("Vrijeme [s]")
    axs[1].set_ylabel("Brzina [m/s]")

    axs[2].plot(lista_vremena, lista_akceleracija)
    axs[2].set_title("a-t")
    axs[2].set_xlabel("Vrijeme [s]")
    axs[2].set_ylabel("Akceleracija [m/s^2]")

    plt.show()    

    return 

jednoliko_gibanje()

