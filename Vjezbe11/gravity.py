import matplotlib.pyplot as plt
import numpy as np
import math

class SunEarth:
    def __init__(self):
        self.lista_Zx = []
        self.lista_Zy = []
        self.lista_Sx = []
        self.lista_Sy = []
        self.lista_t = []
        self.dt = 1.1
        self.G = 6.67408*(10**(-11))
        self.Ms =  1.989*((10)**30)
        self.Mz = 5.9742*((10)**24)

    def set_initial_conditions(self, Vs, Vz, Rs, Rz):
        self.lista_Zx.append(0)
        self.lista_Zy.append(0)
        self.lista_Sx.append(0)
        self.lista_Sy.append(0)
        self.lista_t.append(0)
        self.As = np.array([0, 0, 0])
        self.Az = np.array([0, 0, 0])
        self.Vs = Vs
        self.Vz = Vz
        self.Rs = Rs
        self.Rz = Rz
        
    def __move(self):
        self.Az = (-self.G*(self.Ms*(self.Rz-self.Rs)))/(abs(self.Rz-self.Rs))**3
        self.Vz = self.Vz+self.Az*self.dt
        self.lista_Zx.append(self.lista_Zx[-1]+self.Vz[0]*self.dt)
        self.lista_Zy.append(self.lista_Zy[-1]+self.Vz[1]*self.dt)

        self.As = (-self.G*(self.Mz*(self.Rs-self.Rz)))/(abs(self.Rs-self.Rz))**3
        self.Vs = self.Vs+self.As*self.dt
        self.lista_Sx.append(self.lista_Sx[-1]+self.Vs[0]*self.dt)
        self.lista_Sy.append(self.lista_Sy[-1]+self.Vs[1]*self.dt)

        self.Rz = ([self.lista_Zx[-1], self.lista_Zy[-1]])
        self.Rs = ([self.lista_Sx[-1], self.lista_Sy[-1]])

    def Euler_method(self, t):
        n = int(t/self.dt) 
        for i in range(n):
            self.__move()  
        return self.lista_Zx, self.lista_Zy, self.lista_Sx, self.lista_Sy        
    





    
        

