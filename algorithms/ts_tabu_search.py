import numpy as np

B = [[-3,12.1],[4.1,5.8]] #Bounds (x,y)
S = range(1000) #Iterations
D = range(len(B)) #Dimension
C = 10 #Tabu list length

def obj(x, y):
    return 21.5+x*np.sin(4*np.pi*x)+y*np.sin(20*np.pi*y)

best = {s: None for s in S}
T = []

#Encoding
a = {d: np.random.rand() for d in D}

for s in S:
    
    #Decoding
    x = {d: B[d][0]+a[d]*(B[d][1]-B[d][0]) for d in D}
    
    #Evaluation
    g = obj(x[0],x[1])
    
    #Selection
    notcontains = {0: True if a!=aa else False for aa in T}
    if s ==0:  best[s] = g; a_best=a
    else: 
        if g>best[s-1] and notcontains[0]: best[s] = g; x_best  = x; a_best=a.copy()
        else: best[s] = best[s-1]       
  
    #Memorizing
    T.append(a_best)
    if (len(T) > C): T.pop(0)
    
    #Neighborhood search
    a = {d: a_best[d] + 2*np.random.rand()-1 for d in D}
    
    #Reparation
    a = {d: 1 if a[d] >1 else 0 if a[d] <0 else a[d] for d in D}