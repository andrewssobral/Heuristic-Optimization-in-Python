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