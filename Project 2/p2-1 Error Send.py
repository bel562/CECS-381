import numpy as np

def nSidedDie(p):
        n = len(p)
        array = np.array(p)
        cs = np.cumsum(array)
        cp = np.append(0,cs)
        r = np.random.rand()
        for k in range(0,n):
                if r > cp[k] and r <= cp[k+1]:
                    d = k + 1
                    return d

    
failure = 0
N = 100000
for x in range(N):         
    p= [0.35, 1-.35]
    S = nSidedDie(p) -1
    if S == 0:
        R = nSidedDie([1-.04, .04]) - 1
    else:
        R = nSidedDie([.07, 1-.07]) - 1
    if S != R:
        failure += 1
failureRate = failure / N #.05961
