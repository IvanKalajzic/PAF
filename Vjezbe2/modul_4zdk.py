import numpy as np
import matplotlib.pyplot as plt
import math

def kosi(v0, theta):
    lista_dometa = []
    lista_visina = []

    dt = 0.01
    x = 0
    y = 0
    g = 9.81
    Vx = np.cos(theta*np.pi/180)*v0
    Vy = np.sin(theta*np.pi/180)*v0


    while y >= 0:
        
        x = x+Vx*dt
        Vy = Vy-g*dt
        y = y+Vy*dt
        lista_dometa.append(x)
        lista_visina.append(y)


    fig, axs = plt.subplots()

    axs.plot(lista_dometa, lista_visina)
    axs.set_title("x-y")

    plt.show()   

    return


def maksimalna_visina(v0, theta):
    lista_visina = []
    
    dt = 0.01
    x = 0
    y = 0
    g = 9.81
    Vx = np.cos(theta*np.pi/180)*v0
    Vy = np.sin(theta*np.pi/180)*v0


    while y >= 0:
        
        x = x+Vx*dt
        Vy = Vy-g*dt
        y = y+Vy*dt
        lista_visina.append(y)

    print('Maksimalna visina tijela na putanji: {}m.'.format(max(lista_visina)))

    return


def domet(v0, theta):
    lista_dometa = []
    
    dt = 0.01
    x = 0
    y = 0
    g = 9.81
    Vx = np.cos(theta*np.pi/180)*v0
    Vy = np.sin(theta*np.pi/180)*v0


    while y >= 0:
        
        x = x+Vx*dt
        Vy = Vy-g*dt
        y = y+Vy*dt
        lista_dometa.append(x)
       
    print('Domet kosog hitca: {}m.'.format(lista_dometa[-1]))   


def maksimalna_brzina(v0, theta):
    
    lista_brzina = []
    dt = 0.01
    x = 0
    y = 0
    g = 9.81
    V0x = np.cos(theta*np.pi/180)*v0
    V0y = np.sin(theta*np.pi/180)*v0


    while y >= 0:
        
        x = x+V0x*dt
        V0y = V0y-g*dt
        y = y+V0y*dt
        v = math.sqrt((V0x**2)+(V0y**2))

        lista_brzina.append(v)
    

    print('Maksimalna brzina tijela tokom gibanja: {}m/s.'.format(max(lista_brzina)))   
     


def projektil_meta(s1, s2, r, v0, theta):

    lista_dometa = []
    lista_visina = []
    lista_udaljenosti = []

    dt = 0.01
    x = 0
    y = 0
    g = 9.81
    Vx = np.cos(theta*np.pi/180)*v0
    Vy = np.sin(theta*np.pi/180)*v0


    while y >= 0:
        
        x = x+Vx*dt
        Vy = Vy-g*dt
        y = y+Vy*dt
        d = math.sqrt(((s1-x)**2)+((s2-y)**2))
        lista_dometa.append(x)
        lista_visina.append(y)
        lista_udaljenosti.append(d)

    if min(lista_udaljenosti) <= r:
         print("Projektil je pogodio metu")

    else:
        print('Najmanja udaljenost projektila od mete: {}m.'.format(min(lista_udaljenosti)-r)) 
           

    krug = plt.Circle((s1, s2), r, fill = True)

    fig, ax = plt.subplots()
    ax.set_aspect(1)

    ax.add_artist(krug)
    plt.plot(s1, s2, "bo")

    ax.plot(lista_dometa, lista_visina)
    ax.set_title("x-y")
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")

    plt.show()

    return 

