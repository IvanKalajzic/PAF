import matplotlib.pyplot as plt
import numpy as np
import math

class projectile:
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_aX = []
        self.lista_aY = []
        self.lista_V0x = []
        self.lista_V0y = []
        self.lista_t = []
        self.g = 9.81

    def set_initial_conditions(self, x0, y0, v0, theta, C, p, A, m, dt):
        self.lista_x.append(x0)
        self.lista_y.append(y0)
        self.lista_aX.append(0)
        self.lista_aY.append(9.81)
        self.lista_t.append(0)
        self.dt = dt
        self.C = C
        self.p = p
        self.A = A
        self.m = m
        self.theta = theta
        self.V0x = np.cos(theta*np.pi/180)*v0
        self.V0y = np.sin(theta*np.pi/180)*v0 
        self.lista_V0x.append(self.V0x)
        self.lista_V0y.append(self.V0y)

    def __move(self):
        self.lista_aX.append(-((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0x[-1])**2)
        self.lista_V0x.append(self.lista_V0x[-1] + self.lista_aX[-1]*self.dt)
        self.lista_x.append(self.lista_x[-1]+self.lista_V0x[-1]*self.dt)
        self.lista_aY.append(-self.g-((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0y[-1])**2)
        self.lista_V0y.append(self.lista_V0y[-1] + self.lista_aY[-1]*self.dt)
        self.lista_y.append(self.lista_y[-1]+self.lista_V0y[-1]*self.dt)

    def Euler_method(self): 
        while self.lista_y[-1] >= 0:
            self.__move()
        return  self.lista_x, self.lista_y

    def a_x(self, x, v, t):
        return -((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0x[-1])**2

    def a_y(self, x, v, t):
        return -self.g-((self.p*self.C*self.A)/(2*self.m))*(self.lista_V0y[-1])**2      

    def __move1(self):
        k1vx = self.a_x(self.lista_x[-1], self.lista_V0x[-1], self.lista_t[-1])*self.dt
        k1x = self.lista_V0x[-1]*self.dt
        k2vx = self.a_x(self.lista_x[-1]+(k1x/2), self.lista_V0x[-1]+(k1vx/2), self.lista_t[-1]+(self.dt/2))*self.dt
        k2x = (self.lista_V0x[-1]+(k1vx/2))*self.dt
        k3vx = self.a_x(self.lista_x[-1]+(k2x/2), self.lista_V0x[-1]+(k2vx/2), self.lista_t[-1]+(self.dt/2))*self.dt
        k3x = (self.lista_V0x[-1]+(k2vx/2))*self.dt
        k4vx = self.a_x(self.lista_x[-1]+(k3x/2), self.lista_V0x[-1]+(k3vx/2), self.lista_t[-1]+(self.dt))*self.dt
        k4x = (self.lista_V0x[-1]+k3vx)*self.dt
        self.lista_V0x.append(self.lista_V0x[-1]+1/6*(k1vx+2*k2vx+2*k3vx+k4vx))
        self.lista_x.append(self.lista_x[-1]+1/6*(k1x+2*k2x+2*k3x+k4x))

        k1vy = self.a_y(self.lista_y[-1], self.lista_V0y[-1], self.lista_t[-1])*self.dt
        k1y = self.lista_V0y[-1]*self.dt
        k2vy = self.a_y(self.lista_y[-1]+(k1x/2), self.lista_V0y[-1]+(k1vy/2), self.lista_t[-1]+(self.dt/2))*self.dt
        k2y = (self.lista_V0y[-1]+(k1vy/2))*self.dt
        k3vy = self.a_y(self.lista_y[-1]+(k2x/2), self.lista_V0y[-1]+(k2vy/2), self.lista_t[-1]+(self.dt/2))*self.dt
        k3y = (self.lista_V0y[-1]+(k2vy/2))*self.dt
        k4vy = self.a_y(self.lista_y[-1]+(k3x/2), self.lista_V0y[-1]+(k3vy/2), self.lista_t[-1]+(self.dt))*self.dt
        k4y = (self.lista_V0y[-1]+k3vy)*self.dt
        self.lista_V0y.append(self.lista_V0y[-1]+1/6*(k1vy+2*k2vy+2*k3vy+k4vy))
        self.lista_y.append(self.lista_y[-1]+1/6*(k1y+2*k2y+2*k3y+k4y))

    def Runge_Kutta_method(self):
        while self.lista_y[-1] >= 0:
            self.__move1()
        return  self.lista_x, self.lista_y

    def Domet(self):
        while self.lista_y[-1] >= 0:
            self.__move1()
        return  self.lista_x[-1]    


               