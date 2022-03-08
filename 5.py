
import matplotlib.pyplot as plt
import numpy as np
def jedn_pravca2( x1 = int(input(" ")),  y1 = int(input(" ")),  x2 = int(input(" ")),  y2 = int(input(" "))):

    x = np.linspace(-20, 20, 20)
    k = (y2-y1)/(x2-x1)
    l = y1-k*x1
    y = k*x+l

    izbor = input("Ako zelite prikazati sliku stisnite 'p', a ako je zelite spremiti stisnite 's': ")

    if (izbor == "p"):
        plt.plot(x, y)
        plt.plot(x1, y1, 'bo')
        plt.plot(x2, y2, 'bo')
        plt.show()
    if (izbor == "s"):
        ime_slike = input("Pod kojim imenom zelite spremiti sliku: ")
        plt.plot(x, y)
        plt.plot(x1, y1, 'bo')
        plt.plot(x2, y2, 'bo')
        plt.savefig('{}.pdf'.format(ime_slike))
    
    return k, l
jedn_pravca2()




    