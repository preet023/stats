import numpy as np
import matplotlib.pyplot as plt
def graph1(xs_1,ys_1,xs_2,ys_2,T,title):
    fig,axs=plt.subplots(2,1,figsize=(10,30))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1,ys_1,'*', color='green')
    ax11.set_ylabel(r"$G(\nu)$"),ax11.set_xlabel(r"$\nu$"),ax11.set_xscale("log");ax11.set_yscale("log")
    ax12.plot(xs_2[0],ys_2[0],'*',color='black',label="T ={}K".format(T[0]));ax12.plot(xs_2[1],ys_2[1],'*', color='green',label="T ={}K".format(T[1]))
    ax12.plot(xs_2[2],ys_2[2],'*', color='red',label="T ={}K".format(T[2]));ax12.plot(xs_2[3],ys_2[3],'*', color='brown',label="T ={}K".format(T[3]))
    ax12.set_ylabel(r"$u(\nu) d\nu$"),ax12.set_xlabel(r"$\nu$")         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()
def graph2(xs_1,ys_1,xs_2,ys_2,T,title):
    fig,axs=plt.subplots(2,1,figsize=(10,30))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1,ys_1,'*', color='green')
    ax11.set_ylabel(r"$G(\nu)$"),ax11.set_xlabel(r"$\nu$")
    ax12.plot(xs_2[0],ys_2[0],'*',color='black',label="T ={}K".format(T[0]));ax12.plot(xs_2[1],ys_2[1],'*', color='green',label="T ={}K".format(T[1]))
    ax12.plot(xs_2[2],ys_2[2],'*', color='red',label="T ={}K".format(T[2]));ax12.plot(xs_2[3],ys_2[3],'*', color='brown',label="T ={}K".format(T[3]))
    ax12.axvspan(4*(10**14)/1.5*10**(-18),8*(10**14)/1.5*10**(-18),color="grey",alpha=0.1)
    ax12.set_ylabel(r"$u(\nu) d\nu$"),ax12.set_xlabel(r"$\nu$")         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()



def f_rj(x):
    return np.pi*(x**2)

x=np.linspace(0,12,100)
k = 1.38e-23;h=6.626e-34;c=3e8;T=[4000,5000,6000,7000];constant=[]
output = f_rj(x)
output_1=[];x1=[];output_2=[]
for i in T:
    v0=(k*i)/(h)
    l=(c*h)/(v0*h)
    x1.append(x*(v0))
    constant = ((8*(np.pi)*k*i)/l**3)
    output_1.append(output*constant)
    output_2.append(output*constant/v0)
graph1(x,output,x1,output_2,T,"Rayleigh Jeans Law")


def f_p(x):
    return (x**3)/((np.exp(x)-1))
output = f_p(x)
output_1=[];x1=[];output_2=[]
for i in T:
    v0=(k*i)/(h)
    l=(c*h)/(v0*h)
    x1.append(x*(v0))
    constant = ((8*(np.pi)*k*i)/l**3)
    output_1.append(output*constant)
    output_2.append(output*constant/v0)
graph2(x,output,x1,output_2,T,"Plank Law")
