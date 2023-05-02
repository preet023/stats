import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import binom
#Heads = 0
#Tails = 1
def toss(N_c):
    outcomes = []
    for i in range(0, N_c):
        result = random.randint(0,1)
        outcomes.append(result)
    return outcomes

def macrostates(N_c, N_t): #Number of Heads in each trial and then count how many times particular number of heads are attained
    counts = np.zeros(N_c+1)
    print(len(counts))
    ensemble = [];sum_head=[];prob_head=[]
    for j in range(0, N_t):
        temp = toss(N_c)
        for i in range(0, N_c+1):
            if sum(temp) == i:
                sum_head.append(sum(temp))
                prob_head.append(sum(sum_head)/((j+1)*N_c))
                counts[i] = counts[i] + 1
        ensemble.append(temp)
    return counts,prob_head
def frequency(N_c, N_t):
    freq = []
    counts,prob_head = macrostates(N_c, N_t)
    for i in range(0, N_c+1):
        freq.append(counts[i]/sum(counts))
    print(sum(counts))
    return freq,prob_head

def plot1(N_c, N_t):
    heads = np.arange(0,N_c + 1)
    for i in range(len(N_t)):
        plt.plot(heads, frequency(N_c, N_t[i])[0], label = f'N_t = {N_t[i]/N_c}N_c',marker="*")
    plt.plot(x, binom.pmf(x, n, p), 'bo',label='binomial Probability Mass Function')
    plt.xlabel('No of Heads')
    plt.ylabel('Frequency of Heads')
    plt.title('Frequency Vs No of Heads for 10 coins')
    plt.grid()
    plt.legend()
    plt.show()
N_c=10
N_T = np.multiply([10, 50, 100, 500,1000,10000],N_c)
#Bionomial Probability Distribution
n, p = N_c, 0.5
# mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
x = np.arange(binom.ppf(0.01, n, p),
              binom.ppf(0.99, n, p))
plot1(N_c, N_T)

def plot2(N_c, N_t):
    for j in N_c:
        heads = np.arange(0,j+1)    
        plt.plot(heads, frequency(j, N_t)[0], label = f'No of Coins = {j}',marker="*")
        plt.xlabel('No of Coins')
        plt.ylabel('Frequency of Heads')
        plt.title('Frequency of Heads Vs No of Coins  for 100 Trials')
        plt.grid(True)
        plt.legend()
    plt.show()
# plot2(np.arange(1,11,1),100)

def plot3(N_c, N_t):
    Trials = np.arange(0,N_t)
    plt.plot(Trials, frequency(N_c, N_t)[1], label = f'N_t = {N_t}',marker="*")
    plt.xlabel('No of Trials')
    plt.ylabel('Probability of Heads')
    plt.title('Probability of Heads Vs Number of Trials for 5 coins for 10000 Trials ')
    plt.grid()
    plt.legend()
    plt.show()
N_c,N_t=5,10000
# plot3(N_c,N_t)