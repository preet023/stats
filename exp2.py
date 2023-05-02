import numpy as np
import matplotlib.pyplot as plt

def graph(xs_1,ys_1,xs_2,ys_2,T,title):
    fig,axs=plt.subplots(2,1,figsize=(10,25))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1,ys_1,'*', color='green')
    ax11.set_ylabel("f(x)"),ax11.set_xlabel("x")
    ax12.plot(xs_2[0],ys_2,'*',color='black',label="T ={}K".format(T[0]));ax12.plot(xs_2[1],ys_2,'*', color='green',label="T ={}K".format(T[1]))
    ax12.plot(xs_2[2],ys_2,'*', color='red',label="T ={}K".format(T[2]));ax12.plot(xs_2[3],ys_2,'*', color='brown',label="T ={}K".format(T[3]))
    ax12.set_ylabel("f(epsilon)"),ax12.set_xlabel("epsilon")         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()

T=[10,100,1000,5000]
def Max_Boltzman(T):
    A=1;scale=[]
    for i in T:
        scale.append(x*k*i)
    output=A*np.exp(-x)
    # x=-epsilon/(k*T)
    return x,scale,output 
k = 8.617*(10**-5);eV=1.6*(10**-19)
x = np.linspace(0,2,100)
x,scale,output=Max_Boltzman(T)
graph(x,output,scale,output,T,"Maxwell Distribution")

def bose_einstien():
    scale=[];alpha=0
    for i in T:
        scale.append(x*k*i)
    output=(1/(np.exp(x+alpha)-1))
    return x, scale, output
x = np.linspace(0,2,100)
x,scale,output=bose_einstien()
graph(x,output,scale,output,T,"Bose Einstien")

def dirac(T):
    scale=[]
    for i in T:
        scale.append(x*k*i)
    output=1/(np.exp(x)+1)
    return x,scale,output
x = np.linspace(0,2,100)
x,scale,output=dirac(T)
graph(x,output,scale,output,T,"Fermi Dirac")
