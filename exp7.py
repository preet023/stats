import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import linregress
import math
h = 6.63*10**(-34)
k = 1.38*10**(-23)
N = 6.023*10**(23)
m = 1.67*10**(-27)

def Z_VT(n,V,T):
    C = h**2/(8*m*(V**(2/3))*k*T)
    return (np.pi/2)*(n**2)*np.exp(-(n**2)*C)

def inte(n_i,n_f,V,T):
    I = quad(lambda n: Z_VT(n,V,T),n_i,n_f)
    return I

V = np.linspace(20*10**(-3),50*10**(-3),10)
T = np.linspace(150,450,10)

main = np.zeros((len(V),len(T)))
for i in range(len(V)):
    for j in range(len(T)):
        main[i,j] = inte(1,10**(11),V[i],T[j])[0]

main_log = np.zeros((len(V),len(T)))
for i in range(len(V)):
    for j in range(len(T)):
        main_log[i,j] = np.log(inte(1,10**(11),V[i],T[j]))[0]
for i in range(len(T)):
    plt.plot(np.log(V),np.log(main[:,i]),label="T ={}K".format(float(f'{T[i]:.3f}')))
    plt.xlabel("logV")
    plt.ylabel("logZ")
    plt.grid()
    plt.legend()
plt.show()

for i in range(len(V)):
    plt.plot(np.log(T),np.log(main[i,:]),label="V ={}".format(float(f'{V[i]:.3f}')))
    plt.xlabel("logT")
    plt.ylabel("logZ")
    plt.grid()
    plt.legend()
plt.show()

def pressure(T,V,lnZ):
    P = []
    for i in range(len(lnZ)-1):
        p = (N*k*T*(lnZ[i+1]-lnZ[i]))/(V[i+1]-V[i])
        P.append(p)
    return P

P = []
for i in range(len(V)):
    P.append(pressure(T[i],V,main_log[:,i])) 
#Energy
def energy(T,lnZ):
    U = []
    for i in range(len(lnZ)-1):
        u = (k*(T[i]**2)*(lnZ[i+1]-lnZ[i]))/(T[i+1]-T[i])
        U.append(u)
    return U

U = []
for i in range(len(V)):
    U.append(energy(T,main_log[i,:]))
#entropy
S_main =[]
for i in range(len(U)):
    S = []
    for j in range(len(U)-1):
        S.append((U[i][j]/T[i])+N*k*(main_log[i,:][j]-np.log(N)+1))
    S_main.append(S)

def C_v(T,U):
    C_v = []
    for i in range(len(U)-1):
        Cv = (1/N)*((U[i+1]-U[i])/(T[i+1]-T[i]))
        C_v.append(Cv)
    return C_v

C__v = []
for i in range(len(U)):
    C__v.append(C_v(T,U[i]))          
for i in range(len(V)):
    slope = linregress(U[i], T[:-1])[0]    
    plt.plot(T[:-1],U[i],label="V ={}".format(float(f'{V[i]:.3f}')))
    plt.xlabel("T")
    plt.ylabel("U")
    plt.grid()
    plt.legend()
plt.show()
print(slope)

for i in range(len(V)):
    plt.plot(T[:-1],S,label="V ={}".format(float(f'{V[i]:.3f}')))
    plt.xlabel("T")
    plt.ylabel("S")
    plt.grid()
    plt.legend()
plt.show()


for i in range(len(V)):
    plt.plot(V[:-1],P[i],label="T ={}K".format(float(f'{T[i]:.3f}')))
    plt.xlabel("V")
    plt.ylabel("P")
    plt.grid()
    plt.legend()
plt.show()

# for i in range(len(V)):
#     plt.plot(T[:-1],P[i],label="T ={}K".format(float(f'{T[i]:.3f}')))
#     plt.xlabel("T")
#     plt.ylabel("P")
#     plt.grid()
#     plt.legend()
# plt.show()

slope = linregress(U[0], T[:-1])[0]
plt.plot(T,np.multiply(slope,k*(T**2)))
plt.xlabel("T")
plt.ylabel("$\sigma_{E}$")
plt.grid()
plt.legend()
plt.show()
