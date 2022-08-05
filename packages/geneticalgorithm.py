# Installation (Uncomment the line below)
#!pip install geneticalgorithm

import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# Define charateristics of variables:
varbound=np.array([[0,1],[0,1]])
vartype=np.array([['real'],['real']])

# Define settings of the algorithm:
algorithm_param = {'max_num_iteration': 100,\
                   'population_size':60,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}  
    
# Define your optimization model:
def MyOptProb(X):
    y = 0+X[1]*(1.29-0)
    x = np.round(0+X[0]*(2-0))
    g1 = 5/10 * x + 3/10 * y - 1
    g2 = 2/9 * x + 7/9 * y - 1
    penalty = np.amax(np.array([0,g1,g2]))
    return -(2*x+5*y)+150*penalty**2

# Define a solution retriever:
def Results(obj, variables):
    x = round(0+variables[0]*(2-0))
    y = 0+variables[0]*(1.29-0)
    g1 = 5 * x + 3 * y - 10
    g2 = 2 * x + 7 * y - 9
    print(g1)
    print(g2)
    if g1>10e-6 or g2>10e-6:
      print("infeasible")
    else:
      print("feasible")
    print("x:",x)
    print("y:",y)
    print("obj:",2*x+5*y)

# Model and solve the problem:
model=ga(function=MyOptProb,dimension=2,variable_type_mixed=vartype,variable_boundaries=varbound,algorithm_parameters=algorithm_param)
model.run()

# Display results:    
Results(model.best_function,model.best_variable)   
