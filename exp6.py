import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
def z_(states,energy,T):
    z=[]
    for i in range(len(states)):
        print(states[i],energy[i])
        z_ =states[i]*(np.exp((-energy[i])/(k*T)))
        z.append(z_)
    z_final = sum(z)
    return z_final,z

def graph(xs_1,ys_1,xs_2,ys_2,xlabel,ylabel,label1,label2,title):
    fig,axs=plt.subplots(2,1,figsize=(10,25))
    fig.suptitle(title, fontsize=10)
    ax11,ax12=axs[0],axs[1]
    ax11.plot(xs_1,ys_1,'*', color='green',label=label1)
    ax11.set_ylabel(ylabel),ax11.set_xlabel(xlabel)
    ax12.plot(xs_2,ys_2,'o',color='black',label=label2)
    ax12.set_ylabel(ylabel),ax12.set_xlabel(xlabel)         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
    plt.show()

k = 8.617e-5
states=[1,2]
low_Trange= np.linspace(0.1,5000,100)
high_Trange = np.linspace(5000,10**5,100)
energy=[0,1]
n=10**5
z_final,z=z_(states,energy,low_Trange)
z_final1,z1=z_(states,energy,high_Trange)

graph(low_Trange,z_final,high_Trange,z_final1,"T","z","Low Temperature","High Temperature","z vs T")

fig,axs=plt.subplots(2,1,figsize=(10,25))
fig.suptitle("U/N v/s T", fontsize=10)
ax11,ax12=axs[0],axs[1]
for i in range(len(energy)):
    ax11.plot(high_Trange,z1[i]/z_final1,'*', color='green',label="state = {}".format(i+1))
    ax11.set_ylabel(r"$N_{j}/N$"),ax11.set_title("High Temperature")
    ax12.plot(low_Trange,z[i]/z_final,'*', color='green',label="state = {}".format(i+1))
    ax12.set_ylabel(r"$N_{j}/N$"),ax12.set_xlabel("T"),ax12.set_title("Low Temperature")         
    ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
plt.show()

U_=[];U1=[]
fig,axs=plt.subplots(2,1,figsize=(10,25))
fig.suptitle("U/N v/s T", fontsize=10)
ax11,ax12=axs[0],axs[1]
for i in range(len(energy)):
    U_.append(energy[i]*(z[i]/z_final))
    U1.append(energy[i]*(z1[i]/z_final1))
U11=sum(U1)
U=sum(U_)
print("test",U_[0][:3],U_[1][:3],U[:3])
ax11.plot(low_Trange,U,'*', color='green',label="Low Temperature")
ax11.set_ylabel("U/N"),ax11.set_xlabel("T")
ax12.plot(high_Trange,U11,'*', color='green',label="High Temperature")
ax12.set_ylabel("U/N"),ax12.set_xlabel("T")         
ax11.legend(),ax11.grid(True),ax12.legend(),ax12.grid(True)
plt.show()

s= n*k*np.log(z_final/n) + (U/low_Trange) + n*k
s1= n*k*np.log(z_final1/n) + (U11/high_Trange) + n*k
# graph(low_Trange,s,high_Trange,s1,"T","s","Low Temperature","High Temperature","Entropy(s) vs T")

F = -n*k*low_Trange*(np.log(z_final))
F1 = -n*k*high_Trange*(np.log(z_final1))
graph(low_Trange,F,high_Trange,F1,"T","F","Low Temperature","High Temperature","Gibbs Free Energy(F) vs T")

slope=linregress(U,s)[0]
slope1=linregress(U11,s1)[0]
graph(U,s,U11,s1,"U","s","Low Temperature","High Temperature","s vs U")

