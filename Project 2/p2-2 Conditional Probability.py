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

    
success = 0
total = 0
N = 100000
for x in range(N):         
    p= [0.35, 1-.35]
    S = nSidedDie(p) -1
    if S == 1:
        total += 1
        R = nSidedDie([.07, 1-.07]) - 1
        if S == R:
            success += 1
    
successRate = success / total #.93024

