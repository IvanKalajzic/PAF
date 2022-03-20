import numpy as np
import matplotlib.pyplot as plt
import math

def jednoliko_gibanje(F, m):
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

    axs[1].plot(lista_vremena, lista_brzina)
    axs[1].set_title("v-t")

    axs[2].plot(lista_vremena, lista_akceleracija)
    axs[2].set_title("a-t")

    plt.show()    

    return a


def kosi_hitac(v0, theta):
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

    axs[1].plot(lista_vremena, lista_dometa)
    axs[1].set_title("x-t")

    axs[2].plot(lista_vremena, lista_visina)
    axs[2].set_title("Y-t")

    plt.show()   

    return

 
       



