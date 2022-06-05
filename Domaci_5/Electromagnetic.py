import matplotlib.pyplot as plt
import numpy as np
import math

class particles:
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_z = []
        self.lista_t = []
        self.dt = 0.01

    def set_initial_conditions(self, v, m, E, B, q):
        self.lista_x.append(0)
        self.lista_y.append(0)
        self.lista_t.append(0)
        self.lista_z.append(0)
        self.a = np.array([0, 0, 0])
        self.m = m
        self.v = v
        self.E = E
        self.B = B
        self.q = q



    def __move(self):
        self.a = (self.q*(self.E+(np.cross(self.v, self.B))))/self.m
        self.v = self.v+self.a*self.dt
        self.lista_x.append(self.lista_x[-1]+self.v[0]*self.dt)
        self.lista_y.append(self.lista_y[-1]+self.v[1]*self.dt)
        self.lista_z.append(self.lista_z[-1]+self.v[2]*self.dt)

    def Euler_method(self, t):
        n = int(t/self.dt) 
        for i in range(n):
            self.__move()
        return  self.lista_x, self.lista_y, self.lista_z

    def b(self, t):
        return  t/10


    def __move1(self):
    
        k1vx = ((self.q*(self.E+(np.cross(self.v, self.B))))/self.m)*self.dt
        k1x = self.v*self.dt
        k2vx = (self.q*(self.E+(np.cross(self.v+k1vx/2, self.B))))/self.m*self.dt
        k2x = (self.v+(k1vx/2))*self.dt
        k3vx = (self.q*(self.E+(np.cross(self.v+k2vx/2, self.B))))/self.m*self.dt
        k3x = (self.v+(k2vx/2))*self.dt
        k4vx = (self.q*(self.E+(np.cross(self.v+k3vx, self.B))))/self.m*self.dt
        k4x = (self.v+k3vx)*self.dt
        self.v = self.v+1/6*(k1vx+2*k2vx+2*k3vx+k4vx)
        self.lista_x.append(self.lista_x[-1]+1/6*(k1x[0]+2*k2x[0]+2*k3x[0]+k4x[0]))
        self.lista_y.append(self.lista_y[-1]+1/6*(k1x[1]+2*k2x[1]+2*k3x[1]+k4x[1]))
        self.lista_z.append(self.lista_z[-1]+1/6*(k1x[2]+2*k2x[2]+2*k3x[2]+k4x[2]))
        self.B = np.array([0, 0, self.b(self.lista_t[-1])])
        self.lista_t.append(self.lista_t[-1]+self.dt)


    def __move12(self):
        
        k1vx = ((self.q*(self.E+(np.cross(self.v, self.B))))/self.m)*self.dt
        k1x = self.v*self.dt
        k2vx = (self.q*(self.E+(np.cross(self.v+k1vx/2, self.B))))/self.m*self.dt
        k2x = (self.v+(k1vx/2))*self.dt
        k3vx = (self.q*(self.E+(np.cross(self.v+k2vx/2, self.B))))/self.m*self.dt
        k3x = (self.v+(k2vx/2))*self.dt
        k4vx = (self.q*(self.E+(np.cross(self.v+k3vx, self.B))))/self.m*self.dt
        k4x = (self.v+k3vx)*self.dt
        self.v = self.v+1/6*(k1vx+2*k2vx+2*k3vx+k4vx)
        self.lista_x.append(self.lista_x[-1]+1/6*(k1x[0]+2*k2x[0]+2*k3x[0]+k4x[0]))
        self.lista_y.append(self.lista_y[-1]+1/6*(k1x[1]+2*k2x[1]+2*k3x[1]+k4x[1]))
        self.lista_z.append(self.lista_z[-1]+1/6*(k1x[2]+2*k2x[2]+2*k3x[2]+k4x[2]))
            

       
    def konstantno_polje(self, t):
        n = int(t/self.dt) 
        for i in range(n):
            self.__move12()
        return  self.lista_x, self.lista_y, self.lista_z

    def promjenjivo_polje(self):
        while self.B[2] <= 10:
            self.__move1()
        return  self.lista_x, self.lista_y, self.lista_z    

    


               