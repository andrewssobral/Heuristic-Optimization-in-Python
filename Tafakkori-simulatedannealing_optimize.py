# PART 1

import numpy as np

B = [[-3,12.1],[4.1,5.8]] #Bounds (x,y)
S = range(1000) #Iterations
D = range(len(B)) #Dimension
C = range(50) #Cooling cycles
max_temp = 10000 #Maximum temperature

def obj(x, y):
    return 21.5+x*np.sin(4*np.pi*x)+y*np.sin(20*np.pi*y)

best = {s: None for s in S}
b = -np.infty

#Encoding
a = {d: np.random.rand() for d in D}
aa = a.copy()

for s in S:

    temp = ((len(S)-s)/len(S))*max_temp

    for c in C:
    
        #Decoding
        x = {d: B[d][0]+a[d]*(B[d][1]-B[d][0]) for d in D}
        
        #Evaluation
        g = obj(x[0],x[1])
        
        #Selection
        diff = abs(g-b)
        select = {0: 1 if g>b or np.random.rand()<np.exp(-diff/temp) else 0}
        a = {d: a[d] if select[0]==1 else aa[d] for d in D}

        #Neighborhood search
        aa = a.copy()
        a = {d: a[d] + 2*np.random.rand()-1 for d in D}
        a = {d: 1 if a[d] >1 else 0 if a[d] <0 else a[d] for d in D}

        if g>b: b = g ; x_best = [x[0],x[1]]

    best[s] = b

# PART 2

import matplotlib.pyplot as plt

def plot_landscape():
    x = np.linspace(-3, 12.1, 30)
    y = np.linspace(4.1, 5.8, 30)
    X, Y = np.meshgrid(x, y)
    Z = obj(X, Y)
    plt.figure(dpi=1200)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')

def plot_convergence():
    plt.figure(dpi=1200)
    plt.plot(list(S),list(best.values()))

def report_solution():
    print('Objective value =', best[len(S)-1])
    print(x_best)

plot_landscape()
plot_convergence()     
report_solution()
