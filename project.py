import numpy as np
import matplotlib.pyplot as plt
kB = 1.38e-23;h = 6.626e-34;m = 9.1e-31;c = 3e8;s=0.5;e=1.6e-19
E=np.linspace(0,2,10000)
meu = 1;MeV=10**6
V=1
#non relativistic fermions
def plot(E, N, g, dN_de, temperatures,title):
    fig, axes = plt.subplots(3, 1, figsize=(8, 10))
    fig.suptitle(title)    
    for i, T in enumerate(temperatures):
        axes[0].plot(E, N[i], label=f'T={T}K')
    axes[0].set_xlabel('Energy (eV)')
    axes[0].set_ylabel('N')
    axes[0].legend()
    for i, T in enumerate(temperatures):
        axes[1].plot(E, g[i], label=f'T={T}K')
    axes[1].set_xlabel('Energy (eV)')
    axes[1].set_ylabel('Density of states (g)')
    axes[1].legend()

    for i, T in enumerate(temperatures):
        axes[2].plot(E, dN_de[i], label=f'T={T}K')
    axes[2].set_xlabel('Energy (eV)')
    axes[2].set_ylabel('dN/de')
    axes[2].legend()
    
    plt.show()

def non_rel_fermi_dirac():
    Cn = (2*s+1)*(2*np.pi*V*((2*m)**(3/2)))/(h**3)
    dN_de=[];N=[];g=[];U=[]
    for i in range(len(T)):
        beta = 1/(kB*T[i])
        dN_de_=[];N_=[];g_=[];U_=[]
        for j in range(len(E)):
            N_.append(1/(np.exp(np.multiply(beta*e,(E[j]-meu)))+1))
            g_.append(Cn*(E[j])**0.5)
            
            dN_de_.append(Cn*(E[j])**0.5/(np.exp((e/(kB*T[i]))*(E[j]-meu))+1))

        N.append(N_);g.append(g_);dN_de.append(dN_de_)
    return N,g,dN_de
T = [10,100,1000]
N,g,dN_de = non_rel_fermi_dirac()
plot(E, N, g, dN_de, T,"non relativistic fermi dirac")
plt.scatter(E,E * np.array(N) * np.array(g))
plt.show()
def total_internal_energy(E, N, g):
    U = np.trapz(E * np.array(N) * np.array(g), E)
    return U

for i in range(len(T)):
    U = total_internal_energy(E, N[i], g[i])
    print(f'T={T[i]}K: U={U} J')
    # print(f'T_c={T[i]}K: T_c={U/((3/2)*N*kB)} J')
def pressure(E, N, g, T):
    n = np.trapz(np.array(N) * np.array(g), E)
    P = n * kB * T
    return P
for i in range(len(T)):
    P = pressure(E, N[i], g[i], T[i])
    print(f'T={T[i]}K: P={P} Pa')

def rel_fermi_dirac():
    Cr = (2*s*4*np.pi*V)/((h**3)*(c**3))
    dN_de=[];N=[];g=[]
    for i in range(len(T)):
        beta = 1/(kB*T[i])
        dN_de_=[];N_=[];g_=[]
        for j in range(len(E)):
            N_.append(1/(np.exp(np.multiply(MeV*beta*e,(E[j]-meu)))+1))
            g_.append(Cr*(E[j])**2)
            dN_de_.append(Cr*((E[j])**2)/(np.exp((MeV*e/(kB*T[i]))*(E[j]-meu))+1))
        N.append(N_);g.append(g_);dN_de.append(dN_de_)
    return N,g,dN_de
T = [10**6,10**9]
N,g,dN_de = rel_fermi_dirac()
plot(E, N, g, dN_de, T,"relativistic fermi dirac")

for i in range(len(T)):
    U = total_internal_energy(E, N[i], g[i])
    print(f'T={T[i]}K: U={U} J')

for i in range(len(T)):
    P = pressure(E, N[i], g[i], T[i])
    print(f'T={T[i]}K: P={P} Pa')

# s=1
# def non_rel_bose_eins():
#     Cn = (2*s+1)*(2*np.pi*V*((2*m)**(3/2)))/(h**3)
#     dN_de=[];N=[];g=[]
#     for i in range(len(T)):
#         beta = 1/(kB*T[i])
#         dN_de_=[];N_=[];g_=[]
#         for j in range(len(E)):
#             N_.append(1/(np.exp(np.multiply(beta*e,(E[j]-meu)))-1))
#             g_.append(Cn*(E[j])**0.5)
#             dN_de_.append(Cn*(E[j])**0.5/(np.exp((e/(kB*T[i]))*(E[j]-meu))-1))
#         N.append(N_);g.append(g_);dN_de.append(dN_de_)
#     return N,g,dN_de
# T = [10,100,1000]
# N,g,dN_de = non_rel_bose_eins()
# plot(E, N, g, dN_de, T,"non relativistic bose einstien")

# for i in range(len(T)):
#     U = total_internal_energy(E, N[i], g[i])
#     print(f'T={T[i]}K: U={U} J')
# for i in range(len(T)):
#     P = pressure(E, N[i], g[i], T[i])
#     print(f'T={T[i]}K: P={P} Pa')


# def rel_bose_eins():
#     Cr = (2*s*4*np.pi*V)/((h**3)*(c**3))
#     dN_de=[];N=[];g=[]
#     for i in range(len(T)):
#         beta = 1/(kB*T[i])
#         dN_de_=[];N_=[];g_=[]
#         for j in range(len(E)):
#             N_.append(1/(np.exp(np.multiply(MeV*beta*e,(E[j]-meu)))-1))
#             g_.append(Cr*(E[j])**2)
#             dN_de_.append(Cr*((E[j])**2)/(np.exp((MeV*e/(kB*T[i]))*(E[j]-meu))-1))
#         N.append(N_);g.append(g_);dN_de.append(dN_de_)
#     return N,g,dN_de
# T = [10**8,10**9]
# N,g,dN_de = rel_fermi_dirac()
# plot(E, N, g, dN_de, T,"relativistic bose einstien")

# for i in range(len(T)):
#     U = total_internal_energy(E, N[i], g[i])
#     print(f'T={T[i]}K: U={U} J')

# for i in range(len(T)):
#     P = pressure(E, N[i], g[i], T[i])
#     print(f'T={T[i]}K: P={P} Pa')
