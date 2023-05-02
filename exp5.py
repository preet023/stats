import numpy as np
from scipy.integrate import quad
from scipy import stats
import matplotlib.pyplot as plt
xmin=0;xmax=12
x=np.linspace(xmin,xmax,100)
k = 1.38e-23;h=6.626e-34;c=3e8

def f_p(x):
    return (x**3)/((np.exp(x)-1))
output = f_p(x)
y = np.array(output)
y_p = max(output[1:])
I = np.where(y == y_p)[0][0]
x_p = x[I]
print("x_p =",x_p)
print("b =",h*c/(k*x_p))
I = quad(f_p,0,np.inf)
print("I_p =",I[0])
print("I_p theoretical(pi^4/15) =",((np.pi)**4)/15)
plt.scatter(x,output)
plt.xlabel("x")
plt.ylabel(r"$f_p$")
plt.grid()
plt.show()

T = np.linspace(100,10000,20)

c_ = (8*(np.pi**2)*(k**4))/((h*c)**3)
C_T = []
U = []
F = []
for i in T:
    C_t = c_*(i**4)
    C_T.append(C_t)
    u = ((np.pi**4)/15)*(C_t)
    U.append(u)
    F.append((c/4)*u)  
    
plt.plot(T,F)
plt.xlabel("T")
plt.ylabel("F(T)")
plt.grid()
plt.show()


slope, intercept, r, p, se = stats.linregress(np.log(T),np.log(F))
print("slope =" ,slope , "intercept = ",intercept)
print("stephen constant",np.exp(intercept))
plt.plot(np.log(T),np.log(F))
# plt.plot(np.log(T),np.log(F),'-gD',markevery = np.where(np.log(F)==intercept))
plt.xlabel("log(T)")
plt.ylabel("log(F(T))")
# plt.xlim([-1,9])
# plt.ylim([-20,20])
plt.grid()
plt.show()

I = quad(f_p,xmin,xmax)
x_=np.linspace(0,12,10000)
for i in x_[100:]:
    I_ = quad(f_p,xmin,i)[0]
    if abs(I_-(I[0]/2))<=0.001:
        print("x_mean",i)
        break
print("Area/2 =",I[0]/2)
print("b=",h*c/(k*(i)))