import numpy as np
import matplotlib.pyplot as plt
import Projectile as pro
p1 = pro.projectile()
p2 = pro.projectile()

lista_C = []
lista_dometa = []
lista_m = []
lista_dometa1 = []

for i in range(0, 401, 100):
    c = i/100
    lista_C.append(c)
    p1.set_initial_conditions(0.0, 0.0, 30.0, 60.0, c, 1.22, 0.5, 3.0, 0.01)
    lista_dometa.append(p1.Domet())

for i in range(1, 1001, 100):
    M = i/100
    lista_m.append(M)
    p2.set_initial_conditions(0.0, 0.0, 30.0, 60.0, 1.4, 1.22, 0.5, M, 0.01)
    lista_dometa1.append(p2.Domet())

fig, axs = plt.subplots(2)
axs[0].plot(lista_C, lista_dometa, 'b-')
axs[0].set_title("Ovisnost dometa o koeficijentu trenja")
axs[0].set_xlabel("Koeficijent trenja")
axs[0].set_ylabel("Domet/m)")

axs[1].plot(lista_m, lista_dometa1, 'g-')
axs[1].set_title("Ovisnost dometa o masi cestice")
axs[1].set_xlabel("Masa/kg")
axs[1].set_ylabel("Domet/m")

plt.show()    


