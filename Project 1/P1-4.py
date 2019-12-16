import numpy as np
def probOfHack(m,k):
    success = 0
    N = 1000
    n = 26**4
    for i in range(0,N):
        password = np.random.randint (0,n)
        hackerList = np.random.randint(0,n,m*k)
        if (password in hackerList):
            success += 1
    prob = success / N
    return prob

m = 70000
prob1 = probOfHack(m,1)#recorded answer .135
prob2 = probOfHack(m,7)#recorded answer .629

expectedProb = 0.5
result = 0
while  result < (expectedProb - .02):
    m += 1000
    result = probOfHack(m,1) #recorded answer m = 280000
    
    
