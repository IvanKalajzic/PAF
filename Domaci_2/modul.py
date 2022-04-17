import matplotlib.pyplot as plt
import numpy as np
import math

class Gibanje:
        
    def __init__(self, F, m, v0, s0, t0):
        self.dt = 0.01
        self.v0 = v0
        self.s0 = s0
        self.t0 = t0
        self.m = m
        F0 = F(v0, s0, self.dt)
        self.lista_brzina = []
        self.lista_puteva = []
        self.lista_akceleracija = []
        self.lista_vremena = []
       

        for i in range(1000):
            a = F0/m
            v0 = v0+a*self.dt
            s0 = s0+v0*self.dt
            F0 = F(v0, s0, t0)
    
            self.lista_brzina.append(v0)
            self.lista_puteva.append(s0)
            self.lista_akceleracija.append(a)
            self.lista_vremena.append(t0)
            t0 = t0+self.dt  

        return 


    def graf(self): 

        fig, axs = plt.subplots(3)
        axs[0].plot(self.lista_vremena, self.lista_puteva)
        axs[0].set_title("x-t")

        axs[1].plot(self.lista_vremena, self.lista_brzina)
        axs[1].set_title("v-t")

        axs[2].plot(self.lista_vremena, self.lista_akceleracija)
        axs[2].set_title("a-t")

        plt.show() 

        return    
