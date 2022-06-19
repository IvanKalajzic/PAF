
import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def __init__(self):
        self.lista_x = []
        self.lista_y = []
        self.lista_t = []
        self.lista_a = []
        self.lista_gresaka = []
        self.lista_v = []
        self.lista_udaljenosti = []
        self.dt = 0.01
        self.g = 9.81

    def set_initial_conditions(self, x0, y0, v0, theta):
        self.lista_a.append(self.g)
        self.lista_x.append(x0)
        self.lista_y.append(y0)
        self.lista_t.append(0)
        self.lista_gresaka.append(0)
        self.lista_v.append(0)
        self.theta = theta
        self.v0 = v0
        self.V0x = math.cos(theta*math.pi/180)*v0
        self.V0y = math.sin(theta*math.pi/180)*v0

        return 

    def reset(self):
        self.__init__()  

    def __move(self):
        self.lista_t.append(self.lista_t[-1]+self.dt)
        self.lista_x.append(self.lista_x[-1]+self.V0x*self.dt)
        self.V0y = self.V0y-self.g*self.dt
        self.maks = math.sqrt(((self.V0x)**2)+((self.V0y)**2))
        self.lista_v.append(self.maks)
        self.lista_y.append(self.lista_y[-1]+self.V0y*self.dt)

    def range(self): 
        while self.lista_y[-1] >= 0:
            self.__move()
        return  self.lista_x, self.lista_y     


    def range_d(self):
        while self.lista_y[-1] >= 0:
            self.__move()
        return abs(self.lista_x[-1])

    def range_t(self):
        while self.lista_y[-1] >= 0:
            self.__move()
        return self.lista_t[-1]    



    def plot_trajectory(self):
        fig, axs = plt.subplots()

        axs.plot(self.lista_x, self.lista_y)
        axs.set_title("x-y")
        plt.show()

    def odstupanje_dometa(self, v0, theta):
        self.ana_domet = (v0**2/self.g*2)*np.sin(2*theta*np.pi/180) 
        print('Odstupanje iznosi: {}%.'.format(((abs(self.ana_domet-self.lista_x[-1]))/self.ana_domet)*100.0))


        
    def __relativna_pogreska(self, dt):
        self.lista_t.append(self.lista_t[-1]+dt)
        self.lista_x.append(self.lista_x[-1]+self.V0x*dt)
        self.V0y = self.V0y-self.g*dt
        self.lista_y.append(self.lista_y[-1]+self.V0y*dt)

       
       

    def range_pogreske(self, dt):
         while self.lista_y[-1] >= 0:
            self.__relativna_pogreska(dt)
         return self.lista_x[-1]         

    def analit_dom(self):
        return ((self.v0**2)*math.sin(2*(self.theta*math.pi/180)))/self.g        
            


    def total_time(self):
        while self.lista_y[-1] >= 0:
            self.__move()

        return self.lista_t[-1]   

    def max_speed(self):
        while self.lista_y[-1] >= 0:
            self.__move()

        return max(self.lista_v)  

   

    

          
               

                




    
             









    








        



        