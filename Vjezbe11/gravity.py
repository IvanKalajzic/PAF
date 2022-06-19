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
        self.dt = 100
        self.G = 6.67408*(10**(-11))
        self.Ms =  1.989*((10)**30)
        self.Mz = 5.9742*((10)**24)
        self.tt = 365.24*24*3600

    def set_initial_conditions(self, Vs, Vz, Rz, Rs):
        self.lista_Zx.append(1.486*10**(11))
        self.lista_Zy.append(0)
        self.lista_Sx.append(0)
        self.lista_Sy.append(0)
        self.lista_t.append(0)
        self.As = np.array([0, 0])
        self.Az = np.array([0, 0])
        self.Vs = Vs
        self.Vz = Vz
        self.Rs = Rs
        self.Rz = Rz
        
    def __move(self):
        dx = (self.Rz - self.Rs)**2
        self.Az = (-self.G*(self.Ms*(self.Rz-self.Rs)))/((math.sqrt(dx[0]+dx[1])))**3
        self.Vz = self.Vz+self.Az*self.dt
        self.Rz = self.Rz + self.Vz*self.dt
        self.lista_Zx.append(self.Rz[0])
        self.lista_Zy.append(self.Rz[1])

        dy = (self.Rs - self.Rz)**2
        self.As = (-self.G*(self.Mz*(self.Rs-self.Rz)))/((math.sqrt(dy[0]+dy[1])))**3
        self.Vs = self.Vs+self.As*self.dt
        self.Rs = self.Rs + self.Vs*self.dt
        self.lista_Sx.append(self.Rs[0])
        self.lista_Sy.append(self.Rs[1])
    
        self.lista_t.append(self.lista_t[-1]+self.dt)

    def Euler_method(self):
        while self.lista_t[-1] <= self.tt:
            self.__move()  
        return self.lista_Zx, self.lista_Zy, self.lista_Sx, self.lista_Sy        
    





    
        

