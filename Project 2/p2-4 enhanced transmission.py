import numpy as np

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

    
failure = 0
N = 100000
p= [0.35, 1-.35]

for x in range(N):         
    D = 1
    S = nSidedDie(p) - 1
    R = []
    
    for i in range(3):
        if S == 0:
            R.append(nSidedDie([1-.04, .04]) - 1)
            
        else:
            R.append(nSidedDie([.07, 1-.07]) - 1)
   
    if sum(R) < 2:
        D = 0
    if S != D:
        failure += 1
        
failureRate = failure / N #.01064
