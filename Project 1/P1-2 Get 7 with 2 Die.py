import numpy as np
import matplotlib.pyplot as plt

N = 100000
s = np.zeros((N, 1))

for k in range (0,N):
    total = 0
    rolls = 0
    while total != 7:
        rolls += 1
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)
        total = d1 + d2
    s[k] = rolls
    
    
    

# Plotting
b = range (1,  int(s.max() + 2))
sb = np.size(b)
h1, bin_edges = np.histogram(s, bins = b)
b1 = bin_edges[0:sb-1]
plt.close('all')
prob = h1/N
# Plots and labels
plt.stem(b1,prob)
plt.title('Rolls to get 7 with 2 Dice', fontsize = 14, fontweight = 'bold')
plt.xlabel('Success Roll', fontsize = 14)
plt.ylabel('Probability', fontsize = 14)
plt.xticks(b1)

