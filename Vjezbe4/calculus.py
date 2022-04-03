import numpy as np
import matplotlib.pyplot as plt 
def deriv(f, x, dx):
    return (f(x+dx)-f(x))/(dx)

def deriv2(f, a, b, dx, nacin):
    x = np.linspace(a, b, 50)
    if nacin == 3:
        derivacija = (f(x+dx)-f(x-dx))/(2*dx)
       
    else:
        derivacija = (f(x+dx)-f(x))/(dx)
          

    return x, derivacija    


def num_integracija(f, a, b, n):
    dx = (b-a)/n
    gornja = 0
    donja = 0
    for x in range(int(n)):
        gornja += f(a + (x+1)*dx)*dx 
        donja += f(a + x*dx)*dx
        
    return gornja, donja 

def trapezna_integracija(f, a, b, n):
    dx = (b-a)/n
    zbroj = 0.5*dx*(f(a)+f(b))
    for x in range(1, int(n)+1):
        zbroj += dx*f(x*dx)

    return zbroj  
           




 

     





 
        
