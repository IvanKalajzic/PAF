
import calculus as cal
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return 2*x**2+3
  
gore, dole = cal.num_integracija(f1, 0, 1, 100) 
print(gore)
print(dole) 
print(cal.trapezna_integracija(f1, 0, 1, 100)) 

x = np.linspace(20, 1000, 20)
gor = []
dol = []
trapz = []
analit = []

for el in x:

    gornja, donja = cal.num_integracija(f1, 0, 1, el)
    trapez = cal.trapezna_integracija(f1, 0, 1, el)
    analiticka = 11/3

    gor.append(gornja)
    dol.append(donja)
    trapz.append(trapez)
    analit.append(analiticka)


fig, axs = plt.subplots()

axs.plot(x, gor, 'y--')
axs.plot(x, dol, 'r--')
axs.plot(x, trapz, 'g--')
axs.plot(x, analit)
axs.set_title("integral")

plt.show()








