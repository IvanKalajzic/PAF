
import matplotlib.pyplot as plt
import numpy as np
import math

class HarmonicOscilator:
    def __init__(self):
        self.lista_x = []
        self.lista_v = []
        self.lista_a = []
        self.lista_t = []
        

    def set_initial_conditions(self, k, x0, v0, m, t0, a0, dt): 
        self.k = k
        self.m = m
        self.t0 = t0
        self.dt = dt
        self.x0 = x0
        self.lista_x.append(x0)
        self.lista_v.append(v0)
        self.lista_t.append(t0)
        self.lista_a.append(a0)

    def __move(self):
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_a.append((self.k/self.m)*self.lista_x[-1])
        self.lista_v.append(self.lista_v[-1]+self.lista_a[-1]*self.dt)
        self.lista_x.append(self.lista_x[-1]-self.lista_v[-1]*self.dt)

    def oscilate(self, t):
        n = int(t/self.dt)
        for i in range(n):
            self.__move() 
        return self.lista_a, self.lista_t, self.lista_v, self.lista_x 

    def oscilate2(self, t):
        n = int(t/self.dt)
        for i in range(n):
            self.__move() 
        return self.lista_x, self.lista_t 

    def period(self, t):
        x, tt = self.oscilate2(t)
        A = max(x)
        i = x.index(A)
        j = tt[i]
        T = j*(1/2)
    
        print("Numericki (dt = {}): {}.".format(self.dt, T))
        

    def periodA(self):   
        T = 2*math.pi*math.sqrt(self.m/self.k) 
        print("Analiticki: {}.".format(T))







                





        
