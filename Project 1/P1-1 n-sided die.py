import numpy as np
import matplotlib.pyplot as plt

def nSidedDie(p):
        n = len(p)
        array = np.array(p)
        #
        cs = np.cumsum(array)
        cp = np.append(0,cs)
        r = np.random.rand()
        for k in range(0,n):
                if r > cp[k] and r <= cp[k+1]:
                    d = k + 1
                    return d

    

            
p=[0.10,  0.15,  0.20,  0.35, 0.20]
N = 10000
s = np.zeros((N, 1))
n = len(p)
for i in range (0,N):
    r = nSidedDie(p)            
    s[i] = r
            
# Plotting
b = range (1, n + 2)
sb = np.size(b)
h1, bin_edges = np.histogram(s, bins = b)
b1 = bin_edges[0:sb-1]
plt.close('all')
prob = h1/N
        
# Plots and labels
plt.stem(b1,prob)
plt.title('PMF for an unfair n-sided die', fontsize = 14, fontweight = 'bold')
plt.xlabel('Number on the face of the die', fontsize = 14)
plt.ylabel('Probability', fontsize = 14)
plt.xticks(b1)
