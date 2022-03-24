
import numpy as np
import matplotlib.pyplot as plt
import math

def krug_funkc(x1 = int(input("Unesite x koordinatu prve tocke: ")), y1 = int(input("Unesite y koordinatu prve tocke:  ")), s1 = int(input("Unesite x koordinatu sredista:  ")), s2 = int(input("Unesite y koordinatu sredista:  ")), r = int(input("Unesite iznos radijusa:  "))):

    d = math.sqrt(((s1-x1)**2)+(s2-y1)**2)

    if d > r:
        print("Tocka se nalazi izvan kruga")

    if d < r:
        print("Tocka se nalazi unutar kruga") 

    if d == r:
        print("Tocka se nalazi na kruznici")

    krug = plt.Circle((s1, s2), r, fill = False)

    fig, ax = plt.subplots()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    ax.set_aspect(1)

    ax.add_artist(krug)
    plt.plot(s1, s2, "bo")

    plt.show()

    return 

krug_funkc()    
