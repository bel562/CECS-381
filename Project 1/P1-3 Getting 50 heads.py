import numpy as np
N = 100000
success = 0
for i in range (0,N):   
    results = np.random.randint(0,2,100)
    heads = sum(results)
    if heads == 50:
        success += 1
        
prob = success / N #results at around 0.0791
