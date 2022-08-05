import numpy as np
import itertools as it

B = [[-3,12.1],[4.1,5.8]] #Bounds (x,y)
P = [4, 4] #Precision
T = range(10) #Population size
S = range(1000) #Iterations
Cr = 0.6; #Crossover rate
Mu = 0.2; #Mutation rate
D = range(len(B)) #Dimension
I = {d: range(int(np.floor(np.log2((B[d][1]-B[d][0])*10**P[d])))+1) for d in D} #Chromosome length

def obj(x, y):
    return 21.5+x*np.sin(4*np.pi*x)+y*np.sin(20*np.pi*y)
    
def argmax(x):
    return max(range(len(x)), key=lambda i: x[i])

best = {s: -np.infty for s in S}

#Encoding
a = {d: {(t,i): np.random.randint(0,1) for t,i in it.product(T,I[d])} for d in D}

for s in S:
    
    #Decoding
    x = {d: {t: B[d][0]+ ((sum((2**i)*a[d][(t,i)] for i in I[d]))/((2**len(I[d]))-1))*(B[d][1]-B[d][0]) for t in T} for d in D}
    
    #Evaluation
    g = {t: obj(x[0][t],x[1][t]) for t in T}
    
    #Selection
    aa = a.copy()
    r = {t: np.random.rand() for t in T}
    q = {tt: sum(g[t] for t in range(tt+1))/sum(g[t] for t in T) for tt in T}
    a = {d: {(t,i): aa[d][(0,i)] if r[t] <= q[0] else aa[d][(tt,i)] if tt!=0 and r[t] > q[tt-1] and r[t] <= q[tt] else aa[d][(t,i)] for t,tt,i in it.product(T,T,I[d])} for d in D}
    
    #Crossover
    aa = a.copy()
    r = {t: np.random.rand() for t in T}
    cross = {(t,tt): 1 if r[t] < Cr and r[tt] < Cr and t<tt else 0 for t,tt in it.product(T,T)}
    pos = {d: {(t,tt): np.random.randint(0,len(I[d])-1) if cross[(t,tt)]==1 else 0 for t,tt in it.product(T,T) } for d in D}
    a = {d: {(t,i): aa[d][(tt,i)] if cross[(t,tt)]==1 and t<tt else aa[d][(tt,i)] if cross[(tt,t)]==1 and t>tt else aa[d][(t,i)] for t,tt in it.product(T,T) for i in range(pos[d][(t,tt)],len(I[d]),1)} for d in D}
  
    #Mutation
    aa = a.copy()
    r = {d: {(t,i): np.random.rand() for t,i in it.product(T,I[d])} for d in D}
    a = {d: {(t,i): 1 if aa[d][(t,i)]==0 and r[d][(t,i)]<Mu else 0 if r[d][(t,i)]<Mu else aa[d][(t,i)] for t,i in it.product(T,I[d])} for d in D}
    
    objval = max(list(g.values()))
    idx    = argmax(list(g.values()))
    if s ==0: best[s] = objval
    else:
        if objval>best[s-1]: 
            best[s] = objval
            x_best=[x[0][idx],x[1][idx]]
        else: best[s] = best[s-1]

