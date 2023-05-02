import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
def dulong_petit(T):
    y=[]
    for i in T:
        y.append(1)
    return y, T

T=np.linspace(0,2,100)
y_,T_ = dulong_petit(T)

def einst(eins_freq):
    x=np.arange(0,2.01,0.1)
    y=[]
    for i in x:
        if i==eins_freq:
            y.append(1)
        else:
            y.append(0)
    return x,y
eins_freq=1
x,y = einst(eins_freq)
plt.plot(x,y,marker="*")
plt.xlabel(r"$\nu/ \nu_{e}$")
plt.ylabel(r"$G(\nu)/(N \times f)$")
plt.title("Density of States for Einstien Model")
plt.grid()
plt.show()


def einstien(x):
    return x, (((1/x)**2)*(np.exp(1/x)))/((np.exp(1/x)-1)**2)
x=np.linspace(0,2,100)
x_1,output_1 = einstien(x)


def debye(x):
    output=[]
    y = lambda x: ((x**3))/(np.exp((x))-1)
    for i in range(len(x)):
        y_=(-3*(x[i])/(np.exp(x[i])-1))+(12/((x[i])**3))*(integrate.quad(y, 0, x[i])[0])
        output.append(y_)
    return output
xmin=0;xmax=2
x_2= np.linspace(xmin,xmax,100)
output_2 = debye(1/x)
plt.scatter(T_,y_,label="Dulong Petit Distribution Model")
plt.scatter(x_2,output_2,label="Debye Model")
plt.scatter(x_1,output_1,label="Einstien Method")
plt.xlabel(r"$T/ \theta$")
plt.ylabel(r"$C_{v}/3R$")
plt.grid()
plt.legend()
plt.show()
