# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
i=0
j=0
delta= fx[i+1]-fx[i]
primeraDerivada = []
segundaDerivada = []

def primeraD():
    D = (fx[i+1]-fx[i])/((x+delta)-x)
    primeraDerivada.append(D)
    i=i+1   


def segundaD():
    S= (fx[j+1]-fx[j])/((PrimeraDerivada+delta)-primeraDerivada)
    segundaDerivada.append(S)
    j=j+1

plt.plot(x,segundaDerivada)
plt.savefig('segunda.png')
plt.plot()
    

    
    