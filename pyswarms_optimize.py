# Installation (Uncomment the line below)
# !pip install pyswarms

from pyswarms.single.global_best import GlobalBestPSO
import numpy as np

# Define charateristics of variables:
x_min = [0, 0]
x_max = [1, 1]
bounds = (x_min, x_max)
dim = len(x_min)

# Define settings of the algorithm:
pop = 100
iterations = 250
options = {'c1': 0.5, 'c2': 0.4, 'w': 0.9}

# Define your optimization model:
def MyOptProb(x):
    y = 0 + x[:, 1] * (1.29 - 0)
    x = np.round(0 + x[:, 0] * (2 - 0))
    g1 = 5 / 10 * x + 3 / 10 * y - 1
    g2 = 2 / 9 * x + 7 / 9 * y - 1
    penalty = np.amax(np.array([np.zeros(pop), g1, g2]))
    return -(2 * x + 5 * y) + 150 * penalty ** 2

# Define a solution retriever:
def Results(obj, variables):
    x = round(0 + variables[0] * (2 - 0))
    y = 0 + variables[0] * (1.29 - 0)
    g1 = 5 * x + 3 * y - 10
    g2 = 2 * x + 7 * y - 9
    if g1 > 10e-6 or g2 > 10e-6:
        print ('infeasible')
    else:
        print ('feasible')
    print ('x:', x)
    print ('y:', y)
    print ('obj:', 2 * x + 5 * y)

# Model and solve the problem:
optimizer = GlobalBestPSO(n_particles=pop, dimensions=dim,
                          options=options, bounds=bounds)
(obj, variables) = optimizer.optimize(MyOptProb, iterations)

# Display results:
Results(obj, variables)
