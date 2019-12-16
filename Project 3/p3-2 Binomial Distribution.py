import numpy as np
import matplotlib.pyplot as plt
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

successes = [0,1,2,3,4,5,6]
trials = 1000;
N = 9
s = np.zeros((N, 1))
p= .001
for x in range(N):
    s[x] = nCr(trials,x) * p**x * (1-p)**(trials-x)
    
# Plotting
b = range (0, N + 1)
sb = np.size(b)
h1, bin_edges = np.histogram(successes, bins = b)
b1 = bin_edges[0:sb-1]
plt.close('all')
prob = s
        
# Plots and labels
plt.stem(b1,prob)
plt.title('Bernoulli Trials: PMF – Binomial Formula', fontsize = 14, fontweight = 'bold')
plt.xlabel('Number of Success', fontsize = 14)
plt.ylabel('Probability', fontsize = 14)
plt.xticks(b1)        
        
        

