import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_t = []
        self.lista_a = []
        self.dt = 0.01
        self.g = 9.81

    def set_initial_conditions(self, x0, y0, v0, theta, t0):
        self.lista_a.append(g)
        self.lista_x.append(x0)
        self.lista_y.append(y0)
        self.lista_t.append(t0)
        self.V0x = np.cos(theta*np.pi/180)*v0
        self.V0y = np.sin(theta*np.pi/180)*v0

    def reset(self):
        self._innit_()  

    def __move(self):
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_x.append(self.lista_x[-1]+self.V0x*self.dt)
        self.V0y = self.V0y-self.g*self.dt
        self.lista_y.append(self.lista_y[-1]+self.Vy*self.dt)

    def range(self):
        while self.lista_y[-1] >= 0:
            self.__move()

    def plot_trajectory(self):
        fig, axs = plt.subplots(1)

        axs[0].plot(self.lista_x, self.lista_y)
        axs[0].set_title("x-y")





        



        