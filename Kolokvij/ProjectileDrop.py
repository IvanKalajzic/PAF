from cgitb import reset
import matplotlib.pyplot as plt
import numpy as np
import math

class ProjectileDrop:
    
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_t = []
        self.lista_v = []
        self.lista_udaljenosti = []
        self.g = 9.81

    def set_initial_conditions(self, y0, v0, dt):
        self.y0 = y0
        self.dt = dt
        self.x0 = 0
        self.theta = 0
        self.v0 = v0
        self.lista_x.append(0)
        self.lista_y.append(y0)
        self.lista_t.append(0)
        self.lista_v.append(0)
        self.V0x = np.cos(self.theta*np.pi/180)*self.v0
        self.V0y = np.sin(self.theta*np.pi/180)*self.v0
        print("Objekt uspjesno stvoren, iznos visine je {} km, a brzine {} m/s.".format(y0/1000, v0))

        return 

    def promjena_visine(self, y0):
        return self.set_initial_conditions(y0, self.v0, self.dt)

    def promjena_brzine(self, v0):
        return self.set_initial_conditions(self.y0, v0, self.dt)    
            
            

    def __move(self):
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_x.append(self.lista_x[-1]+self.V0x*self.dt)
        self.V0y = self.V0y-self.g*self.dt
        self.maks = math.sqrt(((self.V0x)**2)+((self.V0y)**2))
        self.lista_v.append(abs(self.V0y))
        self.lista_y.append(self.lista_y[-1]+self.V0y*self.dt)

    def range(self): 
        while self.lista_y[-1] >= 0:
            self.__move()
        return  self.lista_x, self.lista_t, self.lista_v, self.lista_y 

    def vrijeme_trajanja_pada(self):
        while self.lista_y[-1] >= 0:
            self.__move()
        return self.lista_t[-1]

    def udaljenosti(self):
        while self.lista_y[-1] >= 0:
            self.__move1()
        return self.lista_udaljenosti
    



    def __move1(self):
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_x.append(self.lista_x[-1]+(self.V0x+self.Vv)*self.dt)
        self.V0y = self.V0y-self.g*self.dt
        self.maks = math.sqrt(((self.V0x)**2)+((self.V0y)**2))
        self.lista_v.append(abs(self.V0y))
        self.lista_y.append(self.lista_y[-1]+self.V0y*self.dt)
        d = math.sqrt(((self.s1-self.lista_x[-1])**2)+((self.s2-self.lista_y[-1])**2))
        self.lista_udaljenosti.append(d)

    def indeks1(self):
        for i in range(len(self.udaljenosti())):
            if (self.udaljenosti())[i] <= self.r:
                indeks = i
                break

            else:
                print("Meta nije pogodena")

        return indeks    

     


    def projektil_meta(self, x, sirina, Vv):
        self.Vv = Vv
        self.r = sirina/2
        self.s1 = x
        self.s2 = 0


          
            
        krug = plt.Circle((s1, s2), r, fill = True)

        fig, ax = plt.subplots()
        ax.set_aspect(1)

        ax.add_artist(krug)
        plt.plot(s1, s2, "bo")

        ax.plot(lista_dometa, lista_visina)
        ax.set_title("x-y")

        plt.show()

         
