import particle
import matplotlib.pyplot as plt

p1 = particle.Particle()
p1.__init__()

lista_vremena = []
lista_gresaka = []

for i in range(100):
    p1.set_initial_conditions(0.0, 0.0, 10.0, 60.0)
    dt = i/100
    lista_vremena.append(dt)
    ana_domet = p1.analit_dom()
    num_dom = p1.range_pogreske(dt)
    pogreska = ((abs(ana_domet-num_dom))/ana_domet)*100
    lista_gresaka.append(pogreska)
    p1.reset()

fig, axs = plt.subplots()
axs.set_xlabel("dt [s]")
axs.set_ylabel("Relativna pogreška [%]")
axs.plot(lista_vremena, lista_gresaka)
axs.set_title("Graf relativne pogreske dometa projektila")
plt.show()   



