import numpy as np
import matplotlib.pyplot as plt
import math

def kosi_hitac(v0 = 30.0, theta = 80):
    lista_dometa = []
    lista_visina = []
    lista_vremena = []
    dt = 0.01
    t = 0
    x = 0
    y = 0
    g = 9.81
    Vx = np.cos(theta*np.pi/180)*v0
    Vy = np.sin(theta*np.pi/180)*v0


    for i in range(1000):
        
        x = x+Vx*dt
        Vy = Vy-g*dt
        y = y+Vy*dt
        lista_dometa.append(x)
        lista_visina.append(y)
        lista_vremena.append(t)
        t = t+dt


    fig, axs = plt.subplots(3)

    axs[0].plot(lista_dometa, lista_visina)
    axs[0].set_title("x-y")
    axs[0].set_xlabel("X [m]")
    axs[0].set_ylabel("Y [m]")

    axs[1].plot(lista_vremena, lista_dometa)
    axs[1].set_title("x-t")
    axs[1].set_xlabel("Vrijeme [s]")
    axs[1].set_ylabel("X [m]")

    axs[2].plot(lista_vremena, lista_visina)
    axs[2].set_title("Y-t")
    axs[2].set_xlabel("Vrijeme [s]")
    axs[2].set_ylabel("Y s[m]")

    plt.show()   

    return

kosi_hitac()     
       


