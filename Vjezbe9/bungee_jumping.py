import matplotlib.pyplot as plt
import numpy as np
import math

class bungee:
    def __init__(self):
        self.lista_y = []
        self.lista_aY = []
        self.lista_V0y = []
        self.lista_t = []
        self.lista_potencijalna = []
        self.lista_kineticka = []
        self.lista_elasticna = []
        self.lista_ukupna = []
        self.g = 9.81
        

    def set_initial_conditions(self, k, v0, y0, l0, C, p, A, m, dt): 
        self.dt = dt
        self.C = C
        self.p = p
        self.m = m
        self.dt = dt
        self.y0 = y0
        self.A = A
        self.k = k
        self.l0 = l0
        self.lista_V0y.append(v0)
        self.lista_t.append(0)
        self.lista_aY.append(-self.g)
        self.lista_y.append(y0)
        self.lista_potencijalna.append(m*self.g*self.lista_y[-1])
        self.lista_kineticka.append(0)
        self.lista_elasticna.append(0)
        self.lista_ukupna.append(m*self.g*self.lista_y[-1])

    def a_y(self, y, v, t):
        return -self.g    

    def __move(self):    
        self.lista_t.append(self.lista_t[-1]+self.dt)   
        self.lista_aY.append(self.a_y(self.lista_y[-1], self.lista_V0y[-1], self.lista_t[-1]))
        self.lista_V0y.append(self.lista_V0y[-1] + self.lista_aY[-1]*self.dt)
        self.lista_y.append(self.lista_y[-1] + self.lista_V0y[-1]*self.dt)
        self.lista_potencijalna.append(self.m*(self.g)*(self.lista_y[-1]))
        self.lista_kineticka.append(0.5*self.m*(self.lista_V0y[-1])**2)
        if self.lista_y[-1] > self.y0 - self.l0:
            self.lista_elasticna.append(0)
        else:
            self.lista_elasticna.append(0.5*self.k*(self.y0-self.lista_y[-1]-self.l0)**2)    

        self.lista_ukupna.append(self.lista_potencijalna[-1]+self.lista_kineticka[-1]+self.lista_elasticna[-1])
        

    def a_y1(self, y, v, t):
        return -self.g+(self.k/self.m)*(self.y0-self.lista_y[-1]-self.l0)

    def __move1(self):    
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_aY.append(self.a_y1(self.lista_y[-1], self.lista_V0y[-1], self.lista_t[-1]))
        self.lista_V0y.append(self.lista_V0y[-1]+self.lista_aY[-1]*self.dt)
        self.lista_y.append(self.lista_y[-1]+self.lista_V0y[-1]*self.dt)
        self.lista_potencijalna.append(self.m*(self.g)*(self.lista_y[-1]))
        self.lista_kineticka.append(0.5*self.m*(self.lista_V0y[-1])**2)  
        if self.lista_y[-1] > self.y0 - self.l0:
            self.lista_elasticna.append(0)
        else:
            self.lista_elasticna.append(0.5*self.k*(self.y0-self.lista_y[-1]-self.l0)**2)    

        self.lista_ukupna.append(self.lista_potencijalna[-1]+self.lista_kineticka[-1]+self.lista_elasticna[-1])
        

    def bez_otpora(self, t):
        while self.lista_t[-1] <= t:
            if self.lista_y[-1] > self.y0 - self.l0:
                self.__move()
            else:
                self.__move1()
        return self.lista_y, self.lista_elasticna, self.lista_kineticka, self.lista_potencijalna, self.lista_ukupna, self.lista_t

    def a_Y(self, y, v, t):
        return -self.g-((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0y[-1])*abs(self.lista_V0y[-1])

    def __move11(self):    
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_aY.append(self.a_Y(self.lista_y[-1], self.lista_V0y[-1], self.lista_t[-1]))
        self.lista_V0y.append(self.lista_V0y[-1] + self.lista_aY[-1]*self.dt)
        self.lista_y.append(self.lista_y[-1] + self.lista_V0y[-1]*self.dt)
        self.lista_potencijalna.append(self.m*(self.g)*(self.lista_y[-1]))
        self.lista_kineticka.append(0.5*self.m*(self.lista_V0y[-1])**2)  
        if self.lista_y[-1] > self.y0 - self.l0:
            self.lista_elasticna.append(0)
        else:
            self.lista_elasticna.append(0.5*self.k*(self.y0-self.lista_y[-1]-self.l0)**2)

        self.lista_ukupna.append(self.lista_potencijalna[-1] + self.lista_kineticka[-1] + self.lista_elasticna[-1])
        
     
    def a_Y1(self, y, v, t):
        return -self.g-((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0y[-1])*abs(self.lista_V0y[-1]) + (self.k/self.m)*(self.y0 - self.lista_y[-1] - self.l0) 


    def __move12(self):    
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_aY.append(self.a_Y1(self.lista_y[-1], self.lista_V0y[-1], self.lista_t[-1]))
        self.lista_V0y.append(self.lista_V0y[-1] + self.lista_aY[-1]*self.dt)
        self.lista_y.append(self.lista_y[-1] + self.lista_V0y[-1]*self.dt)
        self.lista_potencijalna.append(self.m*(self.g)*(self.lista_y[-1]))
        self.lista_kineticka.append(0.5*self.m*(self.lista_V0y[-1])**2)  
        if self.lista_y[-1] > self.y0 - self.l0:
            self.lista_elasticna.append(0)
        else:
            self.lista_elasticna.append(0.5*self.k*(self.y0-self.lista_y[-1]-self.l0)**2)

        self.lista_ukupna.append(self.lista_potencijalna[-1] + self.lista_kineticka[-1] + self.lista_elasticna[-1])
         

    def s_otporom(self, t):
        while self.lista_t[-1] <= t:
            if self.lista_y[-1] > self.y0 - self.l0:
                self.__move11()
            else:
                self.__move12()
        return self.lista_y, self.lista_elasticna, self.lista_kineticka, self.lista_potencijalna, self.lista_ukupna, self.lista_t                     


  
    

    
    