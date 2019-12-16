import numpy as np
import matplotlib.pyplot as plt

p0 = (.1, .1, .1, .3, .2, .2)
c = [1,2,3,4,5,6]
trials = 1000;
N = 10000
s = np.zeros((N, 1))
largest = 0
for i in range(N):
    success = 0
    d1 = np.random.choice(c,trials,p=p0)
    d2 = np.random.choice(c,trials,p=p0)
    d3 = np.random.choice(c,trials,p=p0)
    for x in range(len(d1)):
        if (d1[x] == 1 and d2[x] == 1 and d3[x] == 3):
            success = success + 1
    if success > largest:
        largest = success
    s[i] = success
# Plotting
b = range (0, largest + 2)
sb = np.size(b)
h1, bin_edges = np.histogram(s, bins = b)
b1 = bin_edges[0:sb-1]
plt.close('all')
prob = h1/N
        
# Plots and labels
plt.stem(b1,prob)
plt.title('Bernoulli Trials: PMF - Experimental', fontsize = 14, fontweight = 'bold')
plt.xlabel('Number of Success', fontsize = 14)
plt.ylabel('Probability', fontsize = 14)
plt.xticks(b1)        
        
        

